# 🦖 Gesture Dino - Hand Gesture Game Controller

Control the Chrome Dino game using hand gestures through your webcam! This project uses computer vision and hand tracking to detect peace signs and make the dino jump.

## ✨ Features

- 🎮 **Real-time hand gesture recognition** using MediaPipe
- ✌️ **Peace sign detection** to trigger dino jumps
- 📹 **Webcam integration** with OpenCV
- 🎯 **Low latency** gesture detection (120ms cooldown)
- 🖥️ **Cross-platform** support (Windows, macOS, Linux)
- 🎨 **Visual feedback** with on-screen status display

## 🛠️ Technologies Used

- **Python 3.11+**
- **OpenCV** - Computer vision and camera handling
- **MediaPipe (cvzone)** - Hand tracking and gesture recognition
- **Windows API (directkeys)** - Keyboard simulation for game control

## 📋 Requirements

- Python 3.11 or higher
- Webcam/Camera device
- Windows OS (for keyboard simulation)

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/torikkyun/gesture-dino.git
cd gesture-dino
```

2. **Install dependencies using uv**

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

## 🎮 How to Use

### Step 1: Open the Dino Game

1. Open your web browser
2. Go to [Chrome Dino Game](https://chromedino.com/) or type `chrome://dino/` in Chrome
3. Make sure the game is in focus and ready to start

### Step 2: Run the Gesture Controller

```bash
uv run main.py
```

### Step 3: Position Your Hand

- Sit in front of your camera with good lighting
- Keep your hand visible in the camera frame
- Maintain a distance of about 30-60cm from the camera

### Step 4: Control the Game

- **✌️ Peace Sign**: Make dino jump (Space key)
  - Raise your **index finger** and **middle finger**
  - Keep **thumb**, **ring finger**, and **pinky** down
  - Hold the gesture for at least 120ms
- **Other gestures**: Dino stays on ground

### Step 5: Exit

- Press `q` key in the camera window to quit

## 🎯 Gesture Guide

| Gesture       | Action | Description                           |
| ------------- | ------ | ------------------------------------- |
| ✌️ Peace Sign | Jump   | Index + Middle finger up, others down |
| 👊 Fist/Other | Stay   | Any other hand position               |
| 🚫 No Hand    | Stay   | No hand detected in frame             |

## 🔧 Configuration

You can modify these settings in `main.py`:

```python
# Detection settings
detectionCon=0.8        # Hand detection confidence (0.0-1.0)
maxHands=1              # Maximum hands to detect

# Timing settings
action_cooldown = 0.12  # Minimum time between jumps (seconds)

# Camera settings
frame_width = 640       # Camera resolution width
frame_height = 480      # Camera resolution height
```

## 📁 Project Structure

```
gesture-dino/
├── main.py              # Main application file
├── directkeys.py        # Windows keyboard simulation
├── requirements.txt     # Python dependencies
├── .editorconfig       # Code formatting configuration
└── README.md           # Project documentation
```

## 🐛 Troubleshooting

### Camera Issues

- **Error: "Cannot open camera!"**
  - Make sure no other application is using the camera
  - Try running as administrator
  - Check if camera is properly connected

### Performance Issues

- **Laggy detection:**
  - Ensure good lighting conditions
  - Close unnecessary applications
  - Lower camera resolution if needed

### Gesture Not Detected

- **Peace sign not working:**
  - Make sure fingers are clearly separated
  - Check hand is well-lit and visible
  - Maintain steady hand position
  - Ensure proper distance from camera

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MediaPipe** team for the excellent hand tracking library
- **OpenCV** community for computer vision tools
- **Chrome Dino Game** for providing the perfect test game

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Make sure your environment meets the requirements

---

**Happy Gaming! 🎮✌️**
