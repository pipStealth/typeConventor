import os
import ffmpeg
from glob import glob

def convert_wma_to_mp3(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, codec='libmp3lame')
        .run()
    )

input_files = glob('*.mp3') # []

for input_file in input_files:
    output_file = os.path.splitext(input_file)[0] + '.wma'
    convert_wma_to_mp3(input_file, output_file)

def delr():
    files = os.listdir()

    for file in files:
        if file.endswith('.mp3'):
            os.remove(file)

delr()

print("Process end")