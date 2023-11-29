from django.urls import path

from.import views

app_name ='App'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name='contact' ),
    path('services/', views.service, name = 'service'),
    path('about/', views.about, name = 'about'),
    path('cars/', views.cars, name = 'cars'),
    path('blog/', views.blog, name = 'blog'),
    path('enterdetails', views.enterdetails, name = 'enterdetails')
]