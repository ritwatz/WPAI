from django.shortcuts import render

# Create your views here.
# scrape/views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def index(request):
    url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    Film = []
    Year = []
    Award = []
    Nomination = []
    count = 0

    for i in soup.findAll('td'):
        i = re.sub('^<td>.*">|<td>|</td>|<.*>|\n', "", str(i))
        if count == 0:
            Film.append(i)
            count += 1
        elif count == 1:
            Year.append(i)
            count += 1
        elif count == 2:
            Award.append(i)
            count += 1
        else:
            count = 0
            Nomination.append(i)

    oscar = pd.DataFrame({"Film": Film[:1360], "Year": Year[:1360], "Award": Award[:1360], "Nomination": Nomination[:1360]})
    oscar.to_scv("oscar.csv")

    context = {'data': oscar.to_html()}
    return render(request, 'scrape/index.html', context)
