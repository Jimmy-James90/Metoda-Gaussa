import numpy as num
import PySimpleGUI as sg
from numpy import array, zeros

# inicjalizacja zadanych macierzy
a=num.array([
              [1,10,-7],
              [6,2.099,3.0],
              [5,-1.0,5.0]])

b=num.array([7,3.901,6])

n=len(b)
x = zeros(n,float)
#Layout okienka
wd, hg = 8 , 8
w,h =5,3
layout = [
    [sg.Text('DO WPISYWANIA PRZECINKA PROSZE UŻYWAC KROPKI')],
    [sg.InputText('', key='-INPUT1-',size=(wd, hg)),sg.InputText('', key='-INPUT2-',size=(wd, hg)),sg.InputText('', key='-INPUT3-',size=(wd, hg)),sg.Text('         '),sg.InputText('', key='-OUT1-',size=(wd, hg))],
    [sg.InputText('', key='-INPUT4-',size=(wd, hg)),sg.InputText('', key='-INPUT5-',size=(wd, hg)),sg.InputText('', key='-INPUT6-',size=(wd, hg)),sg.Text('         '),sg.InputText('', key='-OUT2-',size=(wd, hg)),sg.Button('Wprowadź', key='-GUZIK1')],
    [sg.InputText('', key='-INPUT7-',size=(wd, hg)),sg.InputText('', key='-INPUT8-',size=(wd, hg)),sg.InputText('', key='-INPUT9-',size=(wd, hg)),sg.Text('         '),sg.InputText('', key='-OUT3-',size=(wd, hg))],
    [sg.Text('WPROWADZONA MACIERZ'),sg.Text('          ')],
    [sg.Text('', key='-TEXT1-',size=(w,h)),sg.Text('   '),sg.Text('', key='-TEXT2-',size=(w,h)),sg.Text('   '),sg.Text('', key='-TEXT3-',size=(w,h)),sg.Text('      '),sg.Text('', key='-OUTP1-',size=(w,h))],
    [sg.Text('', key='-TEXT4-',size=(w,h)),sg.Text('   '),sg.Text('', key='-TEXT5-',size=(w,h)),sg.Text('   '),sg.Text('', key='-TEXT6-',size=(w,h)),sg.Text('      '),sg.Text('', key='-OUTP2-',size=(w,h))],
    [sg.Text('', key='-TEXT7-',size=(w,h)),sg.Text('   '),sg.Text('', key='-TEXT8-',size=(w,h)),sg.Text('   '),sg.Text('', key='-TEXT9-',size=(w,h)),sg.Text('      '),sg.Text('', key='-OUTP3-',size=(w,h))],
    [],
    [],
    [sg.Button('Oblicz', key='-GUZIK2')],
    [sg.Text('____________________WYNIK____________________')],
    [sg.Text('x1 ≈ '),sg.Text('', key='-WYNIK1-')],
    [sg.Text('x2 ≈ '),sg.Text('', key='-WYNIK2-')],
    [sg.Text('x3 ≈ '),sg.Text('', key='-WYNIK3-')],
    [sg.Button('DANE Z ZADANIA', key='-GUZIK3')],
    [sg.Text('_______________Powered by MJ_________________')]
]

window = sg.Window('Eliminacja Gaussa', layout)

#Obsługa okienek i przycisków
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    none = ''
    if event == '-GUZIK1':
        #zabezpieczenie przed wpisaniem niczego w okienko
        if values['-INPUT1-'] is none:
            a[0, 0] = 0
        else:
            a[0,0] = values['-INPUT1-']

        if values['-INPUT2-'] is none:
            a[0,1] = 0
        else:
            a[0, 1] = values['-INPUT2-']

        if values['-INPUT3-'] is none:
            a[0,2] = 0
        else:
            a[0,2] = values['-INPUT3-']

        if values['-INPUT4-'] is none:
            a[1, 0] = 0
        else:
            a[1, 0] = values['-INPUT4-']

        if values['-INPUT5-'] is none:
            a[1, 1] = 0
        else:
            a[1, 1] = values['-INPUT5-']

        if values['-INPUT6-'] is none:
            a[1, 2] = 0
        else:
            a[1, 2] = values['-INPUT6-']

        if values['-INPUT7-'] is none:
            a[2, 0] = 0
        else:
            a[2, 0] = values['-INPUT7-']
        if values['-INPUT8-'] is none:
            a[2, 1] = 0
        else:
            a[2, 1] = values['-INPUT8-']
        if values['-INPUT9-'] is none:
            a[2, 2] = 0
        else:
            a[2, 2] = values['-INPUT9-']
        if values['-OUT1-'] is none:
            b[0] = 0
        else:
            b[0] = values['-OUT1-']
        if values['-OUT2-'] is none:
            b[1] = 0
        else:
            b[1] = values['-OUT2-']
        if values['-OUT3-'] is none:
            b[2] = 0
        else:
            b[2] = values['-OUT3-']

        if a[0,0] == 0:
            window['-TEXT1-'].update("0")
        else:
            window['-TEXT1-'].update(values['-INPUT1-'])
        if a[0,1] == 0:
            window['-TEXT2-'].update("0")
        else:
            window['-TEXT2-'].update(values['-INPUT2-'])
        if a[0,2] == 0:
            window['-TEXT3-'].update("0")
        else:
            window['-TEXT3-'].update(values['-INPUT3-'])
        if a[1,0] == 0:
            window['-TEXT4-'].update("0")
        else:
            window['-TEXT4-'].update(values['-INPUT4-'])
        if a[1,1] == 0:
            window['-TEXT5-'].update("0")
        else:
            window['-TEXT5-'].update(values['-INPUT5-'])
        if a[1,2] == 0:
            window['-TEXT6-'].update("0")
        else:
            window['-TEXT6-'].update(values['-INPUT6-'])
        if a[2,0] == 0:
            window['-TEXT7-'].update("0")
        else:
            window['-TEXT7-'].update(values['-INPUT7-'])
        if a[2,1] == 0:
            window['-TEXT8-'].update("0")
        else:
            window['-TEXT8-'].update(values['-INPUT8-'])
        if a[2,2] == 0:
            window['-TEXT9-'].update("0")
        else:
            window['-TEXT9-'].update(values['-INPUT9-'])
        if b[0] == 0:
            window['-OUTP1-'].update("0")
        else:
            window['-OUTP1-'].update(values['-OUT1-'])
        if b[1] == 0:
            window['-OUTP2-'].update("0")
        else:
            window['-OUTP2-'].update(values['-OUT2-'])
        if b[2] == 0:
            window['-OUTP3-'].update("0")
        else:
            window['-OUTP3-'].update(values['-OUT3-'])

    if event == '-GUZIK2':
        #zabezpieczenie przed zerami w pierwszym i drugim wierszu macierzy
        #Jeżeli pierwszy element pierwszego wiersza to 0, zamien wiersz pierwszy z drugim
        if a[0, 0] == 0:
            a[0, 0], a[1, 0] = a[1, 0], a[0, 0]
            a[0, 1], a[1, 1] = a[1, 1], a[0, 1]
            a[0, 2], a[1, 2] = a[1, 2], a[0, 2]
            b[0], b[1] = b[1], b[0]
            # Jeżeli po zamianie drugi element drugiego wiersza to 0, zamien nowy wiersz drugi z trzecim
            if a[1, 1] == 0:
                a[1, 0], a[2, 0] = a[2, 0], a[1, 0]
                a[1, 1], a[2, 1] = a[2, 1], a[1, 1]
                a[1, 2], a[2, 2] = a[2, 2], a[1, 2]
                b[1], b[2] = b[2], b[1]
        for k in range(n - 1):
            for i in range(k + 1, n):
                if a[i, k] == 0: continue
                factor = a[k, k] / a[i, k]
                for j in range(k, n):
                    a[i, j] = a[k, j] - a[i, j] * factor
                b[i] = b[k] - b[i] * factor
        # Zamiana wstecz
        x[n - 1] = b[n - 1] / a[n - 1, n - 1]
        for i in range(n - 2, -1,-1):
            sum_ax = 0
            for j in range(i + 1, n):
                sum_ax += a[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / a[i, i]

        #Wypisanie wyników
        window['-WYNIK1-'].update(x[0])
        window['-WYNIK2-'].update(x[1])
        window['-WYNIK3-'].update(x[2])
    #WPROWADZ DANE Z ZADANIA
    if event == '-GUZIK3':
        a[0, 0] = 0
        a[0, 1] = 10
        a[0, 2] = -7
        a[1, 0] = 6
        a[1, 1] = 2.099
        a[1, 2] = 3
        a[2, 0] = 5
        a[2, 1] = -1
        a[2, 2] = 5
        b[0] = 7
        b[1] = 3.901
        b[2] = 6

        window['-TEXT1-'].update(0)
        window['-TEXT2-'].update(10)
        window['-TEXT3-'].update(-7)
        window['-TEXT4-'].update(6)
        window['-TEXT5-'].update(2.099)
        window['-TEXT6-'].update(3)
        window['-TEXT7-'].update(5)
        window['-TEXT8-'].update(-1)
        window['-TEXT9-'].update(5)
        window['-OUTP1-'].update(7)
        window['-OUTP2-'].update(3.901)
        window['-OUTP3-'].update(6)