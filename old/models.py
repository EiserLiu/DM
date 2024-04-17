from django.db import models


class Abnormal(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    floor_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abnormal'


class Accessrecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    building_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accessrecord'


class Admins(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    buildingid = models.OneToOneField('Buildings', models.DO_NOTHING, db_column='buildingId',
                                      primary_key=True)  # Field name made lowercase. The composite primary key (buildingId, userId) found, that is not supported. The first column is selected.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admins'
        unique_together = (('buildingid', 'userid'),)


class Backrecords(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='roomId', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'backrecords'


class Buildings(models.Model):
    name = models.CharField(max_length=255, db_comment='楼宇名称')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buildings'


class Cleaners(models.Model):
    name = models.CharField(max_length=255, db_comment='保洁员姓名')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='保洁员电话')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    buildingid = models.ForeignKey(Buildings, models.DO_NOTHING, db_column='buildingId', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cleaners'


class Cleanrecords(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='roomId', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cleanrecords'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Evaluates(models.Model):
    score = models.IntegerField(db_comment='评价分数')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='评价备注')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='roomId', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evaluates'


class Faculties(models.Model):
    name = models.CharField(max_length=255, db_comment='院系名称')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculties'


class Floors(models.Model):
    layer = models.IntegerField(blank=True, null=True, db_comment='楼层')
    buildingid = models.ForeignKey(Buildings, models.DO_NOTHING, db_column='buildingId', blank=True,
                                   null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    cleanerid = models.ForeignKey(Cleaners, models.DO_NOTHING, db_column='cleanerId', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'floors'
        unique_together = (('layer', 'buildingid'),)


class Getuprecords(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='roomId', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'getuprecords'


class Majors(models.Model):
    name = models.CharField(max_length=255, db_comment='专业名称')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    facultyid = models.ForeignKey(Faculties, models.DO_NOTHING, db_column='facultyId', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'majors'


class Rooms(models.Model):
    number = models.IntegerField(blank=True, null=True, db_comment='房间号')
    buildingid = models.ForeignKey(Buildings, models.DO_NOTHING, db_column='buildingId', blank=True,
                                   null=True)  # Field name made lowercase.
    status = models.IntegerField(db_comment='宿舍状态，可入住为1，不可入住为2')
    peoplenum = models.IntegerField(db_column='peopleNum', db_comment='房间最大人数')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    floorid = models.ForeignKey(Floors, models.DO_NOTHING, db_column='floorId', blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rooms'
        unique_together = (('number', 'buildingid'),)


class Tokens(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tokens'


class Users(models.Model):
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True, db_comment='性别, 0：男, 1：女')
    checktime = models.DateTimeField(db_column='checkTime', blank=True, null=True,
                                     db_comment='入住宿舍时间')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey(Rooms, models.DO_NOTHING, db_column='roomId', blank=True,
                               null=True)  # Field name made lowercase.
    facultyid = models.ForeignKey(Faculties, models.DO_NOTHING, db_column='facultyId', blank=True,
                                  null=True)  # Field name made lowercase.
    majorid = models.ForeignKey(Majors, models.DO_NOTHING, db_column='majorId', blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('id', 'account'),)


class Visitors(models.Model):
    name = models.CharField(max_length=255, db_comment='访客姓名')
    phone = models.CharField(max_length=255, db_comment='访客电话')
    idnumber = models.CharField(db_column='idNumber', max_length=255,
                                db_comment='访客身份证号')  # Field name made lowercase.
    sex = models.IntegerField(db_comment='访客性别, 0：男, 1：女')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    buildingid = models.ForeignKey(Buildings, models.DO_NOTHING, db_column='buildingId', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitors'
