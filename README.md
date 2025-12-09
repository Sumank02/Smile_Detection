__Smile Detection using Haar Cascade__

This project demonstrates a simple and efficient smile detection system using OpenCV’s Haar Cascade Classifier.
It detects faces and checks whether a smile is present in an image using the provided pre-trained cascade file.


Project Structure
```
Smile_Detection/
│
├── haarcascade_smile.xml     # Pretrained Haar cascade for smile detection
├── mk-4.png                  # Sample test image
├── project_2.py              # Main Python script for smile detection
└── README.md                 # Project documentation
```


🧠 Overview
This project uses OpenCV’s CascadeClassifier along with detectMultiScale() to detect smiles in an input image.

What the script does:

- Loads required libraries
- Loads the smile Haar Cascade file
- Reads the input image (e.g., mk-4.png)
- Converts the image to grayscale (required for Haar cascade)
- Applies detectMultiScale to find smile regions
- Draws rectangles around detected smiles
- Displays the final output window
- This project is part of a mini computer-vision practice series.


📦 Requirements

Only one library is required:
    opencv-python

Install it using:
    pip install opencv-python


🔧 Important Parameters

Inside the Haar detection function:
- scaleFactor → adjusts how aggressively the cascade scales
- minNeighbors → higher values reduce false positives
Adjusting these improves detection accuracy depending on image quality.


📌 Notes
- The project does not include any ML model training
- No external dataset is used
- Everything works offline with OpenCV + Haar cascade
- Smile detection accuracy depends on lighting, face angle, and image resolution

❓ Facing Issues?
Feel free to raise an issue in the repo or ask for help.
