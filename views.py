from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Marks,Student
from django.contrib.auth.models import User
#from .forms import degisterForm,Register
# Create your views here.
def basic_demo(request):
    students= Student.objects.all()
    return render(request,'basic.html',{'students':students})
def add(request):
     message=""
     if request.method=="POST":
       Student.objects.create(
        name=request.POST['name'],
        age=request.POST['age'],
        roll_no=request.POST['roll_no'],
        contact=request.POST['contact'],
        )
       name=request.POST['name']
       Marks.objects.create(
        student=Student.objects.get(name=name),
        Telugu=request.POST['telugu'],
        Hindi=request.POST['hindi'],
        English=request.POST['english'],
        Science=request.POST['science'],
        )
       message="Student Added Successfully"
     return render(request,'add.html',{'message':message})
def update(request):
     message=""
     search_term=request.GET.get('search_term')
     student = Student.objects.get(roll_no=search_term)
     marks = Marks.objects.get(student=student)
     if request.method=="POST":
        student.name=request.POST['name']
        student.age=request.POST['age']
        student.contact=request.POST['contact']
        student.save()
        marks.Telugu=request.POST['telugu']
        marks.Hindi=request.POST['hindi']
        marks.English=request.POST['english']
        marks.Science=request.POST['science']
        marks.save()
        message="Student Updated Successfully"
     return render(request,'update.html',{'message':message,'marks':marks,'student':student})        
def form(request):       

       return render(request,'form.html')







































































































































"""
def student_form(request):
   message=""
   if request.method=="POST":
      Student.objects.create(
      name=request.POST['name'],
      roll_no=request.POST['roll'],
      age=request.POST['age'],
      contact=request.POST['contact'],
      )
      message="Student Added Successfully"  
   return render(request,'student_form.html',{'message':message})

def student_list(request):
   students=Student.objects.all()
   return render(request,'student_folist.html',{'students':students})
def student_update(request,roll_no):
   student=Student.objects.get(roll_no=roll_no)
   if request.method=="POST":   
     student.name=request.POST['name']
     student.roll_no=request.POST['roll']
     student.age=request.POST['age']
     student.contact=request.POST['contact']
     student.save()
     return redirect('student_list')
   return render(request,'update.html',{'student':student})
def student_delete(request,roll_no):
    student=Student.objects.get(roll_no=roll_no)
    student.delete()
    return redirect('student_list')
def create_post(request):
   if request.method=='POST':
     form=degisterForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect("/new/")
   else :
      form=degisterForm()
   return render(request,"create_post.html",{'form':form})
def new(request):
    lots=New.objects.all()
    return render(request,"new_one.html",{'lots':lots})
def Register_one(request):
    if request.method=='POST':
      form=Register(request.POST)
      if form.is_valid():
         username=form.cleaned_data['username']
         email=form.cleaned_data['email']
         password=form.cleaned_data['password']
         confirm_password=form.cleaned_data['confirm_password']
         date=form.cleaned_data['date']
         User.objects.create_user(username=username,email=email,password=password)
         return render(request,'success.html',{'username':username})
    else :
       form=Register()
    return render(request,'register.html',{'form':form})  

def jam(request):
    return HttpResponse("Hi,I am ZUBAIR")
def home(request):
     return render(request,'home.html')
def start(request):
     return render(request,'base.html')
def end(request):
     return render(request,'base1.html')
def post_list(request):
    posts=first.objects.all()   
    return render(request,"post_list.html",{'posts': posts})
def onetoone(request):
    user=User.objects.select_related('Profile').all()
#    profile=Profile.objects.filter(user=user).first()
    return render(request,'one_to_one.html',{'user':user,'profile':profile})
def onetomany(request):
   blog=Blog.objects.first()
   comments=blog.comments_set.all()if blog else []
   return render(request,'one_to_many.html',{'blog':blog,'comments':comments})
def many_to_many(request):
   student=Students.objects.first()
   courses=student.courses.all()
   return render(request,'many_to_many.html',{'student':student,'courses':courses})
"""
