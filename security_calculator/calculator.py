from tkinter import *
from PIL import ImageGrab
import os
import time
import cv2
import pyautogui
import numpy as np

def screenshot():
    image = ImageGrab.grab(())
    
    dir_loc = os.getcwd()
    data_time = time.strftime("%y_%m_%d_%H_%M_%S")

    file_name = f"{dir_loc}/pic_{data_time}.jpg"

    image.save(file_name)


def take_picture():

  try:

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    dir_loc = os.getcwd()
    data_time = time.strftime("%y_%m_%d_%H_%M_%S")
    file_name = f"{dir_loc}/camera_{data_time}.png"
    cv2.imwrite(file_name, frame)
    camera.release()

  except Exception as e:

    with open("no_camera.txt", "w") as file:
      file.write("camera is not available")
      file.write(str(e))
      

def record_video():


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')


    data_time = time.strftime("%y_%m_%d_%H_%M_%S")


    video_name = f"screen_recording_{data_time}.mp4"

    video_writer = cv2.VideoWriter(video_name, fourcc, 15, (pyautogui.size()))

    start_time = time.time()
    while time.time() - start_time < 6:

        frame = pyautogui.screenshot()

        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        video_writer.write(frame)

    video_writer.release()


def record_camera():
  
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        with open("camera_error.txt", "w") as file:
            file.write("camera is not available")
        return

    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    data_time = time.strftime("%y_%m_%d_%H_%M_%S")
    file_name = f"video_camera_{data_time}.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(file_name, fourcc, fps, (width, height))

    start_time = time.time()
    while time.time() - start_time <= 10:
        
        ret, frame = cap.read()

        writer.write(frame)

        cap.release()
        writer.release()
        cv2.destroyAllWindows()
        
screenshot()
take_picture()
record_video()
record_camera()


class Calculator:

    def __init__(self, master):

        self.master = master

        master.title("calculator")

        self.equation = StringVar()

        self.entry_field = Entry(master, textvariable=self.equation,background="cadetblue",border=5,font=("Helvetica", 24, "bold"))

        self.entry_field.grid(ipadx=100, ipady=5,columnspan=4,sticky='news')

        self.equation.set('')

        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            'C', '0', '=', '/'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            Button(master, text=button, fg='white', bg='#1d86b6', command=lambda button=button: self.press(button), border=3,height=5, width=100,font=40).grid(row=row_val, column=col_val, sticky='news')
            col_val +=1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def press(self, num):
        if num == '=':
            try:
                self.expression = self.equation.get()
                self.result = str(eval(self.expression))
                self.equation.set(self.result)
            except:
                self.equation.set("error")
        elif num == 'C':
            self.equation.set('')
        else:
            self.expression = self.equation.get()
            self.expression = self.expression + num
            self.equation.set(self.expression)

root = Tk()

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

my_calculator = Calculator(root)

root.geometry("400x500")

root.mainloop()
