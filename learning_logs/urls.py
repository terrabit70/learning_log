"""URL schemes for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    path('about/', views.about, name='about'),
]
