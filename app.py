import PySimpleGUI as sg
from subscribers import get_subscriber_count, get_channel_title, update_every_minute
import threading

sg.theme('darkblack')

center_itens = [
    [sg.Text('MONITORAR EM TEMPO REAL', size=(30, 0),
             text_color='red', font=('Impact', 15), justification='center')],
    [sg.Text('Canal', key='channel_name', size=(30, 0),
             text_color='white', font=('Impact', 20), justification='center')],
    [sg.Text('99,999', key='sub_count', text_color='red', font=(
        'Impact', 25)), sg.Text('Inscritos', text_color='white')],
    [sg.Text('ID do canal', text_color='white')],
    [sg.Input(key='channel_id', size=(20, 0))],
    [sg.Button('Buscar')]
]

layout = [
    [sg.Column(center_itens, element_justification='center')]
]

window = sg.Window('Subscriber Watcher', layout=layout, size=(
    300, 250), element_justification='center', resizable=False)

subscriber_count_thread = None

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Buscar':
        channel_id = values['channel_id']
        total = get_subscriber_count(channel_id)
        title = get_channel_title(channel_id)
        window['sub_count'].Update(str(total))
        window['channel_name'].Update(str(title))
        if subscriber_count_thread != None:
            subscriber_count_thread = threading.Thread(
                target=update_every_minute, args=(channel_id, window)).join()
            subscriber_count_thread = threading.Thread(
                target=update_every_minute, args=(channel_id, window)).start()
        elif subscriber_count_thread == None:
            subscriber_count_thread = threading.Thread(
                target=update_every_minute, args=(channel_id, window)).start()
