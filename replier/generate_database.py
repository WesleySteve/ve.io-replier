import os
import PySimpleGUI as sg

from upload_data.upload_data_sqlite import check_db_exists, create_db_files_xlsx_and_xls


# project paths
BASE_DIR = os.path.dirname(os.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'data')

