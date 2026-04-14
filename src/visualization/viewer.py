import cv2
from dataset.utils import draw_bbox
from config import SHOW_BBOX, MAX_FRAMES

def play_video(cap, annotations=None):
    frame_id = 0
    is_single = annotations is not None and len(annotations) <= 1

    first_frame = None
    init_pause_frames = 14
    pause_counter = 0

    while True:
        # Read first frame for single videos
        if is_single and first_frame is None:
            ret, frame = cap.read()
            if not ret:
                break
            first_frame = frame.copy()

        # INIT phase (pause)
        if is_single and pause_counter < init_pause_frames:
            frame = first_frame.copy()
            pause_counter += 1
            label = "INIT"

            # Draw bbox ONLY here
            if annotations and SHOW_BBOX and len(annotations) == 1:
                frame = draw_bbox(frame, annotations[0])

        else:
            # 🔹 Normal playback
            ret, frame = cap.read()
            if not ret:
                break

            label = "SINGLE" if is_single else "MULTI"

            # Draw bbox ONLY for multi videos
            if (not is_single) and annotations and SHOW_BBOX:
                if frame_id < len(annotations):
                    frame = draw_bbox(frame, annotations[frame_id])

        # Label
        cv2.putText(frame, label, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Video", frame)

        key = cv2.waitKey(30)
        if key == 27:
            break

        # Update frame_id only during real playback
        if not (is_single and pause_counter <= init_pause_frames):
            frame_id += 1
            if MAX_FRAMES and frame_id >= MAX_FRAMES:
                break

    cap.release()
    cv2.destroyAllWindows()