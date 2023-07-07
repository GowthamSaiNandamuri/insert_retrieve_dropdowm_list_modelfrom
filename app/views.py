from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def dept_insert(request):
  if request.method=='POST':
    de=DEPTNO=request.POST.get('d')
    dn=DNAME=request.POST.get('e')
    dl=LOC=request.POST.get('p')
    TO=Dept.objects.get_or_create(DEPTNO=de,DNAME=dn,LOC=dl)[0]
    TO.save()
    return HttpResponse('DEPT DATA IS INSERTED ')  
  return render(request,'dept_insert.html')
    
