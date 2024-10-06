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
    # Print gaze points of left and right eye
    # print(gaze_data['left_gaze_point_on_display_area'][0]*pyautogui.size()[0], gaze_data['left_gaze_point_on_display_area'][1]*pyautogui.size()[1])
    gaze_data_queue.put((np.mean([gaze_data['left_gaze_point_on_display_area'][0], gaze_data['right_gaze_point_on_display_area'][0]])*pyautogui.size()[0], np.mean([gaze_data['left_gaze_point_on_display_area'][1], gaze_data['right_gaze_point_on_display_area'][1]])*pyautogui.size()[1]))
    # mouse.position = (gaze_data['left_gaze_point_on_display_area'][0]*pyautogui.size()[0], gaze_data['right_gaze_point_on_display_area'][1]*pyautogui.size()[1])
    # time.sleep(0.01) # delay over 0.01s
    #pyautogui.moveTo(gaze_data['left_gaze_point_on_display_area'][0]*pyautogui.size()[0], gaze_data['right_gaze_point_on_display_area'][1]*pyautogui.size()[1], duration=0.1)
    
if __name__ == '__main__':

    
    data_list = []
    gaze_data_queue = Queue()
    my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    nbr_data = 15
    paused = False

    while True:
        if keyboard.is_pressed('space'):
            paused = not paused
            while keyboard.is_pressed('space'):
                pass

        if paused == False : 
            try:
                data = gaze_data_queue.get(timeout=1)
                data_list.append(data)
                # Gardez au maximum les n dernières données
                if len(data_list) > nbr_data:
                    data_list.pop(0)
                
                # Si nous avons collecté n données, calculez la moyenne
                if len(data_list) == nbr_data:
                    
                    # mean
                    # Calculez la moyenne des données
                    avg_data = np.mean(data_list, axis=0)  # axis=0 signifie que nous calculons la moyenne de chaque composante séparément
                    
                mouse.position = avg_data
                
            except:
                # La file d'attente est vide, aucune donnée n'est disponible pour le moment
                pass
            
        else :
            print("pause")