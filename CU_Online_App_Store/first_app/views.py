from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile, App_Profile, MyWishList
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    # return HttpResponse("Moja lagtese")
    # my_dict = {'insert_me':"Hello I am from view.py"}
    # return render(request,'first_app/index.html',context=my_dict)
    app_profiles = App_Profile.objects.all()
    print(app_profiles)
    return render(request,'index.html',{'app_profiles':app_profiles})

def dashboard(request,email):
    app_profiles = App_Profile.objects.all()
    # context = {'key':email}
    print(app_profiles)
    return render(request,'dashboard.html',{'app_profiles':app_profiles,'key':email})


def create(request):
    print(request.POST)
    name = request.GET['name']
    email = request.GET['email']
    catagory = request.GET['catagory']
    department = request.GET['department']
    dept_id = request.GET['dept_id']
    password = request.GET['password']
    confirm_password = request.GET['confirm_password']
    phone_no = request.GET['phone_no']
    about = request.GET['about']
    profile_info = Profile(name=name,email=email,catagory=catagory,department=department,dept_id=dept_id,password=password,confirm_password=confirm_password,phone_no=phone_no,about=about)
    profile_info.save()
    return redirect('/dashboard/'+email)
    # return render(request,'dashboard.html')

# def upload(request):
#     my_dict = {'insert_me':"Hello I am from first_app/index.html"}
#     return render(request,'upload.html',context=my_dict)

def auth(request):
    # print(request.POST)
    email = request.GET['email']
    password = request.GET['password']
    profiles = Profile.objects.all()
    # key = '/redirect/'+email
    # context = {'key':email}
    print(profiles)

    try:
        if Profile.objects.filter(email=email) and Profile.objects.filter(password=password):
            print("Email and password matched")
            return redirect('/dashboard/'+email)
                # return render(request,'/success',context)
    except:
            return redirect('/login')

def success(request):
    pass



def login(request):
    # my_dict = {'insert_me':"Please enter correct email or passoword"}
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def upload(request,email):
    # context = {}
    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        uploaded_image = request.FILES['image']
        # print(uploaded_file.name)
        # print("yes")
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        location = fs.save(uploaded_file.name,uploaded_file)
        image_location = fs.save(uploaded_image.name,uploaded_image)
        url = fs.url(location)
        image_url = fs.url(image_location)
        # print(url)
        # context['url'] = fs.url(location)
        context = {'url':fs.url(location),'image_url':fs.url(image_url)}
        app_name = request.POST['namea']
        developer = request.POST['developer']
        email = request.POST['email']
        size = uploaded_file.size
        version = request.POST['version']
        description = request.POST['description']
        app_profile_info = App_Profile(app_name=app_name,developer=developer,email=email,size=size,version=version,description=description,apklocation=url,imagelocation=image_url)
        print(app_profile_info)
        app_profile_info.save()
    return render(request, 'upload.html',{'key':email})

def delete(request,email,app_name):
    selectedApp = App_Profile.objects.get(app_name=app_name)
    selectedApp.delete()
    # return render(request,'myprofile.html')
    return redirect ('/myprofile/'+email)


def viewapp(request,email,app_name):
    selectedprofile = App_Profile.objects.get(app_name=app_name)
    return render(request,'appprofile.html',{'selectedprofile':selectedprofile,'key':email})


def myprofile(request,email):
    # my_dict = {'insert_me':"Hello I am from first_app/user.html"}
    profile = Profile.objects.get(email=email)
    appprofile = App_Profile.objects.all()
    print(appprofile)
    return render(request,'myprofile.html',{'profile':profile,'appprofile':appprofile,'key':email})

def addtowishlist(request,email,app_name):
    mylist = App_Profile.objects.get(app_name=app_name)
    addtolist = MyWishList(email=email,app_name=app_name)
    addtolist.save()
    # return redirect('viewapp/'+email+'/'+app_name)
    return redirect('/dashboard/'+email)
    # return render(request,'appprofile.html',{'selectedprofile':selectedprofile,'key':email})


def wishlist(request,email):
    # app_names =  MyWishList.objects.filter(email=email)
    showlist = App_Profile.objects.none()
    for app_names in MyWishList.objects.filter(email=email):
        print(app_names.app_name)
        showlist |= App_Profile.objects.filter(app_name = app_names.app_name)
    return render(request,'wishlist.html',{'key':email,'showlist':showlist})
