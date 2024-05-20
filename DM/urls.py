from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/action/", include("action.urls")),
    path("api/old/", include("old.urls"))
]
