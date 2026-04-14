import json
import os
from .sequence import Sequence


class Manifest:
    def __init__(self, root_dir, manifest_path):
        self.root_dir = root_dir

        with open(manifest_path, "r") as f:
            self.data = json.load(f)

        self.train = self.data.get("train", {})
        self.public_lb = self.data.get("public_lb", {})

    def get_train_sequences(self):
        return self._build_sequences(self.train)

    def get_public_sequences(self):
        return self._build_sequences(self.public_lb)

    def _build_sequences(self, split_dict):
        sequences = []

        for key, info in split_dict.items():
            video_path = os.path.join(self.root_dir, info["video_path"])

            annotation_path = None
            if info["annotation_path"]:
                annotation_path = os.path.join(self.root_dir, info["annotation_path"])

            seq = Sequence(
                name=key,
                video_path=video_path,
                annotation_path=annotation_path,
                n_frames=info["n_frames"]
            )

            sequences.append(seq)

        return sequences