from django.shortcuts import render

# Create your views here.
from app.models import *

def dept(request):
    DO=Dept.objects.all()
    d={'dept':DO}
    return render(request,'dept.html',d)


def emp(request):
    EO=Emp.objects.all()
    d={'emp':EO}
    return render(request,'emp.html',d)




def insert_dept(request):
    id=int(input('Enter the dept no: '))
    n=input('Enter the dept name: ')
    l=input('Enter the location: ')

    do=Dept.objects.get_or_create(deptno=id,dname=n,location=l)[0]
    do.save()
    DTO=Dept.objects.all()
    d={'dept':DTO}
    return render(request,'dept.html',d)




def insert_emp(request):
    e=int(input('Enter the emp no: '))
    n=input('Enter the emp name: ')
    j=input('Enter the designation: ')
    s=int(input('Enter the salary: '))
    m=int(input('Enter the mgr no.: '))
    h=input('Enter the hiredate: ')
    c=int(input('Enter the comm: '))
    d=int(input('Enter the dept no: '))

    do=Dept.objects.get(deptno=d)
    eo=Emp.objects.get_or_create(Empno=e,Ename=n,Job=j,Sal=s,MGR=m,Hiredate=h,Comm=c,deptno=do)[0]
    eo.save()
    ETO=Emp.objects.all()
    d={'emp':ETO}
    return render(request,'emp.html',d)



def insert_salgrade(request):
    g=int(input('Enter the  no: '))
    l=int(input('Enter the losal: '))
    h=int(input('Enter the highsal: '))

    so=Dept.objects.get_or_create(grade=g,losal=l,highsal=h)[0]
    so.save()
    STO=SalGrade.objects.all()
    d={'sg':STO}
    return render(request,'salgrade.html',d)






