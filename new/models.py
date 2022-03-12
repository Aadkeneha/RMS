from django.shortcuts import render
from django.db import models




class Project_Guide(models.Model):

    guide = models.CharField(max_length=50,primary_key=True)
    pass_g1 = models.CharField(max_length=50,null  = True, blank = True ,default = "xyz")
    pass_g2 = models.CharField(max_length=50,null  = True, blank = True ,default = "xyz")
    m_g = models.CharField(max_length=10)
    eid_g = models.EmailField()
    total_grps = models.IntegerField(max_length=3,blank=True)
    dept = models.CharField(max_length=50)
    sub = models.CharField(max_length=50)
    inst = models.TextField(max_length=50,null  = True, blank = True )

    def __str__(self):
        return self.guide





class Project_Group(models.Model):
    grp_number = models.IntegerField(primary_key=True)

    proj_name = models.CharField(max_length=50)

    mem1 = models.CharField(max_length=50)
    mem2 = models.CharField(max_length=50)
    eid1 = models.EmailField()
    eid2 = models.EmailField()
    mob_number1 = models.CharField(max_length=10)
    mob_number2 = models.CharField(max_length=10)
    pass_p1 = models.CharField(max_length=10,null  = True, blank = True ,default = "xyz")
    pass_p2 = models.CharField(max_length=10,null  = True, blank = True ,default = "xyz")
    f1 = models.FileField(null  = True, blank = True )
    f2 = models.FileField(null  = True, blank = True )
    f3 = models.FileField(null  = True, blank = True )
    remark = models.CharField(max_length=1000,null  = True, blank = True ,default = " ")
    status = models.CharField(max_length=1, null=True, blank=True,default="N")
    guide = models.ForeignKey(Project_Guide, on_delete=models.CASCADE,default=" ")
    flag = models.BooleanField(default="False")














