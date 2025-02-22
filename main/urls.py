from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:blog_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
    path('download-cv/', views.download_cv, name='download_cv'),
]
