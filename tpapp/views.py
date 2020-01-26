# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from tpapp.serializers import TpAppSerializer
from tpapp.models import AppData


# Test class for filtering years
class ListRecordsByYearRange(ListAPIView):
    serializer_class = TpAppSerializer

    def get_queryset(self):
        queryset = AppData.objects.filter(year__gte=1990, year__lte=1992)
        return queryset


class ListRecordsByYearURL(ListAPIView):
    """
    get:
    Override get_queryset method to list all records in a year range
    """
    serializer_class = TpAppSerializer

    def get_queryset(self):
        start = self.kwargs['start']
        end = self.kwargs['end']
        queryset = AppData.objects.filter(year__gte=start, year__lte=end)
        return queryset


class ListRecordsByYearMonthURL(ListAPIView):
    """
    get:
    Override get_queryset method to list all records in a year range
    """
    serializer_class = TpAppSerializer

    def get_queryset(self):
        month = self.kwargs['month']
        start = self.kwargs['start']
        end = self.kwargs['end']
        queryset = AppData.objects.filter(year__gte=start, year__lte=end, month=month)
        return queryset



class ListCreateRecords(ListCreateAPIView):
    serializer_class = TpAppSerializer

    def get_queryset(self):
        # If no search string passed in url returns all posts in reverse chronological order by year only, not months
        if not self.request.query_params.get('search', None):
            return AppData.objects.order_by('year').reverse()

        # If string passed in url is <   search  >    : searches year field using search parameter
        query_param = self.request.query_params['search']
        queryset = AppData.objects.filter(Q(year=query_param))
        return queryset

        # If strings passed in url are <  start  > and <  end>   : filter records by range of years
        # year_start = self.request.query_params['start']
        #         # year_end = self.request.query_params['end']
        #         # queryset = AppData.objects.filter(year=year_start, year=year_end)
        #         # return queryset


class ListCreateRecordsMonth(ListCreateAPIView):
    serializer_class = TpAppSerializer

    def get_queryset(self):
        # If search string passed in url searches month field
        query_param = self.request.query_params['search']
        queryset = AppData.objects.filter(Q(month=query_param))
        return queryset

