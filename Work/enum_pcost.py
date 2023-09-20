import csv


def read_cost_enum(filename):
    share_list = []
    share_dict = {}
    try:
        f = open(filename,'rt')
    except FileNotFoundError:
        print("File/Path missing")
    else:
        with f:
            rows = csv.reader(f)
            header = next(rows)
            for row in rows:
                share_list.append((zip(header,row)))
                share_dict[[row[0]]=list(zip(header,row))
    return share_list,share_dict
