from django.contrib import admin
from django.urls import path, include, re_path

from action.views import FileView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/action/", include("action.urls")),
    path("api/old/", include("old.urls")),
    re_path(r'file/(.+?)/', FileView.as_view()),
]
