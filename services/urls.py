from django.urls import path
from . import views

urlpatterns = [
    # path('', views.gallery, name='index'),
    path('', views.contact_view, name='index'),
    
]


# path('services/', views.services, name='services'),
#     path('book/', views.book_appointment, name='book_appointment'),
#     path('appointment-success/', views.appointment_success, name='appointment_success'),
#     path('reviews/', views.reviews, name='reviews'),
#     # path('gallery/', views.gallery, name='gallery'),
