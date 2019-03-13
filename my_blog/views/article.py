from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, View, TemplateView, DeleteView

from my_blog.decorator.authorized import authorized_only
from my_blog.forms import ArticleForm
from my_blog.models import Article, Subscription, ArticleRead


@method_decorator(authorized_only, name='dispatch')
class SubscribeView(View):

    def post(self, request):
        try:
            user_id = request.POST.get('pk')
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'error': 'User not found'})

        sub, created = Subscription.objects.get_or_create(user=user)

        if request.user in sub.subscribers.all():
            sub.subscribers.remove(request.user.id)
            subscribed = False
            Article.objects.filter(user_id=request.user.id, post__user_id=user_id).delete()
        else:
            sub.subscribers.add(request.user.id)
            subscribed = True
        sub.save()

        return JsonResponse({'status': 'ok', 'subscribed': subscribed})


class BlogView(DetailView):
    model = User
    template_name = 'blog/user.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['posts'] = Article.objects.filter(user_id=self.object.id).prefetch_related('user')
        return context


class PostCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect(reverse('blog:detail', args=(post.user_id, post.id)))


class PostDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context


class PostReadView(View):
    def post(self, request):
        try:
            post = Article.objects.exclude(user_id=request.user.id).get(pk=request.POST.get('post_id'))
        except Article.DoesNotExist:
            return JsonResponse({'status': 'error', 'error': 'Post dont found'})

        ArticleRead.objects.get_or_create(user=request.user, post=post)
        return JsonResponse({'status': 'ok'})


class PostDeleteView(DeleteView):
    model = Article

    def get_object(self, queryset=None):
        return get_object_or_404(Article, user_id=self.request.user.id, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('blog:base')