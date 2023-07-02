from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

# Create your views here.
from .models import *
from .serializers import *



def Blog_View(request):
    blogs = BLog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return JsonResponse(serializer.data, safe=False)


def BlogDetail_View(request, id):
    blog = get_object_or_404(BLog, id=id)
    serializer = BlogSerializer(blog)
    return JsonResponse(serializer.data, safe=False)