"""
This file can be used to try a live prediction. 
"""

import keras
import librosa
import numpy as np
import pandas as pd

MODEL_DIR_PATH = ""


class LivePredictions:
    """
    Main class of the application.
    """

    def __init__(self, file):
        """
        Init method is used to initialize the main parameters.
        """
        self.file = file
        self.path = MODEL_DIR_PATH + 'Emotion_Voice_Detection_Model.h5'
        self.loaded_model = keras.models.load_model(self.path)

    def make_predictions(self):
        """
        Method to process the files and create your features.
        """
        data, sampling_rate = librosa.load(self.file)
        print("Data: ", data, data.shape)
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
        newdf = pd.DataFrame(data=mfccs).T
        x= np.expand_dims(newdf, axis=2)
        print("Shape of x: ", x.shape)
        predictions = self.loaded_model.predict(x)
        classes_x=np.argmax(predictions,axis=1)
        return self.convert_class_to_emotion(classes_x)
        

    @staticmethod
    def convert_class_to_emotion(pred):
        """
        Method to convert the predictions (int) into human readable strings.
        """
        
        label_conversion = {'0': 'neutral',
                            '1': 'calm',
                            '2': 'happy',
                            '3': 'sad',
                            '4': 'angry',
                            '5': 'fearful',
                            '6': 'disgust',
                            '7': 'surprised'}

        for key, value in label_conversion.items():
            if int(key) == pred:
                label = value
        return label

