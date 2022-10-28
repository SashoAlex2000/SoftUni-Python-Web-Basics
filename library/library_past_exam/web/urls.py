
from django.urls import path, include

from library_past_exam.web.views import index, \
    add_book, edit_book, details_book, delete_book, \
    profile_edit, profile_delete, profile_page

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('delete/<int:pk>', delete_book, name='delete book'),
    path('details/<int:pk>', details_book, name='details book'),
    path('profile/', include([
        path('', profile_page, name='profile page'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
)

