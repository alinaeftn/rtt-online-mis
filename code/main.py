from excel.excel import open_excel_file, save_excel_file, process_excel_file
from onedrive.onedrive import upload_to_onedrive
import sys


def process_file(file_path):
    wb = open_excel_file(file_path)
    process_excel_file(wb, sheet_name="use-case")
    new_file_path = file_path.replace(".xlsx", "_new.xlsx")
    save_excel_file(wb, new_file_path)

    return new_file_path


if __name__ == "__main__":
    file_path = sys.argv[1]
    destination_folder = sys.argv[2]

    new_file_path = process_file(file_path)
    upload_to_onedrive(new_file_path, destination_folder)
