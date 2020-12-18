from django.shortcuts import render,get_object_or_404
from djang.http import JsonResponse
from .models import Poll
# Create your views here.


def polls_list(request):
	max_objects=20
	polls=Poll.objects.all()[:max_objects]
	data={"result":list(polls.values("question","created_by__username","pub_date"))}
	return JsonResponse(data)
	




def polls_detail(request,pk):
	pass