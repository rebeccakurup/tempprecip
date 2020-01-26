"""tpdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tpapp.views import ListCreateRecords, ListCreateRecordsMonth, ListRecordsByYearRange, ListRecordsByYearURL

urlpatterns = [
    path('api/admin/', admin.site.urls),

    path('vue/', TemplateView.as_view(template_name='index.html')),

    path('api/', include('rest_framework.urls')),
    path('api/docs/', include_docs_urls(title='TempPrecip', public=False)),

    # path("",
    #      TemplateView.as_view(template_name="application.html"),
    #      name="app",
    #      ),

    # Returns all records in reverse chronological order (newest to oldest)
    # Creates new record if user is logged in with POST method:
    # If user passes search string (i.e. api/?search=<str:search_string> ) returns search results of year field
    path('api/year/', ListCreateRecords.as_view()),

    path('api/year/<int:start>/<int:end>/', ListRecordsByYearURL.as_view()),

    # If user passes search string (i.e. api/month/?search=<str:search_string> ) returns search results of month field
    path('api/month/', ListCreateRecordsMonth.as_view()),

    path('api/year/range/', ListRecordsByYearRange.as_view())

]
