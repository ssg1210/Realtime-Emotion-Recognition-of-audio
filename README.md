# Realtime-Emotion-Recognition-of-audio
The project is a part of course ECE-GY 6183 DSP Lab (Fall 2022)

Participants: 

Rheya Vithalani

Srishti Gupta

Mrunal Kshirsagar


# Steps to setup the project:

`python3 -m venv dsplab`


`source dsplab/bin/activate`


`pip install -r requirements.txt`


# About the project
Our main task is to implement Digital Signal Processing in Realtime. 

Parts of the project:
1. Dataset Collection

We are mainly using two datasets:

1. [The Ryerson Audio-Visual Database of Emotional Speech and Song](https://zenodo.org/record/1188976#.Y513POzMKLp) (RAVDESS)

There are 7356 files in the Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) (total size: 24.8 GB). 24 professional actors, 12 male and 12 female, are recorded in the database vocalizing two sentences that are lexically similar in a neutral North American accent. Both speech and music can display a range of emotions, including happiness, sadness, anger, fear, surprise, and disgust. There are two emotional intensity levels (normal and strong) and one neutral expression produced for each expression. Three modality forms are accessible for all conditions: Audio-only (16bit, 48kHz.wav), Audio-Video (720p H.264, AAC 48kHz,.mp4), and Video-only (480p H.264, AAC 48kHz,.mp4) (no sound).

2. [Toronto emotional speech set (TESS) Collection](https://tspace.library.utoronto.ca/handle/1807/24487)

 There are 2800 stimuli in total. Two actresses were recruited from the Toronto area. Both actresses speak English as their first language, are university educated, and have musical training. 

For example: 03-01-01-01-02-01-06.wav

Emotions are recognized as follows from the 3rd number of filename: 01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised

2. Feature Extraction

For features we are using MFCCS:

Mel-Frequency Cepstral Coefficients (MFCCs) are a commonly used feature representation for speech emotion recognition tasks. MFCCs are derived from the frequency spectrum of a speech signal and capture important spectral characteristics of the signal, such as the pitch and formants, which are important for identifying the speaker's emotional state.

To compute MFCCs, the following steps are typically followed:

a. Pre-processing: The speech signal is pre-processed to remove noise and improve the signal-to-noise ratio. This can involve applying a high-pass filter to remove low-frequency noise and a spectral subtraction algorithm to remove background noise.

b. Windowing: The signal is then divided into overlapping frames, and each frame is multiplied by a window function (e.g., a Hamming window) to reduce spectral leakage.

c. Fourier Transform: The Fourier Transform is applied to each frame to obtain the frequency spectrum of the frame.

d. Mel-Frequency Filterbank: A Mel-Frequency Filterbank is applied to the frequency spectrum to produce a set of Mel-Frequency Cepstral Coefficients (MFCCs). The Mel-Frequency Filterbank is a set of band-pass filters that are spaced equally on the Mel scale, which is a non-linear scale that approximates the frequency response of the human auditory system. The output of each filter is taken as the energy in the corresponding frequency band.

e. Discrete Cosine Transform: The MFCCs are then transformed using the Discrete Cosine Transform (DCT) to decorrelate the coefficients and reduce the dimensionality of the feature vector.

MFCCs are commonly used as input features to machine learning models for speech emotion recognition tasks because they capture important spectral characteristics of the speech signal and are robust to noise and variations in the signal.


3. Training the neural network

We have used 1D CNN to train a simple neural nework with dimensions = input shape, 1 

We also used "sparse_categorical_crossentropy" as loss and "rmsprop" as our optimizers. The decision of using this loss and optimizer is experimental and it might vary for a relatively different dataset/model

Following is the picture of our model:

<img width="655" alt="image" src="https://user-images.githubusercontent.com/46345142/208232911-c902eb37-caf4-44c6-b441-dfc3913e2825.png">

3. Training the neural network:

The model was trained over colab using minimal free GPU. It was trained for 1000 epochs, time required to train the complete model was around 3 to 4 hours. The approach that was followed: Experiemnt with different training stratergies like changing dimension of network, and looking at the loss curves. If the loss curve was decreasing then we allowed the training to continue for longer duration.


4. Offline testing the model with Tkinter:
Here we show Tkinter concepts learned in the class material and apply it in real world. We show the power of Tkinter, it can browse, play, pause, stop music. It can also create a small library of audio files where we can search from our playlist and select the audio of our choice.

Below command can be used to run the demo for Offline predictions with Tkinter:

`python3 Offline_pred.py`

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/46345142/208322915-924c74cf-ca26-4d9f-a8b4-9ba44ce7b2b3.png">


5. Realtime emotion recognition 

This is the main part of the our project where in we took our existing code and modified it to the theme of the DSP Lab Project i.e. to generate the results real time.

Below command can be used to run the demo for real time emotion recognition with user input (audio/speech):

`python3 real_time_emotion.py`

<img width="730" alt="image" src="https://user-images.githubusercontent.com/46345142/208322976-846e600c-75f7-4dc1-ac63-2f4c22210f6c.png">


## References

The project is inspired by following works:

[emotion-classification-from-audio-files](https://github.com/marcogdepinto/emotion-classification-from-audio-files)

https://www.kaggle.com/code/ejlok1/audio-emotion-part-1-explore-data
