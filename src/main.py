from dataset.loader import UAVDataset
from visualization.viewer import play_video
from config import DATASET_ROOT

def main():
    dataset = UAVDataset(DATASET_ROOT)

    print(f"Found {len(dataset)} videos")

    for i in range(len(dataset)):
        print(f"\nPlaying video {i+1}/{len(dataset)}")

        cap, annotations, folder = dataset.get_video(i)

        print(f"Folder: {folder}")
        print(f"Annotations: {len(annotations)} frames")

        play_video(cap, annotations)

if __name__ == "__main__":
    main()