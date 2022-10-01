from __future__ import print_function
from asyncio.windows_events import NULL
from http.client import HTTPResponse
from django.shortcuts import render
from email.message import EmailMessage
import random
import smtplib, ssl
from django.http import HttpResponse


import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import OffersCarousel, OrderDetails,Stores,Account,StoreMenu,Orders
# Create your views here.

def index(request):
   Offer_images = OffersCarousel.objects.all()
   noOfStores = Stores.objects.count() 
   stores = Stores.objects.all() 
   print(Offer_images)
   print(noOfStores)
   context={}
   context["no"]=noOfStores
   context["Stores"] = stores
   context["Offer_images"]= Offer_images

   if request.session.get("signedin"):
      context["signedAccount"]=request.session["signedAccount"]
      return render(request,"website/home.html", context)
   return render(request,"website/index.html", context)
      


def loginpage(request):
   context={}
   Acc = Account.objects.all()[0]
   if request.method == "POST":
      user = request.POST.get("email",False)
      Pass = request.POST.get("pass",False)
      try:
         Acc = Account.objects.filter(username=user)[0]
         context["wrong"]=False
      except:
         print ('incorrect password')
         context["wrong"]=True


      if(Acc.password == Pass and context["wrong"]==False):
         request.session['signedAccount'] = Acc.username
         request.session['signedin'] = True
         context['signedAccount'] = Acc.username

         Offer_images = OffersCarousel.objects.all()
         noOfStores = Stores.objects.count() 
         stores = Stores.objects.all() 
         print(Offer_images)
         print(noOfStores)
         context={}
         context["no"]=noOfStores
         context["Stores"] = stores
         context["Offer_images"]= Offer_images
         return render(request,"website/home.html",context)
      print("Wrong password")  
   if request.session.get('signedin'):
      context["signedAccount"]=request.sessions["signedAccount"]
   return render(request,"website/login.html",context)


def signuppage(request):
   context = {}
   if request.method == "POST":
      name = request.POST.get("name")
      Password = request.POST.get("pass")
      phoneno = request.POST.get("phoneno")
      collegemail = request.POST.get("email")
      block = request.POST.get("blk")
      roomno = request.POST.get("roomno")
   
      accountclass = Account(
         username = name,
         password = Password,
         Block = block,
         roomNo = roomno,
         email = collegemail,
         phoneNo = phoneno
      )
      accountclass.save()


      Offer_images = OffersCarousel.objects.all()
      noOfStores = Stores.objects.count() 
      stores = Stores.objects.all() 
      print(Offer_images)
      print(noOfStores)
      context={}
      context["signedAccount"] = name
      context["no"]=noOfStores
      context["Stores"] = stores
      context["Offer_images"]= Offer_images
      return render(request,"website/home.html",context)

   return render(request,"website/signup.html",context)

def signoutpage(request):
   context = {}
   request.session['signedin'] = False
   del request.session['signedAccount']
   return render(request,"website/index.html",context)

   #latest

def menupage(request):
   menudetails = StoreMenu.objects.all()
   
   context={"menudetails":menudetails}
   return render(request,"website/enzo.html",context)   

def yourorderspage(request):
   context={}
   OrderDetailsclass = OrderDetails(
      item = "Chicken Briyani",
      quantity = 1,
      priceForEach = 200,
   )

   OrderDetailsclass.save()

   ordersclass = Orders(
      status = 'p',
      Restaurant = "enzo",
      received = "false",
   )
   ordersclass.save()

   return render(request,"website/yourorder.html",context)   


def agentOrderView(request):
   context={}
   return render(request,"website/agentorderview.html",context)


def agentotp(request):
   print("reading otp")


   acc = Account.objects.all()[0]
   receiver_email = acc.email  # Enter receiver address

#send in blue
   configuration = sib_api_v3_sdk.Configuration()
   configuration.api_key['api-key'] = "KEY HIDDEN"


   api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

   otp = random.randint(100000, 999999)

   request.session["otp"]=otp
   request.session["otprequested"]=True

   subject = "OTP for Order verification: "+ str(otp)
   sender = {"name":"District120","email":"d120awards@gmail.com"}
   replyTo = {"name":"District120","email":"d120awards@gmail.com"}
   html_content = """
   <!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Document</title>
</head>
<body>
   your OTP is on the subject
</body>
</html>
"""


   to = [{"email":receiver_email,"name":"DevJams'22"}]
   params = {}
   send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=replyTo, html_content=html_content, sender=sender, subject=subject)

   try:
      api_response = api_instance.send_transac_email(send_smtp_email)
      print(api_response)
   except ApiException as e:
      print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
      


   return render(request,"website/agentotp.html")   


def agentotpsuccess(request):
   if request.session['otprequested']:
      otp=request.session['otp']
      if otp == request.POST.get("otpfield"): 
         return render(request,"website/successotp.html")
   return render(request,"website/successotp.html")


   