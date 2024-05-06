from tkinter import *
from PIL import ImageGrab
import os
import time
import cv2
import pyautogui
import numpy as np

def screenshot(self):
    image = ImageGrab.grab(())
    
    dir_loc = os.getcwd()
    data_time = time.strftime("%y_%m_%d_%H_%M_%S")

    file_name = f"{dir_loc}/pic_{data_time}.jpg"

    image.save(file_name)


def take_picture(self):

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
      

def record_video(self):


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


  


def record_camera(self):
  
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



class Calculator:

    def __init__(self, master):

        self.master = master

        master.title("calculator")

        self.equation = StringVar()

        self.entry_field = Entry(master, textvariable=self.equation)

        self.entry_field.grid(columnspan=140, ipadx=20)

        self.equation.set('')

        self.button_1 = Button(master, text='1', fg='white', bg='blue', command=lambda: (self.press("1"), screenshot(self)), height=1, width=7)
        self.button_1.grid(row=2, column=0)

        self.button_2 = Button(master, text='2', fg='white', bg='blue', command=lambda: (self.press("2"), record_video(self)), height=1, width=7)
        self.button_2.grid(row=2, column=1)

        self.button_3 = Button(master, text='3', fg='white', bg='blue', command=lambda: (self.press("3"), take_picture(self)), height=1, width=7)
        self.button_3.grid(row=2, column=2)

        self.button_4 = Button(master, text='4', fg='white', bg='blue', command=lambda: (self.press("4"), record_camera(self)), height=1, width=7)
        self.button_4.grid(row=3, column=0)

        self.button_5 = Button(master, text='5', fg='white', bg='blue', command=lambda: self.press(5), height=1, width=7)
        self.button_5.grid(row=3, column=1)

        self.button_6 = Button(master, text='6', fg='white', bg='blue', command=lambda: self.press(6), height=1, width=7)
        self.button_6.grid(row=3, column=2)

        self.button_7 = Button(master, text='7', fg='white', bg='blue', command=lambda: self.press(7), height=1, width=7)
        self.button_7.grid(row=4, column=0)

        self.button_8 = Button(master, text='8', fg='white', bg='blue', command=lambda: self.press("8"), height=1, width=7)
        self.button_8.grid(row=4, column=1)

        self.button_9 = Button(master, text='9', fg='white', bg='blue', command=lambda: self.press(9), height=1, width=7)
        self.button_9.grid(row=4, column=2)

        self.button_0 = Button(master, text='0', fg='white', bg='blue', command=lambda: self.press(0), height=1, width=7)
        self.button_0.grid(row=5, column=0)

        self.button_plus = Button(master, text='+', fg='white', bg='blue', command=lambda: self.press('+'), height=1, width=7)
        self.button_plus.grid(row=2, column=3)

        self.button_minus = Button(master, text='-', fg='white', bg='blue', command=lambda: self.press('-'), height=1, width=7)
        self.button_minus.grid(row=3, column=3)

        self.button_multiply = Button(master, text='*', fg='white', bg='blue', command=lambda: self.press('*'), height=1, width=7)
        self.button_multiply.grid(row=4, column=3)

        self.button_divide = Button(master, text='/', fg='white', bg='blue', command=lambda: self.press('/'), height=1, width=7)
        self.button_divide.grid(row=5, column=3)

        self.button_equal = Button(master, text='=', fg='white', bg='blue', command=self.equal_press, height=1, width=7)
        self.button_equal.grid(row=5, column=2)

        self.button_clear = Button(master, text='C', fg='white', bg='blue', command=self.clear, height=1, width=7)
        self.button_clear.grid(row=5, column=1)


    def press(self, num):

        self.expression = self.equation.get()

        self.expression = self.expression + str(num)

        self.equation.set(self.expression)

    def equal_press(self):

        try:

            self.expression = self.equation.get()

            self.result = str(eval(self.expression))

            self.equation.set(self.result)

            self.expression = ''
        except:

            self.equation.set("error")

            self.expression = ''


    def clear(self):

        self.entry_field.delete(0, END)

        self.expression = ''

root = Tk()
my_calculator = Calculator(root)


root.mainloop()

