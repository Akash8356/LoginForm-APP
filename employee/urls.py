
from django.urls import path
from employee import views

urlpatterns = [
    path('',views.showEmployee),
    path('emp/',views.newemployee),
    path('update/<str:id>',views.updateEmployee),
    path('emp/<str:id>',views.getEmployeeById),
    path('delete/<str:id>',views.deleteEmployee),
   
]
