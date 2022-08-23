from django.urls import path, include
from .views import MessageViewSet, MailingViewSet, AllStatisticView, \
    MailingStatisticView
from sending_app.urls import router

router.register(r'messages', MessageViewSet)
router.register(r'mailing', MailingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('statistic/', AllStatisticView.as_view()),
    path('statistic/mailing/<uuid:pk>', MailingStatisticView.as_view()),
]