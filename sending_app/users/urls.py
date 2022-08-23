from django.urls import path, include
from sending_app.urls import router

from users.views import ClientViewSet

router.register(r'clients', ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

