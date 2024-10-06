import time
import tobii_research as tr
import numpy as np
from pynput.mouse import Controller

from EyeController import EyeController

def main(eye_controller:EyeController, cursor:Controller) :
    data_list = []
    paused = False
    eye_controller.eye_tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, eye_controller.gaze_data_callback, as_dictionary=True)
    print("main")
    while True:
        try:
            data = eye_controller.gaze_data_queue.get(timeout=1)

            if eye_controller.blink_detection(data=data, blink_time=0.3):
                print("blink detected")
                paused = not paused
                time.wait(1)


            if paused == False : 
                data_list.append(data)
                # Gardez au maximum les n dernières données
                if len(data_list) > eye_controller.window_size:
                    data_list.pop(0)
                
                # Si nous avons collecté n données, calculez la moyenne
                if len(data_list) == eye_controller.window_size:
                    # mean
                    # Calculez la moyenne des données
                    avg_data = np.mean(data_list, axis=0)  # axis=0 signifie que nous calculons la moyenne de chaque composante séparément

                
                cursor.position = avg_data
            

            
        except:
            # La file d'attente est vide, aucune donnée n'est disponible pour le moment
            pass

if __name__ == '__main__':
    eye_controller = EyeController()
    crusor = Controller()
    main(eye_controller=eye_controller, cursor=crusor)