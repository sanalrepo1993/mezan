from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'family_list', views.FamilyViewSet)
router.register(r'member_list', views.MemberViewSet)


urlpatterns = [
    path('',views.home),
    path('members/',views.fhome),
    path('add/family/', views.add_family),
    path('add/member/', views.add_member),
    path('api/', include(router.urls)),
    path('family/members/<int:id>',views.family_member),
    path('edit/<int:id>/<int:rid>',views.family_member_edit),
    path('delete/<int:id>/<int:rid>',views.delete),
    path('details/<int:id>',views.details)
]