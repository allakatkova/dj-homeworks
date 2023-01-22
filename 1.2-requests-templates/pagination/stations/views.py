from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator
import csv
import urllib.parse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    file_csv = 'data-398-2018-08-30.csv'

    list_bus_stations = read_data_file(file_csv)

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(list_bus_stations, 10)
    current_page = paginator.get_page(page_num)

    objects_on_page = current_page.object_list

    context = {
        'bus_stations': objects_on_page,
        'page': current_page,
    }

    return render(request, 'index.html', context)


def read_data_file(file_csv):
    list_bus_stations = []
    with open(file_csv, 'r', encoding='utf-8') as file:
        data_csv_file = csv.DictReader(file, delimiter=',')
        for row in data_csv_file:
            data_sampling = {
                "Name": row['Name'], "Street": row['Street'], "District": row['District']}
            list_bus_stations.append(data_sampling)
    return list_bus_stations
