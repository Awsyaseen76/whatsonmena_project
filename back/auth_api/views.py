# from rest_framework import generics
# import operator
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

from .models import Auth
from .serializers import AuthSerializer


@csrf_exempt
def auth_list(request):
    if request.method == 'GET':
        auths = Auth.objects.all()
        auths_serializer = AuthSerializer(auths, many=True)
        return JsonResponse(auths_serializer.data, safe=False)


@csrf_exempt
def create_auth(request):
    if request.method == 'POST':
        auth_data = JSONParser().parse(request)
        auth_serializer = AuthSerializer(data=auth_data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return JsonResponse(auth_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def auth_detail(request, pk):
    try:
        auth = Auth.objects.get(pk=pk)
    except Auth.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        auth_serializer = AuthSerializer(auth)
        return JsonResponse(auth_serializer.data)

    elif request.method == 'PUT':
        auth_data = JSONParser().parse(request)
        auth_serializer = AuthSerializer(auth, data=auth_data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return JsonResponse(auth_serializer.data)
        return JsonResponse(auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auth.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# class AuthList(generics.ListCreateAPIView):  # Its ready template
#    queryset = Auth.objects.all()
#    serializer_class = AuthSerializer


# the power of generics is the templates
# RetrieveAPIView -> allow just view one record
# RetrieveUpdateDestroyAPIView -> view update delete

# class AuthDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Auth.objects.all()
#     serializer_class = AuthSerializer
#     # lookup_fields = ['email']


@csrf_exempt
def login(request):
    print('reached ******************')
    auth = JSONParser().parse(request)
    print('the type is : ', type(auth))
    print('request is: ', auth['email'])
    email = auth['email']
    password = auth['password']
    try:
        found_auth = Auth.objects.get(email=email, password=password)
        print('found auth: ', found_auth)
        print('serialized found_auth: ', AuthSerializer(found_auth, many=False))
    except Auth.DoesNotExist:
        print('Not found :( ')
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serialized_auth = AuthSerializer(found_auth, many=False)
        return JsonResponse(serialized_auth.data, safe=False)
