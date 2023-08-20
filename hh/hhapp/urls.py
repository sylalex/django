from django.urls import path
from hhapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parsing/', views.ParsingFormView.as_view(), name='parsing'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),

]