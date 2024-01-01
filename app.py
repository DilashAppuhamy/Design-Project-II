import cv2
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model('E:\\Sliit\\3rd yr 2nd sem\\DP2\\model')

# Labels
labels = ['screws', 'nuts', 'washers']

# Initialize webcam  
cap = cv2.VideoCapture(0)

while True:
    # Capture & resize frame
    ret, frame = cap.read()
    img = cv2.resize(frame, (64, 64))
    
    # Preprocess
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    # Classify 
    pred = model.predict(img)
    i = np.argmax(pred)
    
    # Set a threshold for classification
    threshold = 0.75  # Adjust the threshold as needed
    
    # Display the result based on the predicted class or "No object detected"
    if pred[0, i] >= threshold:
        item = labels[i]
    else:
        item = "No object detected"
    
    # Overlay text 
    cv2.putText(frame, item, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    
    # Display 
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources        
cap.release()
cv2.destroyAllWindows()



# import cv2
# import numpy as np
# import tensorflow as tf

# # Load model
# model = tf.keras.models.load_model('E:\\Sliit\\3rd yr 2nd sem\\DP2\\model')


# # Labels
# labels = ['screws','nuts','washers']

# # Initialize webcam  
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture & resize frame
#     ret, frame = cap.read()
#     img = cv2.resize(frame, (64,64))
    
#     # Preprocess
#     img = img/255.0
#     img = np.expand_dims(img, axis=0)
    
#     # Classify 
#     pred = model.predict(img)
#     i = np.argmax(pred)
#     item = labels[i]
    
#     # Overlay text 
#     cv2.putText(frame, item, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
    
#     # Display 
#     cv2.imshow('frame',frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     # time.sleep(2)
        
# # Release resources        
# cap.release()
# cv2.destroyAllWindows()

