from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from skincareapi.models import *
from skincareapi.views import *



router = routers.DefaultRouter(trailing_slash=False)
router.register(r"customers", CustomersViewSet, "customer")
router.register(r"skintypes", SkintypeViewSet, "skintype")
router.register(r"user", UsersViewSet, "user")
router.register(r"concerns", ConcernViewSet, "concern")
router.register(r"userconcerns", UserConcernsViewSet, "userconcern")
router.register(r"journal", JournalViewSet, "journal")

urlpatterns = [
    path('', include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("api-token-auth", obtain_auth_token),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),

]

