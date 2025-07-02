import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey, space_pressed
import time


class DinoHandController_Peace:
    def __init__(self):
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)
        self.space_key = space_pressed

        self.is_jumping = False
        self.last_action_time = 0
        self.action_cooldown = 0.1

        print("Initializing camera...")
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not self.video.isOpened():
            print("Trying different camera index...")
            self.video = cv2.VideoCapture(1)

        if not self.video.isOpened():
            raise Exception("Cannot open camera!")

        self.setup_camera()

    def setup_camera(self):
        print("Configuring camera...")
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        print("Camera OK!")

    def process_hand_gesture(self, hands):
        if not hands:
            if self.is_jumping:
                self.release_jump()
            return "NO HANDS", (0, 0, 255)

        current_time = time.time()
        fingers = self.detector.fingersUp(hands[0])

        index_finger = fingers[1] == 1
        middle_finger = fingers[2] == 1
        thumb = fingers[0] == 0
        ring_finger = fingers[3] == 0
        pinky = fingers[4] == 0

        is_peace_sign = (
            index_finger and middle_finger and thumb and ring_finger and pinky
        )

        if is_peace_sign:
            if (
                not self.is_jumping
                and current_time - self.last_action_time > self.action_cooldown
            ):
                self.trigger_jump()
                self.last_action_time = current_time
            return "PEACE - JUMP!", (0, 255, 0)
        else:
            if self.is_jumping:
                self.release_jump()
            finger_count = sum(fingers)
            return f"READY ({finger_count} FINGERS)", (255, 165, 0)

    def trigger_jump(self):
        PressKey(self.space_key)
        self.is_jumping = True

    def release_jump(self):
        ReleaseKey(self.space_key)
        self.is_jumping = False

    def run(self):
        print("🦖 Dino Hand Controller - PEACE MODE")
        print("=" * 50)
        print("✌️  GESTURE: PEACE SIGN ONLY")
        print("📝 How to:")
        print("   - Raise INDEX FINGER + MIDDLE FINGER")
        print("   - Lower THUMB + RING FINGER + PINKY")
        print("   - Hold steady for 0.12 seconds")
        print("   - Like when taking a photo ✌️")
        print("🚪 Press 'q' to exit")
        print("=" * 50)

        time.sleep(2)
        frame_count = 0

        while True:
            ret, frame = self.video.read()
            if not ret:
                print("Camera error!")
                time.sleep(0.1)
                continue

            frame_count += 1
            frame = cv2.flip(frame, 1)
            hands, img = self.detector.findHands(frame, draw=True)
            status, color = self.process_hand_gesture(hands)
            self.draw_simple_ui(img, status, color, frame_count)
            cv2.imshow("Dino Control - PEACE", img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cleanup()

    def draw_simple_ui(self, img, status, color, frame_count):
        h, w = img.shape[:2]

        cv2.rectangle(img, (10, 10), (w - 10, 120), (0, 0, 0), -1)
        cv2.rectangle(img, (10, 10), (w - 10, 120), color, 3)

        cv2.putText(
            img, status, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3
        )

        cv2.putText(
            img,
            "Peace sign: Raise index + middle finger",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1,
        )

        cv2.putText(
            img,
            "Lower other fingers down",
            (20, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1,
        )

        cv2.putText(
            img,
            f"Frame: {frame_count}",
            (w - 150, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1,
        )

    def cleanup(self):
        if self.is_jumping:
            self.release_jump()
        self.video.release()
        cv2.destroyAllWindows()
        print("👋 Exited!")


if __name__ == "__main__":
    try:
        controller = DinoHandController_Peace()
        controller.run()
    except Exception as e:
        print(f"Error: {e}")
        print("Please try:")
        print("1. Close apps using camera")
        print("2. Run test_camera.py")
        print("3. Try main.py instead of this version")
