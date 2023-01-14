import csv
from typing import NamedTuple, List, Any, Tuple
from django.shortcuts import render
from . import models, utils


def index(request):
    context = {}
    profession = models.Profession.objects.filter(id=1).all()[0]
    context['profession'] = profession
    return render(request, 'profession.html', context=context)


def get_csv_data(file_path) -> List[List[Any]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        csv_data = csv.reader(f, delimiter=',')
        return [i for i in csv_data]


class Table(NamedTuple):
    head: List[Any]
    body: List[Any]


class Item(NamedTuple):
    title: str
    table: Table
    img: str


def relevance(request):
    context = {'title': 'Востребованность'}
    item = models.RelevancePage.objects.filter(id=1).all()[0]
    elements = models.Element.objects.filter(relevance_id=item.id).all()
    data_for_context = []
    for element in elements:
        table: List[List[str]] = get_csv_data(element.csv_file.path)
        data_for_context.append(Item(element.title, Table(head=table.pop(0), body=table), element.img_file))
    context['data'] = data_for_context
    return render(request, 'detail.html', context=context)


def geo(request):
    context = {}
    item = models.GeoPage.objects.filter(id=3).all()[0]
    elements = models.Element.objects.filter(geo_id=item.id).all()
    data_for_context = []
    for element in elements:
        table: List[List[str]] = get_csv_data(element.csv_file.path)
        data_for_context.append(Item(element.title, Table(head=table.pop(0), body=table), element.img_file))
    context['data'] = data_for_context
    return render(request, 'detail.html', context=context)


def skills(request):
    context = {}
    item = models.SkillPage.objects.filter(id=1).all()[0]
    elements = models.Element.objects.filter(skill_id=item.id).all()
    data_for_context = []
    for element in elements:
        table: List[List[str]] = get_csv_data(element.csv_file.path)
        data_for_context.append(Item(element.title, Table(head=table.pop(0), body=table), element.img_file))
    context['data'] = data_for_context
    return render(request, 'detail.html', context=context)


def last_vacancies(request):
    context = {}
    item = models.Profession.objects.filter(id=1).all()[0]
    vacancies = utils.get_vacancies(item.title)
    context['vacancies'] = vacancies
    return render(request, 'vacancies.html', context=context)
