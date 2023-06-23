from django.contrib import admin
from django.urls import path,include
from .views import EmployeeViewset,CompanyViewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'employees',EmployeeViewset)
router.register(r'companies',CompanyViewset)

urlpatterns = [
    path('',include(router.urls))
   


]
