from django.shortcuts import render
from . models import student
from . forms import studentRegistration

# Create your views here.

def studentinfo(request):
    # create model class variable and hold all query set in stud. all() fun return query set of model class
    stud = student.objects.all()
    # Configure id Attribute and label Tag and Dynamic initial Value in Django
    fm = studentRegistration(auto_id=True,label_suffix=' ',
                             initial={'stuid':21,'name':'rakib','email':'rakib@gmail.com','password':'123456'})
    # Ordering Form Field in Django
    fm.order_fields(field_order=['name','email','password','stuid'])
    return render(request,'enroll/student.html',{'std':stud,'form':fm})
    
    
