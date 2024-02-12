from django.urls import path
from . import consumers as cms

websocket_urlpatterns=[
    path('ws/fleettracking/<str:truckid>/',cms.FleetTrackConsumer.as_asgi()),
    path('ws/sendnotification/<str:fleetuser>/',cms.NotificationToFleet.as_asgi()),
]