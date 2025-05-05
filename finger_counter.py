import cv2
import mediapipe as mp

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=4, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Start webcam capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to read frame")
        break

    # Flip the frame horizontally for a selfie-view display
    frame = cv2.flip(frame, 1)
    # Convert the BGR image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(frame_rgb)

    # Initialize total finger count
    total_finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            landmarks = hand_landmarks.landmark

            # Finger tip and pip indices (thumb, index, middle, ring, pinky)
            finger_tips = [4, 8, 12, 16, 20]  # Tip landmarks
            finger_pips = [3, 6, 10, 14, 18]  # PIP joint landmarks

            # Count raised fingers for this hand (excluding thumb)
            finger_count = 0
            for tip, pip in zip(finger_tips[1:], finger_pips[1:]):
                if landmarks[tip].y < landmarks[pip].y:  # Tip above PIP means finger is raised
                    finger_count += 1

            # Special case for thumb: check if thumb tip is to the left or right of its IP joint
            # Adjust for hand orientation using handedness if available
            if results.multi_handedness:
                hand_label = results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)].classification[0].label
                if hand_label == "Right":
                    if landmarks[4].x < landmarks[2].x:  # Thumb tip left of IP joint
                        finger_count += 1
                else:  # Left hand
                    if landmarks[4].x > landmarks[2].x:  # Thumb tip right of IP joint
                        finger_count += 1
            else:
                # Fallback if handedness not detected
                if landmarks[4].x < landmarks[2].x:
                    finger_count += 1

            total_finger_count += finger_count

    # Display total finger count on the frame
    cv2.putText(frame, f'Total Fingers: {total_finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Finger Counter', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()