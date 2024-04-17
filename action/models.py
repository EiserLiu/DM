from django.db import models


class AccessRecord(models.Model):
    userid = models.ForeignKey('old.Users', db_column='userId', on_delete=models.SET_NULL, blank=True, null=True)
    buildingid = models.ForeignKey('old.Buildings', db_column='buildingId', on_delete=models.DO_NOTHING, blank=True,
                                   null=True)
    status = models.BooleanField(choices=((0, '出'), (1, '入')), default=1)
    createdat = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updatedat = models.DateTimeField(auto_now=True, db_column='updatedAt')
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)

    class Meta:
        db_table = 'accessrecord'
        verbose_name = '出入记录'
        verbose_name_plural = verbose_name


# 异常行为表
class Abnormal(models.Model):
    floorid = models.ForeignKey('old.Floors', db_column='floorId', on_delete=models.DO_NOTHING, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updatedat = models.DateTimeField(auto_now=True, db_column='updatedAt')
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)

    class Meta:
        db_table = 'abnormal'
        verbose_name = '异常行为'
        verbose_name_plural = verbose_name
