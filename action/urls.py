from django.urls import path

from . import views

urlpatterns = [
    path("abnormal/", views.AbnormalView.as_view({
        "post": "create",
    })),

    path("accessrecord/", views.AccessRecordView.as_view()),

]
