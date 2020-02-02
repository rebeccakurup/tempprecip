from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from django.urls import path, include

from tpapp.views import ListCreateRecords, ListCreateRecordsMonth, ListRecordsByYearRange, ListRecordsByYearURL, \
    ListRecordsByYearMonthURL

urlpatterns = [
    path('api/admin/', admin.site.urls),

    path('vue/', TemplateView.as_view(template_name='index.html')),

    path('api/', include('rest_framework.urls')),
    path('api/docs/', include_docs_urls(title='TempPrecip', public=False)),


    # Returns all records in chronological order
    # Creates new record if user is logged in with POST method:
    # If user passes search string (i.e. api/?search=<str:search_string> ) returns search results of year field
    path('api/year/', ListCreateRecords.as_view()),

    path('api/year/<int:start>/<int:end>/', ListRecordsByYearURL.as_view()),

    path('api/month/<int:month>/<int:start>/<int:end>/', ListRecordsByYearMonthURL.as_view()),

    # If user passes search string (i.e. api/month/?search=<str:search_string> ) returns search results of month field
    path('api/month/', ListCreateRecordsMonth.as_view()),

    # Test class endpoint
    path('api/year/range/', ListRecordsByYearRange.as_view())

]
