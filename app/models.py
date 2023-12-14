from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.dname
    


class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Sal=models.PositiveIntegerField()
    MGR=models.PositiveIntegerField()
    Hiredate=models.DateField()
    Comm=models.PositiveIntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.Ename
    


    
class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.IntegerField()
    highsal=models.IntegerField()


   


class Bonus(models.Model):
    bId=models.IntegerField(primary_key=True)
    bonus=models.IntegerField()



        
