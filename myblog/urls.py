from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='myblog-index'),
    path("post_detail/<int:pk>/", views.post_detail, name='myblog-post-detail'),
    path("post_edit/<int:pk>/", views.post_edit, name='myblog-post-edit'),
    path("post_delete/<int:pk>/", views.post_delete, name='myblog-post-delete'),
]

