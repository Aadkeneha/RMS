from django.shortcuts import render,redirect,HttpResponse
from . import models
from django.contrib import messages
from .models import Project_Guide,Project_Group


user_guide = ""
user_group = ""
group_guide = ""
cpunt_reg = ""
flag_s = False
rad = ""
def guide_register(request):
   if request.method == "POST":
        guide = request.POST.get('guide', False)
        pass_g1 = request.POST.get('pass_g1', False)
        pass_g2 = request.POST.get('pass_g1', False)
        m_g = request.POST.get('m_g', False)
        eid_g = request.POST.get('eid_g', False)
        total_grps = request.POST.get('total_grps', False)
        dept = request.POST.get('dept', False)
        sub = request.POST.get('sub', False)
        inst = request.POST.get('inst', False)

        ins = models.Project_Guide(guide=guide, m_g=m_g, eid_g=eid_g, pass_g1=pass_g1, pass_g2=pass_g2,
                                   total_grps=total_grps, dept=dept, sub=sub, inst=inst)
        ins.save()

        print("Data has been saved")

   return render(request, 'guide_register.html')




def group_register(request):
    submit = models.Project_Group.objects.all()
    prof = models.Project_Guide.objects.all()

    stu = {
        'grp': submit,
        "guide": prof
    }

    if request.method == "POST":
        grp_number = request.POST.get('grp_number', False)
        guide = models.Project_Guide.objects.get(guide=request.POST.get('guide'))
        proj_name = request.POST.get('proj_name', False)
        mem1 = request.POST.get('mem1', False)
        mem2 = request.POST.get('mem2', False)
        eid1 = request.POST.get('eid1', False)
        eid2 = request.POST.get('eid2', False)
        mob_number1 = request.POST.get('mob_number1', False)
        mob_number2 = request.POST.get('mob_number2', False)
        pass_p1 = request.POST.get('pass_p1', False)
        pass_p2 = request.POST.get('pass_p1', False)

        ins = models.Project_Group(grp_number=grp_number, guide=guide, proj_name=proj_name, mem1=mem1, mem2=mem2,
                                   eid1=eid1,
                                   eid2=eid2, mob_number1=mob_number1,
                                   mob_number2=mob_number2, pass_p1=pass_p1, pass_p2=pass_p2)
        print("Data has been saved")
        ins.save()
    return render(request,'group_register.html',stu)


# final code for guide login
def guide_login(request):
    global user_guide
    if request.method == "POST":
        username = request.POST.get('username', False)
        password= request.POST.get('password', False)

        bool_ans = models.Project_Guide.objects.filter(guide=username, pass_g1=password).exists()

        if bool_ans == True:
            user_guide = username
            print(user_guide)
            return redirect( 'guide_account.html')

        if bool_ans == False:
            return HttpResponse('<script>alert("Please enter valid credentials"); location.assign("/");</script>')
    return render(request, 'guide_login.html')


#final code  for group login
def group_login(request):
    global user_group
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        bool_ans = models.Project_Group.objects.filter(grp_number=username, pass_p1=password).exists()

        if bool_ans == True:
            user_group = username
            print(user_group)
            return redirect('group_dashboard.html')

        if bool_ans == False:
            return HttpResponse(
                '<script>alert("Please enter valid credentials"); location.assign("group_login.html");</script>')


    return render(request,'group_login.html')



# need to change after adtion of neha wala front end ka part
def submitted_projects(request):
    global user_guide,flag_s
    submit = models.Project_Group.objects.filter(status = "N",guide = user_guide,flag = True )

    lst = models.Project_Guide.objects.filter(guide=user_guide)
    stu = {
        'guide': lst,
        'grp': submit
    }
    if request.method == "POST":
        Number = request.POST.get('number', False)
        remark = request.POST.get('remark', False)
        val = request.POST.get('btn_a', False)
        flag_s = True
        print(val)
        grp = models.Project_Group.objects.all().order_by('grp_number').filter(grp_number = Number)
        for i in grp:
            bool_ans = models.Project_Group.objects.filter(grp_number=Number).exists()
            if bool_ans == True:
                i.remark = remark
                i.save()
                print("remark saved")
                if val == "A":
                   flag_s = True
                   i.flag = flag_s
                   i.status = "A"
                   i.save()
                   print("Approved")
                else:
                    flag_s = False
                    i.flag = flag_s
                    i.status = "R"
                    i.save()
                    print("Returned")
    return render(request,'submitted_projects.html',stu)


#final for registered Groups
def registered_groups(request):
    global user_guide
    all = models.Project_Group.objects.filter(guide = user_guide)
    lst = models.Project_Guide.objects.filter(guide=user_guide)

    stu = {
        'guide': lst,
        'grp': all,
    }

    return render(request,'registered_groups.html',stu)

#temp code for all projects remaining for subject wise diaplay ka pattern
def all_projects(request):
    submit = models.Project_Group.objects.filter(status = "A",flag = True)
    stu = {
        'grp': submit
    }

    return render(request,'all_projects.html',stu)


def index(request):

    return render(request,'index.html')



def group_account(request):
    st = "Null"
    global user_group,rad
    if user_group != "":
        gr = models.Project_Group.objects.filter(grp_number = user_group)

        if request.method == "POST":
            f1 = request.FILES.get('f1')
            f2 = request.FILES.get('f2')
            f3 = request.FILES.get('f3')
            for i in gr:
                i.f1 = f1
                i.save()
                i.f2 = f2
                i.save()
                i.f3 = f3
                i.save()
                print("Details saved")
                i.flag = True
                i.save()
                i.status = "N"
                i.save()
        for i in gr:
            rad = i.guide
            print(rad)
            gd = models.Project_Guide.objects.filter(guide=rad)
            if i.status == "A":
                st = "Approved"
            elif i.status == "R":
                st = "Returned"
            if i.flag == True:
                fg = "Submitted"
            elif i.flag == False:
                fg = "Not Submitted"
        stu = {
            "grp_number": gr,
            "guide": gd,
            "st": st,
            "fg": fg
        }
    return render(request, 'group_account.html',stu)

# almost final
def guide_account(request):
    global user_guide,flag_s
    if user_guide != "":
        gd = models.Project_Guide.objects.filter(guide = user_guide)
        count = Project_Group.objects.filter(guide = user_guide).count()
        count_s = models.Project_Group.objects.filter(status="N", guide=user_guide,flag = True).count()

        if request.method == "POST":
            ins = request.POST.get('inst')


            for i in gd:
              i.inst = ins
              i.save()

        stu = {"guide": gd,
               "count":count,
               "count_s":count_s
               }
    return render(request,'guide_account.html',stu)


def group_dashboard(request):
    st = "Null"
    stu = {}
    global user_group, rad
    if user_group != "":
        gr = models.Project_Group.objects.filter(grp_number=user_group)
        for i in gr:
            rad = i.guide
            print(rad)
            gd = models.Project_Guide.objects.filter(guide=rad)
            if i.status == "A":
                st = "Approved"
            elif i.status == "R":
                st = "Returned"
            if i.flag == True:
                fg = "Submitted"
            elif i.flag == False:
                fg ="Not Submitted"
        stu = {
            "grp_number": gr,
            "guide": gd,
            "st":st,
            "fg":fg
        }
    return render(request,'group_dashboard.html',stu)

def group_edit(request):
    global user_group
    if user_group != "":
        gr = models.Project_Group.objects.filter(grp_number = user_group)
        for i in gr:
            rad = i.guide
            print(rad)
            gd = models.Project_Guide.objects.filter(guide=rad)


        if request.method == "POST":
            pass_p2 = pass_p1 = request.POST.get('password', False)
            for i in gr:
                i.pass_p2 = pass_p2
                i.save()
                i.pass_p1 = pass_p1
                i.save()

                print("Details saved")
        stu = {
            "grp_number": gr,
            "guide": gd,

        }
    return render(request,'group_edit.html',stu)

def guide_edit(request):
    global user_guide, rad
    if user_guide!= "":
        gr = models.Project_Guide.objects.filter(guide=user_guide)
        for i in gr:
            rad = i.guide
            print(rad)
            gd = models.Project_Guide.objects.filter(guide=rad)

        if request.method == "POST":
            pass_p2 = pass_p1 = request.POST.get('password', False)
            for i in gr:
                i.pass_p2= pass_p2
                i.save()
                i.pass_p1 = pass_p1
                i.save()

                print("Details saved")
        stu = {
            "grp_number": gr,
            "guide": gd,
        }

    return render(request,'guide_edit.html',stu)

def about_us(request):
    return render(request,'about_us.html')

