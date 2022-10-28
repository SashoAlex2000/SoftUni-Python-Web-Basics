from django.urls import path

from models_django.web.views import index

urlpatterns = (
    path('', index, name='index'),
)

