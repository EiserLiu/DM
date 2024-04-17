from django.contrib import admin
from django.urls import path, include

from action import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("action/accessrecord/<int:id>/", views.AccessRecordView.as_view()),
]
