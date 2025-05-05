
# Finger Counter

A Python project that uses computer vision to detect and count the number of fingers held up in front of a webcam. It leverages OpenCV for video capture and Mediapipe for hand tracking to count fingers on one or both hands in real-time.

## Features
- Detects up to two hands simultaneously.
- Counts raised fingers (0–10) across both hands.
- Displays the total finger count on the video feed.
- Supports both left and right hands with adjusted thumb detection logic.

## Prerequisites
- Python 3.8 or higher
- A webcam connected to your computer
- macOS, Windows, or Linux

## Installation

1. **Clone the repository** (or download the code):
   ```bash
   git clone https://github.com/your-username/finger-counter.git
   cd finger-counter
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv finger_count_env
   source finger_count_env/bin/activate  # On macOS/Linux
   finger_count_env\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install opencv-python mediapipe==0.10.14
   ```

   *Note*: If you encounter issues installing `mediapipe` on macOS, ensure you have build tools installed:
   ```bash
   xcode-select --install
   brew install cmake libpng jpeg
   ```

## Usage

1. **Run the script**:
   ```bash
   python finger_counter.py
   ```

2. **Interact with the program**:
   - Hold one or both hands in front of the webcam.
   - The video feed will display hand landmarks and the total number of raised fingers (e.g., "Total Fingers: 5").
   - Press `q` to exit the program.

3. **Example output**:
   - Raising three fingers on the right hand and two on the left will show: `Total Fingers: 5`.

## Troubleshooting

- **Webcam not working**:
  - Ensure no other application is using the webcam.
  - Test the webcam with another app (e.g., Photo Booth on macOS).
  - Check the camera index in the script (`cv2.VideoCapture(0)`). Try `1` or `2` if `0` fails.

- **Only one hand detected**:
  - Ensure both hands are clearly visible and not overlapping.
  - Keep hands slightly separated in the camera view.

- **Installation issues**:
  - If `mediapipe` installation fails, try an older version:
    ```bash
    pip install mediapipe==0.10.14
    ```
  - On Apple Silicon (M1/M2) Macs, use Rosetta or Conda:
    ```bash
    conda create -n finger_count python=3.10
    conda activate finger_count
    conda install opencv
    pip install mediapipe==0.10.14
    ```

- **Inaccurate finger counting**:
  - Ensure good lighting and clear hand visibility.
  - Adjust `min_detection_confidence` in `finger_counter.py` (e.g., to `0.5`) for better detection.

## Project Structure
```
finger-counter/
├── finger_counter.py  # Main script for finger counting
├── README.md         # Project documentation
└── finger_count_env/ # Virtual environment (if created)
```

## Contributing
Feel free to open issues or submit pull requests for improvements, such as:
- Displaying separate counts for each hand.
- Adding support for specific gestures.
- Integrating with hardware (e.g., motors) based on finger count.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built using [OpenCV](https://opencv.org/) and [Mediapipe](https://mediapipe.dev/).
- Inspired by real-time computer vision applications.
