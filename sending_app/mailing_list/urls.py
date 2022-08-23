from django.urls import path, include
from rest_framework import routers

from .views import MessageViewSet, MailingViewSet, AllStatisticView, \
    MailingStatisticView
# from sending_app.urls import router


router_mailing = routers.DefaultRouter()

router_mailing.register(r'messages', MessageViewSet)
router_mailing.register(r'mailing', MailingViewSet)

urlpatterns = [
    path('', include(router_mailing.urls)),
    path('statistic/', AllStatisticView.as_view()),
    path('statistic/mailing/<uuid:pk>', MailingStatisticView.as_view()),
]