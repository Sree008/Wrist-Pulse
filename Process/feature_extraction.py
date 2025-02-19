import pandas as pd
from scipy import stats
import numpy as np
import math
import json
import statistics as st
from sklearn.preprocessing import StandardScaler

# Feature extraction
def meanAbsoluteValue(plotdata):
    N = len(plotdata)
    temp = 0
    for i in range(N):
        temp = temp + abs(plotdata[i])
    return int(temp / N)

def rootMeanSquare(plotdata):
    s = 0
    for i in range(len(plotdata)):
        s = s + plotdata[i] ** 2
    s = s / len(plotdata)
    return int(math.sqrt(s))

def crestFactor(plotdata):
    rms = rootMeanSquare(plotdata)
    peak = max(abs(x) for x in plotdata)
    if rms != 0:
        return peak / rms
    else:
        return 0


def zeroCrossingRate(plotdata):
    N = len(plotdata) - 1
    temp = 0

    def myfunc(x, y):
        if (x * y) < 0:
            return 1
        else:
            return 0

    for i in range(N):
        temp = temp + (myfunc(plotdata[i], plotdata[i + 1]))
    return temp / N

def peakToPeakAmplitude(plotdata):
    return max(plotdata) - min(plotdata)

def spectralCentroid(plotdata):
    fft_vals = np.fft.fft(plotdata)
    freqs = np.fft.fftfreq(len(fft_vals))
    return np.sum(np.abs(freqs) * np.abs(fft_vals)) / np.sum(np.abs(fft_vals))

def spectralSpread(plotdata):
    fft_vals = np.fft.fft(plotdata)
    freqs = np.fft.fftfreq(len(fft_vals))
    centroid = spectralCentroid(plotdata)
    return np.sum(((np.abs(freqs) - centroid) ** 2) * np.abs(fft_vals)) / np.sum(np.abs(fft_vals))

def spectralFlatness(plotdata):
    fft_vals = np.fft.fft(plotdata)
    non_zero_fft_vals = fft_vals[fft_vals != 0]
    geometric_mean = np.exp(np.mean(np.log(np.abs(non_zero_fft_vals))))
    arithmetic_mean = np.mean(np.abs(non_zero_fft_vals))
    if arithmetic_mean != 0:
        return geometric_mean / arithmetic_mean
    else:
        return 0


# -----------------------------------------------------------------------------
fSample = 2000

dfIn = pd.read_csv("D:\\Final_Project_Working\\filt_disease.csv")

aC = []
for index, row in dfIn.iterrows():
    adcData1 = json.loads(row['filteredData1'])

    featureSet = [meanAbsoluteValue(adcData1),
                  st.variance(adcData1),
                  np.std(adcData1),
                  stats.skew(adcData1),
                  stats.kurtosis(adcData1),
                  rootMeanSquare(adcData1),
                  crestFactor(adcData1),
                  zeroCrossingRate(adcData1),
                  peakToPeakAmplitude(adcData1),
                  spectralCentroid(adcData1),
                  spectralSpread(adcData1),
                  spectralFlatness(adcData1)]
    aC.append(featureSet)

# Create a DataFrame from the feature sets
dfOut = pd.DataFrame(aC, columns=['Mean', 'Variance', 'Standard Deviation', 'Skewness', 'Kurtosis', 
                                  'RootMeanSquare', 'CrestFactor', 'ZeroCrossingRate', 
                                  'PeakToPeakAmplitude', 'SpectralCentroid', 
                                  'SpectralSpread', 'SpectralFlatness'])

# Standardize the features
#scaler = StandardScaler()
#dfOut_scaled = pd.DataFrame(scaler.fit_transform(dfOut), columns=dfOut.columns)

dfOut.to_csv("D:\\Final_Project_Working\\extracted_features2.csv", index=False)
print("Features extracted and saved")
