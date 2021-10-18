# from django.conf.urls import url
from django.db import router
from django.urls import include, path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet,basename = "user")
schema_view = get_swagger_view(title = 'Documentation')

urlpatterns = [
    path('docs/',schema_view),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
