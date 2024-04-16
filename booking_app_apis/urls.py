from django.urls import path
from booking_app_apis import views
urlpatterns = [
    path('schedule/', views.FlightScheduleAPIView.as_view(), name='flight_schedule_apis_view'),
    
]
