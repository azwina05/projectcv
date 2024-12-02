import cv2

# Read the image
image = cv2.imread(r"C:\Users\aysha\OneDrive\Desktop\Miniproject\image.png")  # Update the path
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Convert the image into grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image into a black and white (binary) image
_, bw_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the black and white image
cv2.imshow("Black and White Image", bw_image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window
