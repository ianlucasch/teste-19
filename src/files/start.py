import os
import camelot
import pandas as pd
import logging
from unidecode import unidecode

class PDFTableExtractor:
    def __init__(self, file_name, configs):
        self.path = os.path.abspath(f"src/files/pdf/{configs["name"].lower()}/{file_name}.pdf")
        self.csv_path = os.path.abspath(f"src/files/csv/")
        self.file_name = file_name
        self.configs = configs

    def start():
        pass

    def get_table_data():
        pass

    def save_csv():
        pass

    def add_infos():
        pass

    def fix_header():
        pass

    def sanitize_column_name():
        pass

    def send_to_db():
        pass

if __name__ == "__main__":
    extractor = PDFTableExtractor().start()

    print(extractor)