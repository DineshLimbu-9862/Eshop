from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def zero(request):

    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()  
       
    return render(request,'app1/index.html',{'form':form})
def list(request):
    data=Employee.objects.all()
    if request.method=="GET":
        ct=request.GET.get('searchname')
        if ct!=None:
         data=Employee.objects.filter(name__icontains=ct)
 
    return render(request,'app1/list.html',{'data':data})

# Delete View
def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')
    

# Update View
def Update_Record(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context)
