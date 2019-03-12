from my_blog.models.article import Article
from django.views.generic import ListView, DetailView


class PostsListView(ListView): # представление в виде списка
    model = Article                  # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Article