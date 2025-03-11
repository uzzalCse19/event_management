

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.event_list,name='event_list'),
    path('event_detail/<int:pk>/',views.event_detail,name='event_detail'),
    path('event/create/',views.create_event,name='create_event'),
    path('event/<int:pk>/update/', views.update_event, name='update_event'),
    path('event/<int:pk>/delete/',views.delete_event,name='delete_event'),
    path('dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('search/',views.search_events,name='search_events'),
    path('categories/',views.category_list,name='category_list'),
    path('category/create/',views.create_category,name='create_category'),
    path('categories/<int:pk>/update/', views.update_category, name='update_category'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('participants/',views.participant_list,name='participant_list'),
    path('participants/create/',views.create_participant,name='create_participant'),
    path('participants/<int:pk>/update/',views.update_participant,name='update_participant'),
    path('participants/<int:pk>/delete/',views.delete_participant,name='delete_participant'),

]

