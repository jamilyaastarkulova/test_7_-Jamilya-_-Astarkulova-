from django.urls import path
from webapp.views import index_view, book_create_view, book_update_view, book_delete_view

urlpatterns = [
    path('', index_view, name='book_list'),
    path('book/add/', book_create_view, name='book_create'),
    path('book/<int:pk>/update/', book_update_view, name='book_update'),
    path('book/<int:pk>/delete/', book_delete_view, name='book_delete'),
]