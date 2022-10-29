from django.urls import path

from recipes.web.views import index, delete_recipe, details_recipe, edit_recipe, create_recipe

'''
•	'/' - home page
•	'/create' - create recipe page
•	'/edit/:id' - edit recipe page
•	'/delete/:id' - delete recipe page
•	'/details/:id' - recipe details page
'''

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('details/<int:pk>', details_recipe, name='details recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),

)
