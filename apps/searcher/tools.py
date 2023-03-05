import xlrd
import os
from django.conf import settings

FILE_DIR = os.path.join(settings.BASE_DIR, 'apps', 'searcher', 'fixtures', 'searcher_data.xls')

def parse_meanings_table():
    book = xlrd.open_workbook(FILE_DIR)
    result = dict()
    sheet = book.sheet_by_index(0)
    meanings = sheet.row_values(0)
    del meanings[0]
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        del row[0]

        index = row.index(1)
        result[row[0]] = meanings[index]
    return result


def get_meanings():
    book = xlrd.open_workbook(FILE_DIR)
    sheet = book.sheet_by_index(0)
    meanings = sheet.row_values(0)
    del meanings[0] 
    del meanings[0]
    meanings = [meaning.strip() for meaning in meanings]
    return meanings


def get_phrases():
    book = xlrd.open_workbook(FILE_DIR)
    sheet = book.sheet_by_index(0)
    phrases = sheet.col_values(1)
    del phrases[0]
    phrases = [phrase.strip() for phrase in phrases]
    return phrases
