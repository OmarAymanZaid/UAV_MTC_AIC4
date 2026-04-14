import cv2

class Sequence:
    def __init__(self, name, video_path, annotation_path, n_frames):
        self.name = name
        self.video_path = video_path
        self.annotation_path = annotation_path
        self.n_frames = n_frames

    def load_video(self):
        return cv2.VideoCapture(self.video_path)

    def has_annotations(self):
        return self.annotation_path is not None