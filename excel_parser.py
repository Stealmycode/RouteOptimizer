import pandas
import tkinter as tk
from tkinter import filedialog


def get_address_map(file_path):
    data = pandas.read_excel(file_path, header = 0)

    #+1 because there is extra column in row for the row number
    filtered_indices = [index+1 for index in range(len(data.columns)) if data.columns[index] in ['Address','City', 'State', 'Zip']]
    res = {}
    index = 0
    for row in data.itertuples():
        filtered_row = [str(row[i]) for i in filtered_indices]
        address = ", ".join(filtered_row)
        res[address] = index
        index += 1
    return res

def get_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def get_save_location():
    root = tk.Tk()
    root.withdraw()
    save_location = filedialog.askdirectory()
    return save_location

def write_addresses(addresses, file_path):
    dataframe = pandas.DataFrame(addresses, columns = ['Optimal address path'])
    dataframe.to_excel(file_path)