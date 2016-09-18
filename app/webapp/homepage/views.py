from django.utils.decorators import method_decorator

__author__ = 'Patrick'
from rest_framework import viewsets
# from django.contrib.auth.models import User, Group
from homepage.models import User
from homepage.serializers import UserSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class UserList(generics.ListCreateAPIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage/index.html'
    model = User
    serializer_class = UserSerializer
    @method_decorator(csrf_exempt)
    def get(self, request):
        queryset = User.objects.all()
        profile = get_object_or_404(User, id=1)
        serializer = UserSerializer(profile)
        return Response({'users': queryset, 'serializer': serializer} )

    #
    # def post(self, request):
    #     content = JSONRenderer().render(request.data)
    #     new_user = User(id = request.data.id)
    #     new_user.save()
    #     User.objects.create(content)
    #     queryset = User.objects.all()
    #     profile = get_object_or_404(User, request.data.id)
    #
    #     serializer = UserSerializer(profile)
    #
    #     return Response({'users': queryset, 'serializer': serializer} )

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        # print(request)
        # data = JSONParser().parse(request)
        data =   {

              "first_name": "New",
              "last_name": "User",
              "id": 6

          }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(id=id)
        print(user.first_name)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)