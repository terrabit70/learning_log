"""URL schemes for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic')
]