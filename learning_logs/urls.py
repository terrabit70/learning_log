"""URL schemes for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
]