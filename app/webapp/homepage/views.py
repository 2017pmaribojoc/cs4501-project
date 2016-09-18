from django.utils.decorators import method_decorator

__author__ = 'Patrick'
from rest_framework import viewsets
# from django.contrib.auth.models import User, Group
from homepage.models import Baby, Daddy
from homepage.serializers import BabySerializer, DaddySerializer
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
import json



class BabyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class BabyList(generics.ListCreateAPIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage/index.html'
    model = Baby
    serializer_class = BabySerializer
    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        queryset = Baby.objects.all()
        profile = get_object_or_404(Baby, id=1)
        serializer = BabySerializer(profile)
        return Response({'babies': queryset, 'serializer': serializer} )

    #
    # def post(self, request, format=None):
    #     content = JSONRenderer().render(request.data)
    #     new_baby = Baby(id = request.data.id)
    #     new_baby.save()
    #     Baby.objects.create(content)
    #     queryset = Baby.objects.all()
    #     profile = get_object_or_404(Baby, request.data.id)
    #
    #     serializer = BabySerializer(profile)
    #
    #     return Response({'babies': queryset, 'serializer': serializer} )



@csrf_exempt
def baby_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        babies = Baby.objects.all()
        serializer = BabySerializer(babies, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        # print(request)
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)

        serializer = BabySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def baby_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        baby = Baby.objects.get(id=id)
        print(baby.first_name)
    except Baby.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BabySerializer(baby)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BabySerializer(baby, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        baby.delete()
        return HttpResponse(status=204)


@csrf_exempt
def daddy_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        daddies = Daddy.objects.all()
        serializer = DaddySerializer(daddies, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        # print(request)
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)

        # data = JSONParser().parse(request.body)
        # data = request.body

        serializer = DaddySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def daddy_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        daddy = Daddy.objects.get(id=id)
        print(daddy.first_name)
    except Daddy.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DaddySerializer(daddy)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request.data)
        serializer = DaddySerializer(daddy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        daddy.delete()
        return HttpResponse(status=204)