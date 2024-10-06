import numpy as np
from queue import Queue
import tobii_research as tr
from pynput.mouse import Controller
import pyautogui
import time


class EyeController:
    def __init__(self):
        self.eye_tracker = self.define_eyetracker()
        self.screen_size = pyautogui.size()
        self.gaze_data_queue = Queue()
        self.window_size = 15

    def define_eyetracker(self):
        """
            Permet de selectionner le dispositif d'eyetracking utilise
        """
        found_eyetrackers = tr.find_all_eyetrackers()
        if len(found_eyetrackers) > 1:
            #% créer une fenetre de selection
            pass
        else:
            return found_eyetrackers[0]

    def average_location(self, window_size:int):
        """
            Calcule la position moyenne du cruseur sur une fenetre definie
        """
        smoothed_data = np.convolve(self.data, np.ones(window_size)/window_size, mode='same')
        return smoothed_data
    
    def gaze_data_callback(self, gaze_data:list):
        """
            Stock dans une Queue les valeurs de position du regard retournees pas l eyetracker
        """
        self.gaze_data_queue.put((np.mean([gaze_data['left_gaze_point_on_display_area'][0], gaze_data['right_gaze_point_on_display_area'][0]])*self.screen_size[0], np.mean([gaze_data['left_gaze_point_on_display_area'][1], gaze_data['right_gaze_point_on_display_area'][1]])*self.screen_size[1]))
    
    def blink_detection(self, data:tuple, blink_time=0.3):
        """
            Detecte un clignement d'oeil volontaire
        """
        if np.isnan(data[0]):
            start_clock = time.time()
            while np.isnan(data[0]) and (time.time() - start_clock) < blink_time :
                data = self.gaze_data_queue.get(timeout=1)
            
            if (time.time() - start_clock) > blink_time and np.isnan(data[0]):
                return True
                
        else:
            start_clock = None