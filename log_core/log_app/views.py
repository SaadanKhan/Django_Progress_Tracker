from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models import User,Work_update,Groups
from django.utils import timezone

def home(request):
       return render(request,'home.html')
       
def student(request):
       if request.method == 'POST':
              task = request.POST['today_topic']
              course = request.POST['course']

              uname = request.session.get('name')
              name = User.user_name(name = uname)

              model = Work_update(
                            # id = request.session.get('ID'),
                            name=name,
                            today_work=task, 
                            your_course=course,
                            date = timezone.now()
                            )
              model.save()
              return HttpResponseRedirect('/student')

       return render(request,'student.html')

def team_lead(request):

       groups = Groups.objects.all()
       id_got = request.GET.get('group_id')
       
       if id_got:
              student_data = User.get_grp_by_id(id_got)
       else:
              student_data = User.objects.all()

       data = {'student_data':student_data, 'groups':groups}
       
       return render(request,'team_lead.html',data)

class signup(View):

       def get(self,request):
              return render(request,'signup.html')
       
       def post(self,request):
              name = request.POST.get('name')
              email = request.POST.get('email')
              phone = request.POST.get('phone')
              password = request.POST.get('password')
              Con_pass = request.POST.get('con_pass')
              
              values = {
                     'name':name,
                     'email':email,
              }

              if password == Con_pass:
                     password = make_password(password)
                     if len(password) <= 6:
                            error = "Password with minimum length of 6 allowed"
                            data = {
                            'error':error,
                            'value':values
                            }
                            return render(request, "signup.html",data)
                     else:
                            user = User(
                                          name=name,
                                          email=email,
                                          password=password,
                                          phone=phone
                                   )

                            if user.isExist():
                                   error = "**Email already exists"
                                   data = {
                                          'error':error,
                                          'value':values
                                          }
                                   return render(request, "signup.html",data)
                            else:
                                   user.save()

                                   return redirect('home')                                  
              else:
                     error = "Passwords must be same"
                     data = {
                            'error':error,
                            'value':values
                     }
                     return render(request, "signup.html",data)                     

class Login(View):

       def get(self, request):
              return render(request,'login.html')

       def post(self,request):
              
              email = request.POST.get('email')
              password = request.POST.get('password')
              
              user = User.get_email(email)
              error = None
              if user:
                     
                     flag = check_password(password , user.password)

                     if flag:
                            request.session['ID'] = user.id
                            request.session['name'] = user.name
                            request.session['email'] = user.email

                            role_of_user = user.role

                            if str(role_of_user) == "Member":
                                   return render(request, 'student.html')
                            elif str(role_of_user) == "Lead":
                                   return redirect('team_lead')
                            else:
                                   return HttpResponse('Your role is not assigned yet...')

                     else:
                            error = "**Enter the valid informations"
              
              else:
                     error = "**Password or email is invalid"

              return render(request, 'home.html', {'error':error})

def logout(request):
       request.session.clear()
       return redirect ('home')

def Role(request):
              
       id_with_name = request.GET.get('student_id')
       print(id_with_name)

       if id_with_name:
              name_list = Work_update.objects.filter(name__name = id_with_name)
              data = {
                     'name_list':name_list
                     }             
       else:
              return HttpResponse('ERROR...')
       return render(request, 'specific_student.html',data)

def SpecificRole(request):

       name_id = request.session.get('name')

       if name_id:
              name_list = Work_update.objects.filter(name__name = name_id)
              
              data = {
                     'name_list':name_list
                     }             
       else:
              return HttpResponse('ERROR...')
       return render(request, 'student.html',data)
