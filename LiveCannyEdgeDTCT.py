import cv2

# Create a VideoCapture object to capture video from the camera
video_capture = cv2.VideoCapture(0)  # ncamera device

# Check if the camera device opened successfully
if not video_capture.isOpened():
    print("Error: Unable to open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = video_capture.read()
    
    # Check if the frame was read successfully
    if not ret:
        break
    
    # Convert to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Blur the frame for better edge detection
    frame_blur = cv2.GaussianBlur(frame_gray, (5, 5), 0)  
    """Gaussian blur with a kernel size of (5, 5)
    mayor kernel = menor ruido
    menor kernel = guarda mayor frecuencia,  mas ruido
    kernel excesivamente alto = menor detalle"""
    
    # Canny Edge Detection
    edges = cv2.Canny(image=frame_blur, threshold1=50, threshold2=85)  #threshold/valor critico del umbral 
    """El concepto de aplicar thresholds es para dar limites critico a nivel pixel
    lo que este por debajo del t1 se descarta de ser un borde
    lo que este entre t1 y t2 se clasifica como esquinas fragiles o no tan marcadas
    valores por encima de t2 son esquinas fuertes
    si aumentas t1 y t2 el n bordes detectados disminuye, y a la inversa
    mientras mayor la diferencia entre t1 y t2 los bordes son mas gruesos"""

    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    
    # Display the original frame
    cv2.imshow('Original', frame)
    
    # Break the loop if 'space' 
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()

