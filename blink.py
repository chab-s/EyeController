import tobii_research as tr
import time
import pyautogui
from pynput.mouse import Controller
import numpy as np
from queue import Queue
import keyboard

found_eyetrackers = tr.find_all_eyetrackers()
mouse = Controller()

my_eyetracker = found_eyetrackers[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

print(pyautogui.size())
#(Size(width=1440, height=900))

def moving_average(data, window_size):
    smoothed_data = np.convolve(data, np.ones(window_size)/window_size, mode='same')
    return smoothed_data

def gaze_data_callback(gaze_data):
    gaze_data_queue.put((np.mean([gaze_data['left_gaze_point_on_display_area'][0], gaze_data['right_gaze_point_on_display_area'][0]])*pyautogui.size()[0], np.mean([gaze_data['left_gaze_point_on_display_area'][1], gaze_data['right_gaze_point_on_display_area'][1]])*pyautogui.size()[1]))
  
     


if __name__ == '__main__':

    data_list = []
    gaze_data_queue = Queue()
    my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    nbr_data = 15
    paused = False
    blink_time = 0.3

    while True:
        data = gaze_data_queue.get(timeout=1)
        
        if np.isnan(data[0]):
            start_clock = time.time()
            while np.isnan(data[0]) and (time.time() - start_clock) < blink_time :
                data = gaze_data_queue.get(timeout=1)
            
            if (time.time() - start_clock) > blink_time and np.isnan(data[0]):
                print('blink')
        else:
            start_clock = None

