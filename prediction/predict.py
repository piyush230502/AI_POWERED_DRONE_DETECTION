import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class DroneNon:
    def __init__(self,filename):
        self.filename =filename


    def predictionDroneNon(self):
        # load model
        #model = load_model(os.path.join("model", "model.h5"))
        model = load_model(os.path.join("model", "F:\Computer_Vision\DRONE_DETECTION\best.pt"),compile=False)

        imagename = self.filename
        # test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.load_img(imagename, target_size = (64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Drone'
            return [{ "image" : prediction}]
        else:
            prediction = 'NoDrone'
            return [{ "image" : prediction}]


