import yaml
from openpyxl import load_workbook

def load_config(file_path):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)

    return config

def open_excel_file(file_path):
    wb = load_workbook(filename=file_path)
    
    return wb

def save_excel_file(wb, file_path):
    wb.save(filename=file_path)

def process_excel_file(wb, sheet_name):
    sheet = wb[sheet_name]

    # Delete first row and first column
    # This is just for demo purposes
    sheet.delete_cols(1, 1)
    sheet.delete_rows(1, 1)

def main():
    config = load_config("config.yaml")
    input = config["input"]
    output = config["output"]
    sheet_name = config["sheet_name"]
    wb = open_excel_file(input)
    
    process_excel_file(wb, sheet_name=sheet_name)
    
    save_excel_file(wb, output)


if __name__ == "__main__":
    main()
