import os
import PySimpleGUI as sg

from upload_data.upload_data_sqlite import check_db_exists, create_db_files_xlsx_and_xls


# project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'data')


layout = [
    [sg.Text('Choose file'), sg.Input(), sg.FileBrowse(key='-IN-')],
    [sg.Button('Submit')],
    [sg.Text(key='-FILE_PATH-')],
    [sg.Text(key='-MSG-')]
  
]

window = sg.Window('System Replier', layout, size=(1200,300))


while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'Submit':
        
        path = values['-IN-']
        file = os.path.basename(path)
        
        if check_db_exists(DATA_DIR):
            
            # remove
            window['-MSG-'].update(f'Database already exists')
            
        else:
            os.rename(path, os.path.join(DATA_DIR, 'DADOS.xlsx'))
            
            if create_db_files_xlsx_and_xls(DATA_DIR, file):
                window['-MSG-'].update(f'Database created successfully')
        

window.close()    