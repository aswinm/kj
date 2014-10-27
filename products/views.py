from django.shortcuts import render
from products.models import Company,Product,ItemType

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html') 

def contacts(request):
    return render(request,'contacts.html')

def product(request,ptype):
    it_list = ItemType.objects.all()
    ittype = ItemType.objects.filter(url=ptype)
    if not ittype:
        return render(request,"404.html")
    c = Company.objects.all()
    prod_list = {}
    for i in c:
        it = Product.objects.filter(company = c,itemtype=ittype)
        if it:
            prod_list[i.name] = it

    return render(request,"catalog.html",{"c_list":c,"prod_list":prod_list,"it_list":it_list})
    

# Create your views here.
