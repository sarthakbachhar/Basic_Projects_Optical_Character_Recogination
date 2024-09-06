# Optical Character Recognition (OCR) with Tesseract and OpenCV

This project extracts text from images using OpenCV and Tesseract OCR.

## Requirements

- Python 3.x
- OpenCV
- Tesseract-OCR
- pytesseract

## Installation

1. **Install Python Packages**:
   Install OpenCV and pytesseract using pip:
   ```bash
   pip install opencv-python pytesseract
   
2. **Install Tesseract-OCR**: Download and install Tesseract.

3. **Set Tesseract Path**: Update the script with the path to your Tesseract executable:
   ```bash
   pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

## Usage

1. Place your image in the specified path within the script.
2. Run the script to extract text from the image:
   ```bash
   python your_script_name.py

## Features

* Converts images to grayscale before text extraction.
* Uses Tesseract-OCR to recognize text from images.
* Prints the extracted text to the console.
  
## License
This project is licensed under the MIT License.
