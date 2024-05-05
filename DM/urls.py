from django.contrib import admin
from django.urls import path, include

from action import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("action/accessrecord/<int:buildingid>/", views.AccessRecordView.as_view()),
    # path("accessrecord/", views.AccessRecordView.as_view({'post': 'post'}))
    # path("", )
]
