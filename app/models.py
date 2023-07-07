from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.PositiveIntegerField(primary_key=True)
    DNAME=models.CharField(max_length=50)
    LOC=models.CharField(max_length=50)
    def _str_(self):
        return self.DNAME
    def _str_(self):
        return self.LOC

class Emp(models.Model):
    EMPNO=models.PositiveIntegerField(primary_key=True)
    ENAME=models.CharField(max_length=50)
    JOB=models.CharField(max_length=50)
    SAL=models.PositiveIntegerField()
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def _str_(self):
        return self.ENAME
    def _str_(self):
        return self.JOB