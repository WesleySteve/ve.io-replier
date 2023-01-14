import os

import PySimpleGUI as sg



# project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'data')

# list files in the directory
list_files = []

layout = [
    [sg.Button('Search Files')],
    [sg.ListBox(list_files, size=(70,30), key='-LIST-')]
    
]


