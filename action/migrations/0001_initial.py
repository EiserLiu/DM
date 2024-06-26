# Generated by Django 4.2 on 2024-04-11 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("old", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(choices=[(0, "出"), (1, "入")], default=1),
                ),
                (
                    "createdat",
                    models.DateTimeField(auto_now_add=True, db_column="createdAt"),
                ),
                (
                    "updatedat",
                    models.DateTimeField(auto_now=True, db_column="updatedAt"),
                ),
                (
                    "deletedat",
                    models.DateTimeField(blank=True, db_column="deletedAt", null=True),
                ),
                (
                    "buildingid",
                    models.ForeignKey(
                        blank=True,
                        db_column="buildingId",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="old.buildings",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        blank=True,
                        db_column="userId",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="old.users",
                    ),
                ),
            ],
            options={
                "verbose_name": "出入记录",
                "verbose_name_plural": "出入记录",
                "db_table": "accessrecord",
            },
        ),
        migrations.CreateModel(
            name="Abnormal",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "createdat",
                    models.DateTimeField(auto_now_add=True, db_column="createdAt"),
                ),
                (
                    "updatedat",
                    models.DateTimeField(auto_now=True, db_column="updatedAt"),
                ),
                (
                    "deletedat",
                    models.DateTimeField(blank=True, db_column="deletedAt", null=True),
                ),
                (
                    "floorid",
                    models.ForeignKey(
                        blank=True,
                        db_column="floorId",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="old.floors",
                    ),
                ),
            ],
            options={
                "verbose_name": "异常行为",
                "verbose_name_plural": "异常行为",
                "db_table": "abnormal",
            },
        ),
    ]
