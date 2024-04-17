from .models import *
from rest_framework import serializers


class AbnormalSerializer(serializers.ModelSerializer):
    # 异常行为序列化器
    class Meta:
        model = Abnormal
        fields = '__all__'


class AccessRecordSerializer(serializers.ModelSerializer):
    # 人员出入序列化器
    class Meta:
        model = AccessRecord
        fields = '__all__'
