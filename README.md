# Characterization of Wrist Pulse using Machine Learning Techniques  

## 📌 Project Overview  
This project focuses on analyzing wrist pulse data using machine learning techniques to classify individuals into **normal, diabetic, or hypertensive** categories. A prototype was developed using **Raspberry Pi and IoT technology**, allowing remote monitoring via a mobile device.  

## 🛠️ Technologies Used  
- **Hardware:** Pulse sensor, Raspberry Pi  
- **Software & Libraries:** Python, NumPy, Pandas, Scikit-learn, Matplotlib  
- **Machine Learning Algorithms:** Random Forest, XGBoost, SVM  
- **Signal Processing:** Feature extraction from wrist pulse data  
- **IoT Integration:** Remote control via mobile device  

## 🔧 How It Works  
1. **Data Collection:** Wrist pulse signals are captured using a pulse sensor.  
2. **Feature Extraction:** Signal processing techniques are applied to extract meaningful features.  
3. **Classification:** Machine learning algorithms classify the pulse patterns.  
4. **IoT Integration:** The system can be controlled remotely using a connected mobile device.  

## The dataset used for training is shared as 'normalised_data.csv'

## Codes for the process of Data Collection, Feature Extraction, Classification are given in the folder "Process"

## Codes for training the ML models are given in the folder "Models"

## Steps to Connect Raspberry Pi to a new Wifi/Mobile Hotspot:
1) Connect the SD card in the Raspberry Pi to your PC using a card reader.
2) Open the file "wpa_supplicant.cnf".
3) There will be a few Wifi details already stored in that file, similarly enter your ssid and passkey after them.
4) Save the file and recheck if the changes you have done is saved correctly.
5) Connect the SD card back to Raspberry Pi.

## Steps to access Raspberry Pi from your PC via a VNC viewer:
1) Download RealVNC viewer (Windows version or MAC) using the link "https://www.realvnc.com/en/connect/download/viewer" and install the application in your PC.
2) Connect your PC to the same Wifi as your Raspberry Pi is connected to.
3) Check the Gateway for the Wifi you have connected, mostly in the form of "192.168.X.Y", here the "X" is the value you have to note.
4) Open the RealVNC application and connect to the IP "192.168.X.86" (here the X is the value you noted before). The value of "Y" is always "86" as for Raspberry Pi.
5) Enter the user ID "Sree" and password "".

## Steps to Trigger Raspberry Pi for Project Output:
1) Connect a device (PC or Mobile Phone) to the same network (Wifi) as your Raspberry Pi.
2) Open a Browser and type the address "http://192.168.X.86:5000//trigger" (You can always find the value of X from the Gatewaye address of your Wifi).
3) Enter the details ans Submit and the output will be displayed.
