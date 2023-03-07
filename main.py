# command 
# ffmpeg -i input.mp4 -preset ultrafast -c:v libx264 -movflags faststart -crf "${crfValue}" -vf tmix=frames="${framesAmount}":weights="${weighting}" -c:a copy -r 60 output-"${fpsAmount}"fps-resampled.mp4
# 
import PySimpleGUI as sg      
import cv2
import os

toggle_sec1 = False
cmd = 'ffmpeg.exe -y -i "$VDEO_IN" -preset $PRESET -c:v libx264 -movflags faststart -crf 20 -vf tmix=frames=$VIDEO_IN_FPS:weights=1 -c:a copy -r 60 "$VIDEO_OUT"'
sg.theme('DarkAmber')

layout = [
    [sg.Text('Resample++', font=('Lucida', 16))],  
    [sg.Text('input file', font="Lucida")],
    [sg.In(size=(16, 1)) ,sg.FileBrowse(file_types=((('Video File to Resample', '*.mp4 *.mkv'),)))],
    [sg.Text('output file', font="Lucida")],
    [sg.In(size=(16, 1)) ,sg.FileSaveAs(file_types=((('Resampled Video', '*.mp4 *.mkv'),)))],
    [sg.Text('Other Stuff', font="Lucida")],
    [sg.Text('FPS:', font="Lucida"), sg.InputText(size=(4, 1), key="fps", default_text="60")],
    [sg.Combo(['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow', 'placebo'], default_value='ultrafast')],  
    [sg.Checkbox('Show CLI Args', size=(11,1), enable_events=True, key='chk_cli')],
    [sg.InputText(key="inp", default_text=cmd, visible=False)],
    [sg.Button('Render!', key="asas"), sg.Exit()]
]      

window = sg.Window('Resample++', layout)      

while True:                             # The Event Loop
    event, values = window.read() 

    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

    if event == 'chk_cli':
        toggle_sec1 = not toggle_sec1
        window['inp'].update(visible=toggle_sec1)

    if event == 'asas':
        fpsmult = round(int(layout[6][1].get()) / 60, 2)
        print("RESAMPLE MULTIPLIER: %d" % fpsmult)
        print("START RENDER")

        os.system(layout[9][0].get().replace('$VDEO_IN', values[0]).replace("$PRESET", values[2]).replace("$VIDEO_IN_FPS", str(fpsmult)).replace("$VIDEO_OUT", values[1]))



window.close()