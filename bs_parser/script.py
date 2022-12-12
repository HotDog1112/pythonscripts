from bs4 import BeautifulSoup as bs
import requests
from prettytable import PrettyTable as pt
import os
import telebot as bot

session = requests.Session()
INTEREST_URL = "https://hh.ru/vacancies/devops"
# get page
def getRequest(page_address):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    res = requests.get(INTEREST_URL, headers=headers)
    return res.text

# make table with PrettyTable module
row = []
column_name = ['Vacancy', 'Company', 'Salary']
col = len(column_name)
table = pt(column_name)
page_code = getRequest(INTEREST_URL)
rows = []

# find block of information about vacancies
def findAllBlocks(page_code):
    s = bs(page_code, features='lxml')
    search = s.find('div', {'class': 'vacancy-serp-content'})
    vacancies = search.find_all('div', {'class': 'serp-item'})
    return vacancies

# fill table rows
for vacancy in findAllBlocks(page_code):
    name = vacancy.find('a', {'class':'serp-item__title'}).text
    company = vacancy.find('div', {'class':'vacancy-serp-item__meta-info-company'}).text
    salary = vacancy.find('span', {'class':'bloko-header-section-3'})
    if salary:
        salary = salary.text
    else:
        salary = '-'
    row.append(name)
    row.append(company)
    row.append(salary)
    rows.append(row)
    row = []

table.add_rows(rows)

def rewriteFile(table):
    filename = 'table.txt'
    f = open(filename, 'w')
    table = str(table)
    f.write(table)
    f.close()

rewriteFile(table)
