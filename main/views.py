# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import quoteForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def index(request):

	qs= Post.objects.all().order_by('-id')
	

	query=request.GET.get('q')
	if query:
		#print(query)

		#qs=qs.filter(body__icontains=query)
		#print(qs)

		qs = qs.filter(
				Q(title__icontains=query)|
				Q(body__icontains=query)|
				Q(author__icontains=query) 
				).distinct()
	paginator = Paginator(qs, 5) # Show 5 contacts per page
	page = request.GET.get('page')
	try:
		qs=paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)
	#print(qs)

	return render(request,'index.html',{'qs':qs})






def addQuote(request):
	form = quoteForm(request.POST or None)
	context={'form':form}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context ={'form':form}
		
	return render(request,'addQuote.html',context)
	

def viewQuote(request,id=None):
	qs = get_object_or_404(Post, id=id)
	context={'qs':qs}
	return render(request,'viewQuote.html',{'qs':qs})


def editQuote(request,id=None):
	instance= get_object_or_404(Post, id=id)
	form = quoteForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
			#"title": qs.title,
			"instance": instance,
			"form":form,
		}	
	return render(request,'addQuote.html',context)
		


def deleteQuote(request,id=None):
	qs= get_object_or_404(Post,id=id)
	qs.delete()
	return HttpResponseRedirect('/')





	