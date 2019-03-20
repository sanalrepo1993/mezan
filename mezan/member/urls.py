from django.urls import path,include
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'members_list', views.MasjidViewSet)


urlpatterns = [
    path('',views.home),
    #path('add/', views.add),
    #path('api/', include(router.urls)),
    #path('details/<int:id>',views.details),
    #path('edit/<int:id>',views.edit),
    #path('delete/<int:id>',views.delete),
]