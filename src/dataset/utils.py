import cv2

def xywh_to_xyxy(box):
    x, y, w, h = box
    return int(x), int(y), int(x + w), int(y + h)

def draw_bbox(frame, box, color=(0, 255, 0)):
    x1, y1, x2, y2 = xywh_to_xyxy(box)
    return cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)