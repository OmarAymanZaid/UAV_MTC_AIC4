from core.manifest import Manifest
from core.dataloader import DataLoader
from config import DATASET_ROOT, MANIFEST_PATH


def main():
    manifest = Manifest(DATASET_ROOT, MANIFEST_PATH)

    print(f"Train sequences: {len(manifest.get_train_sequences())}")
    print(f"Public sequences: {len(manifest.get_public_sequences())}")

    #  Work only on train for now
    loader = DataLoader(manifest.get_train_sequences())

    sample = loader[0]

    print("\nSample:")
    print("Name:", sample["name"])
    print("Frames:", sample["n_frames"])
    print("Annotations:", len(sample["annotations"]))

if __name__ == "__main__":
    main()