from django.shortcuts import render

from .models import OffersCarousel,Stores
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

   return render(request,"website/index.html", context)

def loginpage(request):
   context={}
   if request.method == "POST":
      username = request.POST.get("username",False)
      password = request.POST.get("username",False)
      return render(request,"website/home.html",context)
   return render(request,"website/login.html",context)