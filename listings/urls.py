from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
# (no routes yet – just to avoid import error)

urlpatterns = [
    path('', include(router.urls)),
]
