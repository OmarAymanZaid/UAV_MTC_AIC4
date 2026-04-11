import cv2
from dataset.utils import draw_bbox
from config import SHOW_BBOX, MAX_FRAMES

def play_video(cap, annotations=None):
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if annotations and frame_id < len(annotations):
            if SHOW_BBOX:
                frame = draw_bbox(frame, annotations[frame_id])

        cv2.imshow("Video", frame)

        key = cv2.waitKey(30)
        if key == 27:  # ESC
            break

        frame_id += 1

        if MAX_FRAMES and frame_id >= MAX_FRAMES:
            break

    cap.release()
    cv2.destroyAllWindows()