'''
•	http://localhost:8000/ - index page
•	http://localhost:8000/profile/create - profile create page
•	http://localhost:8000/catalogue/ - catalogue page
•	http://localhost:8000/car/create/ - car create page
•	http://localhost:8000/car/<car-id>/details/ - car details page
•	http://localhost:8000/car/<car-id>/edit/ - car edit page
•	http://localhost:8000/car/<car-id>/delete/ - car delete page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page

'''
from django.urls import path, include

from final_exam.web.views import catalogue, index,\
    profile_edit, profile_delete, profile_create, profile_details,\
    car_details, car_edit, car_create, car_delete

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('create/', car_create, name='create car'),
        path('<int:pk>/details/', car_details, name='details car'),
        path('<int:pk>/edit/', car_edit, name='edit car'),
        path('<int:pk>/delete/', car_delete, name='delete car'),
    ])),
)
