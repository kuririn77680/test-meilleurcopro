from django.urls import path
from .views import Statistics

urlpatterns = [
    path('', Statistics.as_view(), name='statistics'),
]