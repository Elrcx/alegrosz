from django.urls import path

from . import views
from .views import ContactView

app_name = 'contact'

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),

]
