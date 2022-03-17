#def n_remove(text):
#    res = text.replace('\n', '')
#    return res

import PySimpleGUI as sg
import pandas as pd

sg.theme('Default1')

layout = [  [sg.Text('Put the text', font=(20))],
            [sg.InputText(size=(25,4), font=(20), key = 'input')],
            [sg.Button('Process', size = (25,0.5),key = 'go', font =(20))],
]

window = sg.Window('/n_remover', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'go':
        if len(values['input']) > 0:
            input = values['input']
            #output = n_remove(input)
            output = input.replace("\n", "")
            #output = ["test"]
            df=pd.DataFrame([output])
            df.to_clipboard(index=False,header=False)
            sg.popup('Done', font=(20), auto_close=True, auto_close_duration=0.5)
        
        if len(values['input']) == 0:
            sg.popup('Error: No Text', font=(20))

window.close()



