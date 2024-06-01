import datetime
import os

from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import mixins, GenericViewSet

from DM.settings import MEDIA_ROOT
from old.models import Users, Evaluates
from old.serializers import EvaluatesSerializer
from .models import Abnormal, AccessRecord
from .serializers import AbnormalSerializer, AccessRecordSerializer


class AbnormalView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = AbnormalSerializer
    queryset = Abnormal.objects.all()


class AccessRecordAddView(GenericViewSet):
    serializer_class = AccessRecordSerializer
    queryset = AccessRecord.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
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
        today_in = self.get_queryset().filter(buildingid=building_id, status=0,
                                              createdat__gt=datetime.date.today()).count()
        today_out = self.get_queryset().filter(buildingid=building_id, status=1,
                                               createdat__gt=datetime.date.today()).count()
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=3)

        # 获取过去三天内有进入记录的所有独立个体（例如用户ID）
        active_individuals_in = self.get_queryset().filter(
            buildingid=building_id,
            status=0,  # 假设 status=0 表示进入
            createdat__gt=cutoff_date
        ).values_list('userid', flat=True).distinct()

        # 获取过去三天内有离开记录的所有独立个体（例如用户ID）
        active_individuals_out = self.get_queryset().filter(
            buildingid=building_id,
            status=1,  # 假设 status=1 表示离开
            createdat__gt=cutoff_date
        ).values_list('userid', flat=True).distinct()

        # 获取所有个体的总数
        All_User = Users.objects.filter(roomid__buildingid=building_id).count()

        # 计算在过去三天内没有进入记录的人数
        inactive_individuals_in = All_User - active_individuals_in.count()

        # 计算在过去三天内没有离开记录的人数
        inactive_individuals_out = All_User - active_individuals_out.count()

        # 宿舍评分
        rating = Evaluates.objects.filter(roomid__buildingid=building_id, createdat__gt=datetime.date.today())
        ratingser = EvaluatesSerializer(instance=rating, many=True)
        print(rating)
        return Response({
            'code': 200,  # 通常 GET 请求成功时使用 200 状态码
            'bid': building_id,
            # 'in': today_in,
            # 'out': today_out,
            'long_time_no_in': inactive_individuals_in,
            'long_time_no_out': inactive_individuals_out,
            'rating': ratingser.data
        })


class FileView(APIView):
    def get(self, request, name):
        path = MEDIA_ROOT / name
        if os.path.isfile(path):
            return FileResponse(open(path, 'rb'))
        return Response({'error': '文件不存在'}, status=status.HTTP_404_NOT_FOUND)
