"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from perpus.views import index, page, cari_buku, pendaftaran, detail_item, cetak
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    # path('daftar_buku', page)
    path('cari_buku', cari_buku, name='cari_buku'),
    path('pendaftaran', pendaftaran, name='pendaftaran'),
    path('item/<pk>', detail_item, name='detail_item'),
    path('cetak_laporan', cetak, name='cetak_laporan')
    # re_path(r'^.*\.*', pages, name='pages'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
