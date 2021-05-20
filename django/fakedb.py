import random
import os, django
from openpyxl import load_workbook

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Movie

plot = "ОПИСАНИЕ ФИЛЬМА ОТСУТСТВУЕТ"
lis = load_workbook('../films.xlsx')['Лист1']

print('генерация')

for i in lis.values:
    Movie.objects.create(
        title=i[0],
        plot=plot,
        year=i[2],
        runtime=random.randint(10 , 250),
    )

print('Генерация окончена')