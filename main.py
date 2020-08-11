import excel_parser as excel
from googleapi import calculate_optimal_path

def main():
    file_path = excel.get_file()
    if '.xl' not in file_path:
        print("The selected file is not an excel file")
        return
    addresses = excel.get_addresses(file_path)
    print(calculate_optimal_path(addresses))





if __name__ == "__main__":
    main()