import cv2
import pytesseract

# Specify the path to tesseract executable 
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Load the image 
img = cv2.imread("C:\\Users\\Acer\\Desktop\\sampletext.png")

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract the text data from image 
text = pytesseract.image_to_string(img_gray)

# Print the extracted text
print(text)

