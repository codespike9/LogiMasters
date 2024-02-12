from Users.views import FleetManagerRegistration,FleetManagerLogin,FleetRegistration
from fleet.views import GetAllFleets,SendNotifications,GetAllNotifications
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router= DefaultRouter()




#investor urls
router.register(r'fleetmanagerregistration',FleetManagerRegistration,basename='fleetmanagerregistration')
router.register(r'fleetmanagerlogin',FleetManagerLogin,basename='fleetmanagerlogin')
router.register(r'fleetregistration',FleetRegistration,basename='fleetregistration')
router.register(r'getallfleets',GetAllFleets,basename='getallfleets')
router.register(r'sendnotification',SendNotifications,basename='sendnotification')
router.register(r'getallnotifications',GetAllNotifications,basename='getallnotifications')


urlpatterns =router.urls




urlpatterns = [
     path('',include(router.urls)),    
 ]