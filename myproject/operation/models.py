# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Event(models.Model):
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    uid = models.TextField(db_column='UID', primary_key=True, blank=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    descriptionfilterhtml = models.TextField(db_column='descriptionFilterHtml', blank=True, null=True)  # Field name made lowercase.
    discountinfo = models.TextField(db_column='discountInfo', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='imageURL', blank=True, null=True)  # Field name made lowercase.
    websales = models.TextField(db_column='webSales', blank=True, null=True)  # Field name made lowercase.
    sourcewebpromote = models.TextField(db_column='sourceWebPromote', blank=True, null=True)  # Field name made lowercase.
    sourcewebname = models.TextField(db_column='sourceWebName', blank=True, null=True)  # Field name made lowercase.
    hitrate = models.IntegerField(db_column='hitRate', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    editmodifydate = models.TextField(db_column='editModifyDate', blank=True, null=True)  # Field name made lowercase.
    startdate = models.TextField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.TextField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event'


class Showinfo(models.Model):
    show_id = models.AutoField(primary_key=True, blank=True)
    event_uid = models.ForeignKey(Event,on_delete=models.CASCADE, db_column='event_uid', blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    onsales = models.TextField(db_column='onSales', blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(blank=True, null=True)
    locationname = models.TextField(db_column='locationName', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    endtime = models.TextField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShowInfo'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True, blank=True)
    event_uid = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_uid', blank=True, null=True)
    unit_type = models.TextField(blank=True, null=True)
    unit_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Unit'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
