from dataset.parser import parse_annotation_file

class DataLoader:
    def __init__(self, sequences):
        self.sequences = sequences

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, idx):
        seq = self.sequences[idx]

        cap = seq.load_video()
        annotations = []
        if seq.has_annotations():
            annotations = parse_annotation_file(seq.annotation_path)

        return {
            "name": seq.name,
            "cap": cap,
            "annotations": annotations,
            "n_frames": seq.n_frames
        }