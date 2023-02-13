from django.urls import include, re_path
from app1 import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^patch$',views.patchesApi),
    re_path(r'^load_patch$',views.loadPatchesApi),
    # re_path(r'^patch/([0-9]+)$',views.patchesApi),



    # re_path(r'^employee$',views.employeeApi),
    # re_path(r'^employee/([0-9]+)$',views.employeeApi),

    # re_path(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)