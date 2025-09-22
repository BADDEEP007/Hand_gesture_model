# Gesture-Controlled Smart Home Automation System

A real-time gesture recognition system that allows you to control various smart home devices and computer functions using hand gestures captured through your webcam.

## 🚀 Features

### Gesture Controls
- **👍 Thumb Up**: Turn on bulb / Increase screen brightness
- **👎 Thumb Down**: Turn off bulb / Decrease screen brightness  
- **✊ Closed Fist**: Turn on fan / Decrease volume
- **✋ Open Palm**: Turn off fan / Open screenshot
- **✌️ Victory**: Turn on music / Take screenshot
- **☝️ Pointing Up**: Turn off music / Increase volume
- **🤟 I Love You**: Shutdown system

### Smart Home Simulation
- Visual GUI interface showing device states
- Real-time device control feedback
- Bulb, Fan, and Music system controls

### System Controls
- Volume control (increase/decrease)
- Screen brightness adjustment
- Screenshot capture and viewing
- Text-to-speech announcements

## 🛠️ Technologies Used

- **Computer Vision**: OpenCV, MediaPipe
- **GUI Framework**: Tkinter
- **Audio Control**: pycaw (Windows Audio API)
- **System Control**: screen-brightness-control, pyautogui
- **Text-to-Speech**: pyttsx3
- **Machine Learning**: MediaPipe Gesture Recognition Model

## 📋 Requirements

```
opencv-python
mediapipe
tkinter (usually comes with Python)
pycaw
screen-brightness-control
pyautogui
pyttsx3
```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/BADDEEP007/Hand_gesture_model.git
cd gesture-controlled-smart-home
```

2. **Install required packages**
```bash
pip install opencv-python mediapipe pycaw screen-brightness-control pyautogui pyttsx3
```


## 🚀 Usage

### Main Application (with GUI)
```bash
python main_control.py
```
This launches the full application with:
- Smart home GUI interface
- Real-time gesture recognition
- Device control simulation

### Demo Version (System Controls)
```bash
python main_home_automation_demo.py
```
This runs the demo version with:
- System volume and brightness control
- Screenshot functionality
- Voice announcements

### GUI Only
```bash
python smarthomegui.py
```
Launches just the smart home interface for testing.

## 🎯 How It Works

1. **Camera Input**: The system captures video from your default webcam
2. **Gesture Detection**: MediaPipe processes each frame to detect hand gestures
3. **Action Mapping**: Recognized gestures are mapped to specific actions
4. **Device Control**: Actions are executed on simulated smart home devices or system controls
5. **Visual Feedback**: The GUI updates to show current device states

## 📁 Project Structure

```
├── main_control.py              # Main application with GUI integration
├── main_home_automation_demo.py # Demo version with system controls
├── smarthomegui.py             # Smart home GUI interface
├── gesture_recognizer.task     # MediaPipe gesture recognition model
└── README.md                   # Project documentation
```

## 🔧 Configuration

### Model Path Setup
Update the `MODEL_PATH` variable in your chosen main file:
```python
MODEL_PATH = "path/to/your/gesture_recognizer.task"
```

### Camera Settings
The system uses the default camera (index 0). To use a different camera:
```python
self.cap = cv2.VideoCapture(1)  # Change index as needed
```

## 🎮 Controls

- **Press 'q'**: Quit the application
- **Webcam Window**: Shows live feed with gesture recognition
- **GUI Window**: Displays smart home device states

## 🔍 Troubleshooting

### Common Issues

1. **Camera not detected**
   - Ensure your webcam is connected and not being used by another application
   - Try changing the camera index in `cv2.VideoCapture(0)`

2. **Model file not found**
   - Download the MediaPipe gesture recognition model
   - Update the `MODEL_PATH` variable with the correct file path

3. **Audio control not working**
   - Ensure you're running on Windows (pycaw is Windows-specific)
   - Run the application with administrator privileges if needed

4. **Brightness control issues**
   - Some systems may not support programmatic brightness control
   - Try running with administrator privileges

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- MediaPipe team for the gesture recognition model
- OpenCV community for computer vision tools
- Python community for the amazing libraries

## 📧 Contact

[Pradeep Argal] - [Pradeepargal22@gmail.com]



---

**Note**: This project is designed for Windows systems due to the pycaw dependency for audio control. For cross-platform compatibility, consider using alternative audio control libraries.