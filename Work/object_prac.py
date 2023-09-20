import csv

def date_tuple(date: str):
    return tuple(date.split('/'))

def covert_folio(filename):
    f = open(filename)
    record = []
    rows = csv.reader(f)
    header = next(rows)
    types = [str, float, date_tuple, str, float, float, float, float, int]
    for row in rows:
        converted = [func(val) for func, val in zip(types,row)]
        record.append(dict(zip(header,converted)))
    return record

