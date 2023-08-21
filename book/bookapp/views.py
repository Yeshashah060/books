from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from bookapp.models import books
# Create your views here.

def front(request):
	return render(request,'front.html')
def register(request):
	return render(request,'register.html')

def savedata(request):

	bname=request.GET.get('bname')

	bauthor=request.GET.get('bauthor')
	
	bprice=request.GET.get('bprice')
	
	p=books(bname=bname,bauthor=bauthor,bprice=bprice)
	p.save()

	# variable = modelname.objects.allvalues()
	# return render(request,htmlpage,{'variable':'object'})
	data = books.objects.all()
	return render(request,'details.html',{'data':data})

def details(request):
	data = books.objects.all()
	return render(request,'details.html',{'data':data})


def newbook(request):
	return render(request,'newbook.html')

