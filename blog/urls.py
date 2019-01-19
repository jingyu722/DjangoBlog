from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:article_id>/', views.detail_article, name='detail'),
    path('create/', views.create_view, name='create'),
    path('create/blog/', views.create_action, name='create_action'),
    path('<int:article_id>/comment', views.comment, name='comment'),
]
