from django.urls import path

from . import views

urlpatterns = [
    path("accessrecord/<int:buildingid>/", views.AccessRecordView.as_view({
        'get': 'get'
    })),
    path("accessrecord/", views.AccessRecordAddView.as_view({
        'post': 'post'
    })),
]
