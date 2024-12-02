import cv2
import numpy as np

# Function to add salt and pepper noise
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size
    
    # Salt noise (white)
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy_image[salt_coords[0], salt_coords[1]] = 255  # Salt

    # Pepper noise (black)
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0  # Pepper

    return noisy_image

# Read the image
image_path = r"C:\Users\aysha\OneDrive\Desktop\Miniproject\image.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Resize the image for better display (reduce size by 50%)
scale_percent = 50  # Resize factor
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Add salt and pepper noise to the image
salt_prob = 0.01  # 1% salt noise
pepper_prob = 0.01  # 1% pepper noise
noisy_image = add_salt_and_pepper_noise(resized_image, salt_prob, pepper_prob)

# Remove the salt and pepper noise using median filtering
denoised_image = cv2.medianBlur(noisy_image, 5)  # Kernel size of 5x5

# Display the images
cv2.imshow("Original Image", resized_image)
cv2.imshow("Noisy Image (Salt and Pepper)", noisy_image)
cv2.imshow("Denoised Image (Median Filter)", denoised_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
