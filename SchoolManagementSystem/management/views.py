from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from models import FacultyOtherInfo,MainUserOtherInfo
import uuid


# Create your views here.

def invalid_user(request):
    return render(request,'management/invalid_user.html')

# @login_required(login_url='/management/login/')
def add_faculty(request):
    if request.method=='POST':
        data = request.POST.dict()
        data_save = User.objects.create_user(data['username'],data['email'],data['password'],first_name=data['first_name'],
                last_name=data['last_name'])
        data_save.save()
        uid = int(User.objects.get(username=data['username']).id)
        print uid
        param = MainUserOtherInfo.objects.get(f_id=uid)
        cid = param.cid
        userid = param.userid
        f_save_data = FacultyOtherInfo(f_id=uid,subject=data['subject'],contact=data['contact'],cid=cid,userid=userid)
        f_save_data.save()
        return HttpResponseRedirect('/management/home/')
    else:
        context = {}
        username = request.user.username
        context.update({'username':username})
        return render(request,'management/add_faculty.html',context)

def Login(request):
    if request.method=='POST':
        print request.POST.dict()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/management/home/')
        else:
            return HttpResponseRedirect('/management/invalid_user/')
    else:
        try:
            msg = request.session['msg']
            if msg:
                context = {'msg':msg}
                return render(request,'management/login.html',context)
        except:
            return render(request,'management/login.html')
        
# @login_required(login_url='/management/login/')
def Logout(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect('/management/')

# @login_required(login_url='/management/login/')
def home(request):
    context = {}
    username = request.user.username
    is_staff = request.user.is_staff
    uid = int(User.objects.get(username=username).id)
    print uid
    param = MainUserOtherInfo.objects.get(f_id=uid)
    cid = param.cid
    context.update({'username':username})
    if is_staff:
        params = FacultyOtherInfo.objects.filter(cid=cid).values_list('f_id',flat=True)
        print params
        context.update({'params':params})
        return render(request,'management/home.html',context)
    else:
        return render(request,'management/home1.html',context)
        

def register(request):
    if request.method=='POST':
        data = request.POST.dict()
        data_save = User.objects.create_user(data['username'],data['email'],data['password'],is_staff=True)
        data_save.save()
        uid = int(User.objects.get(username=data['username']).id)
        userid = uuid.uuid4()
        cid = str(data['username'])+'-'+str(userid)
        f_save_data = MainUserOtherInfo(f_id=uid,userid=userid,cid=cid)
        f_save_data.save()
        request.session['msg']='User created successfully'
        return HttpResponseRedirect('/management/login/')
    else:
        return render(request,'management/register.html')
    
    
def index(request):
    print request.META
    return render(request,'management/index.html')


def about(request):
    return render(request,'management/about.html')

def gallery(request):
    return render(request,'management/gallery.html')  
    