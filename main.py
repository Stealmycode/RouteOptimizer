import excel_parser as excel
from googleapi import calculate_optimal_path

def main():
    input("Please select the excel file downloaded from setmore. Press any key to continue.")
    file_path = excel.get_file()
    if '.xl' not in file_path:
        print("The selected file is not an excel file.")
        return
    address_map = excel.get_address_map(file_path)
    addresses = [k for k,v in address_map]
    optimal_path = calculate_optimal_path(addresses)
    print("This is the optimal travel path:")
    print(optimal_path)
    print("Select the folder where you would like to save the output.")
    save_location = excel.get_save_location() + "/optimal.xls"
    print(save_location)
    excel.write_addresses(optimal_path, save_location)





if __name__ == "__main__":
    main()
    input("Press any key to exit.")