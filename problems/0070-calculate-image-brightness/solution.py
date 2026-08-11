def calculate_brightness(img: list[list[int]]) -> float | int:
    if not img or not img[0]:
        return -1

    first_len = len(img[0])
    flat = [pixel for row in img for pixel in row]

    # Validate row lengths and pixel ranges
    if any(len(row) != first_len for row in img) or any(
        p < 0 or p > 255 for p in flat
    ):
        return -1

    return round(sum(flat) / len(flat), 2)