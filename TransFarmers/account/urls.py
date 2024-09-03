from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.views import AccountView

router = DefaultRouter()
router.register(r'account', AccountView, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('email-duplication-check',
         AccountView.as_view({'post': 'checkEmailDuplication'}),
         name='account-email-duplication-check'),
    path("find-email", AccountView.as_view({"post": "findEmailByAccountId"}),
         name="find-email-by-account-id"),
    path('register',
         AccountView.as_view({'post': 'registerAccount'}),
         name='register-account'),
]
