import os
import getpass
import PySimpleGUI as sg



# project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'data')

# list files in the directory
list_files = []

layout = [
    [sg.Button('Search Files')],
    [sg.Listbox(list_files, size=(60,20), key='-LIST-')]
    
]

window = sg.Window('System Replier', layout, size=(800, 600))


while True:
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Search Files':
        # getting logged user
        user = getpass.getuser()
        
        # moving to directory
        os.chdir(f"C:/Users{user}/Desktop")
        
        current_diretory = os.getcwd()
        
        
        
    
    
window.close()
