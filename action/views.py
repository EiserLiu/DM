from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, mixins, GenericViewSet, ModelViewSet

from old.models import Users, Buildings
from .models import Abnormal, AccessRecord
from .serializers import AbnormalSerializer, AccessRecordSerializer

# class AbnormalView(mixins.CreateModelMixin, GenericViewSet):
#     serializer_class = AbnormalSerializer
#     queryset = Abnormal.objects.all()


# class AccessRecordView(APIView):

# def get(self, request, *args, **kwargs):
#     id = kwargs.get('buildingid')
#     records = []
#     actions = AccessRecord.objects.filter(buildingid=id)
#     # print(actions)
#     for action in actions:
#         record = {}
#         record['user'] = action.userid.name
#         record['building'] = action.buildingid.name
#         record['createdat'] = action.createdat
#         record['status'] = action.status
#         records.append(record)
#     return Response({'code':201})

# def post(self, request):
#     userId = request.data.get('userId')
#     buildingId = request.data.get('buildingId')
#     status = request.data.get('status')
#     user = Users.objects.get(account=userId)
#     building = Buildings.objects.get(id=buildingId)
#     try:
#         AccessRecord.objects.create(userid=user, buildingid=building, status=status)
#     except AccessRecord.DoesNotExist:
#         return Response({"massage": "User or Building does not exist", "code": 404},
#                         status=status.HTTP_404_NOT_FOUND)
#     except:
#         return Response({"massage": "An error occurred", "code": 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     return Response({'code': 201})
