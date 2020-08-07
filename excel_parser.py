import pandas


def get_addresses():
    data = pandas.read_excel('appointments.xls', header = 0)

    #+1 because there is extra column in row for the row number
    filtered_indices = [index+1 for index in range(len(data.columns)) if data.columns[index] in ['Address','City', 'State', 'Zip']]
    res = []
    for row in data.itertuples():
        filtered_row = [str(row[i]) for i in filtered_indices]
        res.append(", ".join(filtered_row))
    return res