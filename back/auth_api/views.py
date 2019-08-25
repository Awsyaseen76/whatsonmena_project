from rest_framework import generics
from .models import Auth
# import operator
from .serializers import AuthSerializer
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt





# class MultipleFieldLookupMixin(object):
#    """
#    Apply this mixin to any view or viewset to get multiple field filtering
#    based on a `lookup_fields` attribute, instead of the default single field filtering.
#    """

#    def get_object(self):
#       queryset = self.get_queryset()             # Get the base queryset
#       queryset = self.filter_queryset(queryset)  # Apply any filter backends
#       filter = {}
#       for field in self.lookup_fields:
#          if self.kwargs[field]:  # Ignore empty fields.
#                filter[field] = self.kwargs[field]
#       #   self.check_object_permissions(self.request, obj)
#       auth = reduce(operator.or_, (Auth(x) for x in filter.items()))
#       return get_object_or_404(queryset, auth)  # Lookup the object
      





class AuthList(generics.ListCreateAPIView):  # Its ready template
   queryset = Auth.objects.all()
   serializer_class = AuthSerializer


# the power of generics is the templates
# RetrieveAPIView -> allow just view one record
# RetrieveUpdateDestroyAPIView -> view update delete

class AuthDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Auth.objects.all()
   serializer_class = AuthSerializer
   # lookup_fields = ['email']


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
