from django.views.decorators.csrf import csrf_protect

#@csrf_protect
from django.http import HttpResponse 
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib.auth.models import User,auth
from .models import Employee

# Create your views here.
def index(request):



        
	return render(request,'index.html')

def registration(request):
    return render(request,'registration.html')


def login(request):
        if request.method=='POST':
                username=request.POST['name']
                password=request.POST['password']
                
                all_record=Employee.objects.all()
                print(username,password)
                print(all_record[0].password)
                print(username in all_record)
                print(type(all_record))
                print(len(all_record))
                for i in range(len(all_record)):
                        text="0"
                        print(all_record[i].empname,all_record[i].password)
                           
                        if(all_record[i].empname==username and all_record[i].password==password):
                                if(all_record[i].usertype=="superuser"):
                                        text="4"                            
                                        return render(request,'superUser_dash.html',{'all_data':all_record,'message':text})

                                else:
                                        text="Welcome "+username
                                        return render(request,'dashboard.html',{'data':all_record[i],'message':text})
                               
                text="1"
                              #  print(i.empname,i.password)
                return render(request,'index.html',{'message':text})

        else:
                return render(request,'index.html')


def addData(request):
        print("Adding the data..")
        name=request.POST["fname"]
        age=request.POST["age"]
        gender=request.POST["gender"]
        qualification=request.POST["qualification"]
        address=request.POST["address"]
        pincode=request.POST["pin"]
        employment=request.POST["employment"]
        password=request.POST["password"]
        print(name,age,gender,qualification,address,pincode
          ,employment,password)
        savedata=Employee(empname=name,age=age,gender=gender,
                           qualification=qualification,
                           address=address,
                           pincode=pincode,
                           employment=employment,
                           password=password,usertype="normal"
                           )
        savedata.save()
        print("Added Sucessfully.")
    
        
        return render(request,'index.html',{'message':"2"})


        
def update(request):
        name=str(request.POST["fname"])#,False)
        age=request.POST["age"]
        gender=request.POST["gender"]
        qualification=request.POST["qualification"]
        address=request.POST["address"]
        pincode=request.POST["pin"]
        employment=request.POST["employment"]
        print(name)

        print(len(name))
        
        #a=Employee.objects.raw('SELECT * from homePage_employee where empname = %s',[name])
        try:
                a=Employee.objects.get(empname=name)
        #a=Employee.objects.filter(empname = empname).first()
        
                print(a.age)
                a.age=age
                a.gender=gender
                a.qualification=qualification
                a.address=address
                a.pincode=pincode
                a.employment=employment
                a.save()
                print("updated Successfully")
                return render(request,'dashboard.html',{'data':a,'message':"Updated Sucessfully"})
        except:
                print("error occured !")
                return render(request,'dashboard.html')
                

def filter(request):
        try:
                
                        
                basis=request.POST["filter_option"]
                print(basis)
                if basis=="Male" or basis=="Female":
                        all_record=Employee.objects.filter(gender=basis)
                      

                elif basis=="Age":
                         all_record=Employee.objects.all().order_by("age")
                       
                        
                
                        
                return render(request,'superUser_dash.html',{'all_data':all_record})
        except:
                
                print("error occured !")
                return render(request,'superUser_dash.html')
                

        
                               
        
        
	
