from django.urls import include, path
from rest_framework import routers
from foodApiApp import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
# router.register('foodApi', views.Saydur, basename="Custom Api")
# router.register('custom', views.CustomerViewSet, basename="Custom Api")
router.register('customer', views.CustomerViewSet, basename="Customer Name")
router.register('catagory', views.CatagoryViewSet, basename="Catagories")
router.register('specialOffer', views.SpecialOfferViewSet, basename="Special Offer")
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('saydur/',views.Saydur.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]