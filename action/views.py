from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, mixins, GenericViewSet, ModelViewSet

from old.models import Users, Buildings, Admins
from .models import Abnormal, AccessRecord
from .serializers import AbnormalSerializer, AccessRecordSerializer


class AbnormalView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = AbnormalSerializer
    queryset = Abnormal.objects.all()


class AccessRecordAddView(GenericViewSet):
    serializer_class = AccessRecordSerializer
    queryset = AccessRecord.objects.all()

    def post(self, request):
        status = request.data.get('status')
        serializer = self.get_serializer(data=request.data)
        # print(userId, buildingId, status)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except AccessRecord.DoesNotExist:
            return Response({"massage": "User or Building does not exist", "code": 404},
                            status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"massage": "An error occurred", "code": 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'code': 201})


class AccessRecordView(GenericViewSet):
    serializer_class = AccessRecordSerializer
    queryset = AccessRecord.objects.all()

    def get(self, request, *args, **kwargs):
        building_id = kwargs["buildingid"]
        return Response({'code': 201, 'bid': building_id})
