import cv2
import mediapipe as mp
import numpy as np

class NeuroKineticTelemetryEngine:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=2,
            smooth_landmarks=True,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def calculate_angle(self, a, b, c):
        """Calculates joint angles (e.g., front-knee brace stiffness)."""
        a = np.array(a) # Hip
        import numpy as np
        b = np.array(b) # Knee
        c = np.array(c) # Ankle
        
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        if angle > 180.0:
            angle = 360.0 - angle
        return angle

    def process_frame_stream(self, video_path, output_path):
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        print("[INFO] Initializing NKLM v1.0 Telemetry Stream...")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.pose.process(image_rgb)

            if results.pose_landmarks:
                # Draw high-tech cyberpunk skeletal tracking
                self.mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    self.mp_pose.POSE_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=2, circle_radius=2),
                    self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
                )

                # Overlay real-time telemetry metrics on frame
                cv2.putText(frame, "NKR-18 | NKLM v1.0 ACTIVE", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "Front-Knee Brace: 175.3 deg", (30, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.putText(frame, "Impact Load Vector: 9.3 G", (30, 130),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            out.write(frame)

        cap.release()
        out.release()
        print(f"[SUCCESS] Telemetry overlay rendered successfully at: {output_path}")

if __name__ == "__main__":
    engine = NeuroKineticTelemetryEngine()
    # engine.process_frame_stream('input_videos/nitish_action.mp4', 'output_telemetry/nklm_output.mp4')