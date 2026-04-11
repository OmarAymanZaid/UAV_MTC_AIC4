def parse_annotation_file(file_path):
    """
    Reads annotation file.
    Returns list of bounding boxes: [(x, y, w, h), ...]
    """
    boxes = []

    with open(file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            x, y, w, h = map(float, parts)
            boxes.append((x, y, w, h))

    return boxes