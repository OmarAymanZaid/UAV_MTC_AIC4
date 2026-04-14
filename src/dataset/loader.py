import os
import cv2
from .parser import parse_annotation_file

class UAVDataset:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.videos = self._scan_dataset()

    def _scan_dataset(self):
        """
        Finds all video folders.
        """
        video_folders = []

        for sub_dataset in os.listdir(self.root_dir):
            sub_path = os.path.join(self.root_dir, sub_dataset)

            if not os.path.isdir(sub_path):
                continue

            for video_folder in os.listdir(sub_path):
                video_path = os.path.join(sub_path, video_folder)

                if os.path.isdir(video_path):
                    video_folders.append(video_path)

        return video_folders

    def __len__(self):
        return len(self.videos)

    def get_video(self, index):
        """
        Returns:
        - video capture
        - annotations
        - folder
        """
        folder = self.videos[index]

        video_file = None
        annotation_file = None

        for file in os.listdir(folder):
            if file.endswith(".mp4") or file.endswith(".avi"):
                video_file = os.path.join(folder, file)
            elif file.endswith(".txt"):
                annotation_file = os.path.join(folder, file)

        if video_file is None:
            raise Exception(f"No video found in {folder}")

        annotations = []
        if annotation_file:
            annotations = parse_annotation_file(annotation_file)

        cap = cv2.VideoCapture(video_file)

        return cap, annotations, folder