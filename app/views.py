from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def gellery(request):
    return render(request,'gallery.html')

def mywork(request):
    return render(request,'myworks.html')

def price(request):
    return render(request,'price.html')

