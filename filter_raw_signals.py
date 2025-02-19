from scipy.signal import butter, lfilter, filtfilt
from scipy.signal import freqs, periodogram
from scipy import stats
import numpy as np
import os
import pandas as pd

def butter_bandpass(lowcut, highcut, fSample, order=5):
    nyq = 0.5 * fSample
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band', analog=False)
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fSample, order=5):
    b, a = butter_bandpass(lowcut, highcut, fSample, order=order)
    y = filtfilt(b, a, data)
    return y

def butter_bandstop(lowcut, highcut, fSample, order=5):
    nyq = 0.5 * fSample
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], 'bandstop', analog=False)
    return b, a

def butter_bandstop_filter(data, lowcut, highcut, fSample, order=5):
    b, a = butter_bandstop(lowcut, highcut, fSample, order=order)
    y = filtfilt(b, a, data)
    return y

fSample = 2000

dfIn = pd.read_csv("D:\\Project_New\\Dataset\\Kapha\\Increased Data\\IncNormal.csv", header=None)

aC1 = []
for index, row in dfIn.iterrows():
    dataArray1 = list(row[5:506])
    filteredData1 = butter_bandpass_filter(dataArray1, 50.0, 300.0, fSample, order=5)
    filteredData1 = butter_bandstop_filter(filteredData1, 48.0, 53.0, fSample, order=5)  # Notch filter to remove Power line interference
    filteredData1 = butter_bandstop_filter(filteredData1, 100.0, 104.0, fSample, order=5)  # Notch filter to Power line interference - Harmonics 1
    filteredData1 = filteredData1.astype(int)
    filteredData1 = filteredData1.tolist()
    aC1.append(filteredData1)

dfOut = pd.DataFrame({'filteredData1': aC1})
dfOut.to_csv("D:\\Final_Project_Working\\filt_disease.csv", header=True, index=False)
print("The signal is filtered")
