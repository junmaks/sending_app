from django.urls import path, include
# from sending_app.urls import router
from rest_framework import routers

from users.views import ClientViewSet

router_users = routers.DefaultRouter()


router_users.register(r'clients', ClientViewSet)

urlpatterns = [
    path("", include(router_users.urls)),
]

