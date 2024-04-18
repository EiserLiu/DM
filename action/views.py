from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, mixins, GenericViewSet

from old.models import Users, Buildings
from .models import Abnormal, AccessRecord
from .serializers import AbnormalSerializer, AccessRecordSerializer


# class AbnormalView(mixins.CreateModelMixin, GenericViewSet):
#     serializer_class = AbnormalSerializer
#     queryset = Abnormal.objects.all()


class AccessRecordView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('buildingid')
        records = []
        actions = AccessRecord.objects.filter(buildingid=id)
        for action in actions:
            record = {}
            record['user'] = action.userid.name
            record['building'] = action.buildingid.name
            record['createdat'] = action.createdat
            record['status'] = action.status
            records.append(record)
        return render(request, 'card.html', {'records': records, 'buildingid': id})

    # def post(self, request):
    #     userId = request.data.get('userId')
    #     buildingId = request.data.get('buildingId')
    #     status = request.data.get('status')
    #     user = Users.objects.get(account=userId)
    #     building = Buildings.objects.get(id=buildingId)
    #     AccessRecord.objects.create(userid=user, buildingid=building, status=status)
    #     return Response({'code': 201})
