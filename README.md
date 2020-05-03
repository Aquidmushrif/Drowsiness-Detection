# Drowsiness-Detection
Today drowsy driving is a serious problem that leads to thousands of accidents each year. Drowsiness or fatigue of a driver is the major reason for these road accidents in India, no monitoring device is used to measure the drowsiness of driver. There is a need for a system that can overcome this problem, a system to monitor driver fatigue and give an alert feedback.<br/>
<br/>
<br/>
The main purpose of the project is to detect such conditions where the driver is drowsy and not in the state of driving the vehicle and alert him about his condition, so that he can stop the driving and will take some rest. The main objective of this project is to reduce the accidents happening due the drowsiness or the fatigue of the driver.
<br/>
<br/>
<br/>
#Please download the pretrained model(shape_predictor_68_face_landmarks.dat) from this repo :https://github.com/davisking/dlib-models.<br/>
<br/>
<i>(C. Sagonas, E. Antonakos, G, Tzimiropoulos, S. Zafeiriou, M. Pantic. 
300 faces In-the-wild challenge: Database and results. 
Image and Vision Computing (IMAVIS), Special Issue on Facial Landmark Localisation "In-The-Wild". 2016.)</i>
<br/>
<br/>
<br/>
<b>Requirements:</b><br/>
-NUMPY<br/>
-OPENCV<br/>
-SCIKIT<br/>
-DLIB<br/>
<br/>
<br/>
<i>Instructions: Execute detect_drowsiness.py. (Runtime arguments for webcam and video input are present inside the file)</i>
<br/>
<br/>
<h2> This Project uses EAR (Eye Aspect Ratio) to detect drivers Drowsiness. </h2>
<br/>
<h3><b><i>When Eyes are not visible due to glasses or due to any other reason the EAR is indeterminable we have a module called Yawn Detector which captures the duration and frequency of yawning of the driver to check the drowsiness of the driver.</i></b></h3>
<br/>
<h4><i>The Yawn Detector module is still in development and hence not perfect</i></h4>

