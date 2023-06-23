from employee.models import Employee
# from django.shortcuts import render
from django.http import JsonResponse
# from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q
# from django.utils import timezone
import time,math
def showEmployee(request):
    if request.method == 'GET':
        empdata=[]

        try :
            response_data=list(Employee.objects.all().values())
            for data in response_data:
                id= data['employee_id']
                print(id)
                name=data.get('name')
                phone=data.get('phone')
                location=data.get('location')
                position=data.get('position')
                about=data.get('about')
                empdata.append({'employee_id':id,'name':name,'phone':phone,'location':location,'position':position,'about':about})        
            return JsonResponse(empdata,safe=False)
        except Exception as e:
            return JsonResponse( 'showEMployee'+str(e))
    return JsonResponse({'message': 'not able to fetch data'})
    
        
    
        

@csrf_exempt 
def newemployee(request):
    try:

     if request.method == 'POST':
        request_data = json.loads(request.body)
        print(request_data.get("name"))
        id="EMP"+str(math.floor(time.time()))
        name = request_data.get('name')
        location = request_data.get('location')
        phone = request_data.get('phone')
        position = request_data.get('position')
        about = request_data.get('about')
        if(validateData(id,name,phone)):
        #    if(Employee.objects.filter(employee_id=id).exists() or Employee.objects.filter(phone=str(phone)).exists()):
           if(Employee.objects.filter(Q(employee_id=id)|Q(phone=phone)).exists()):
              return JsonResponse({'message':'The EMployee id Already Exists'})
           else:
              newEmployee1=Employee(employee_id=id,name=name,phone=phone,location=location,position=position,about=about)
              print(request_data)
              newEmployee1.save()
              return JsonResponse( "thank you Employee Added",safe=False)
        else:
            return JsonResponse({'message':'Validation failed'})
    except Exception as e:
        # print("error",e)
        return JsonResponse( " fail "+e,safe=False)
    
@csrf_exempt                        
def updateEmployee(request,id):
    try:
        if request.method=='PUT':
            update_data=Employee.objects.get(employee_id=id)
            emp_data=json.loads(request.body)
            name=emp_data.get('name')
            about=emp_data.get('about')
            position=emp_data.get('position')
            location=emp_data.get('location')
            phone=emp_data.get('phone')
            if(validateData(id,name,phone)):
               print("hell")
               if not(Employee.objects.filter(phone=phone).exists()):
                   
                  update_data.name=name
                  update_data.position=position
                  update_data.about=about
                  update_data.location=location
                  update_data.phone=phone
                  update_data.save()
                  print(name)
                  return JsonResponse({'massage':'Employee update Success '})
               else:
                   return JsonResponse({'message':'this phone no already exists'})
            else:
                return JsonResponse({'message':'Validation Process failed'})
    except Exception as e:
        return JsonResponse("UpdateEmployee",e)

@csrf_exempt
def deleteEmployee(request,id):
    try:
        if request.method=='DELETE':
          delete_data=Employee.objects.get(employee_id=id)
          delete_data.delete()
        return  JsonResponse({"message": "deleted successfully"})
    except Exception as e:
        return JsonResponse("deleteEpmloyee",e)

def getEmployeeById(request,id):
    try:
        emp_data=Employee.objects.get(employee_id=id)
        if request.method=='GET':
            id=emp_data.employee_id
            name=emp_data.name
            phone=emp_data.phone
            about=emp_data.about
            position=emp_data.position
            location=emp_data.location
        return JsonResponse({'id':id,'name':name,'phone':phone,'about':about,'position':position,'locaton':location})
    except Exception as e:
        return JsonResponse("getElementbyid",e)
    



def validateData(id,name,phone):
        if(str(name).isalpha()):
             if(str(phone).isnumeric()):
                 return True
             else:
                return False
        else:
         return False
    


