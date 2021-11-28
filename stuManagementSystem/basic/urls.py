from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('admin_office/', views.admin_office, name='admin_office'),
    path('admission/', views.admission, name='admission'),
    path('contact/', views.contact, name='contact'),
    path('admission_backend/', views.admission_backend, name='admission_backend')
]
