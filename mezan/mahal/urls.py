from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'mahal_list', views.MahalViewSet)


urlpatterns = [
    path('',views.home),
    path('edit/', views.edit),
    path('api/', include(router.urls)),
]