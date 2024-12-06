from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_event, name= 'list-event' ),
    path('query/<str:event_uid>/', views.query_event_shows, name='query-event-shows'),
    path('delete/<str:event_uid>', views.delete_event, name = 'delete-event'),
    path('update/<str:event_uid>', views.update_event, name= 'update-event'),
    path('logout', views.logout_view , name = 'logout'),
]