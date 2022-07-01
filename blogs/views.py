from django.shortcuts import render
from .models import room
from .models import project
# Create your views here.
from .forms import roomform,mailform
#for email
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def index(request):
	p=project.objects.all()
	d=room.objects.all()
	d=d[::-1]
	d=d[:4:]
	return render(request,'index.html',{'pro':p,'dest':d})

def blog(request):
	d=room.objects.all()
	form=mailform()
	if request.method=="POST":
		form=mailform(request.POST)
		if form.is_valid():
			form.save()
		else:
			print(form.errors.as_data())
	return render(request,'blog.html',{'dest':d,'form':form})

def feed(request):
	form=roomform()
	if request.method=="POST":
		form=roomform(request.POST)
		if form.is_valid():
			form.save()
			send_mail('Hii','New post is here','vrblogs.v2@gmail.com',['vishnuk55265@gmail.com'],fail_silently=False)
		else:
			print(form.errors.as_data())
	context={'form':form}
	return render(request,'feed.html',context)
	


