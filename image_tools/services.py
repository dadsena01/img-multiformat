from io import BytesIO
from pathlib import Path
from rembg import remove

from PIL import Image, ImageFilter


OUTPUT_TYPES = {
    "grayscale": ("PNG", "png", "image/png"),
    "remove_background": ("PNG", "png", "image/png"),
    "blur": ("PNG", "png", "image/png"),
    "jpeg_to_png": ("PNG", "png", "image/png"),
    "compress_webp": ("WEBP", "webp", "image/webp"),
}


def process_image(uploaded_file, tool, blur_radius=3, webp_quality=80):
    if tool not in OUTPUT_TYPES:
        raise ValueError("Choose a valid tool.")

    image = Image.open(uploaded_file)
    original_name = Path(uploaded_file.name).stem or "image"

    if tool == "grayscale":
        image = image.convert("L")
    elif tool == "remove_background":
        image = remove_background(uploaded_file)
    elif tool == "blur":
        radius = clamp_number(blur_radius, minimum=0, maximum=25)
        image = image.convert("RGB").filter(ImageFilter.GaussianBlur(radius=radius))
    elif tool == "jpeg_to_png":
        if image.format not in {"JPEG", "JPG"}:
            raise ValueError("Upload a JPEG image for JPEG to PNG conversion.")
        image = image.convert("RGBA")
    elif tool == "compress_webp":
        image = image.convert("RGB")

    output_format, extension, content_type = OUTPUT_TYPES[tool]
    output = BytesIO()
    save_kwargs = {}

    if tool == "compress_webp":
        save_kwargs["quality"] = clamp_number(webp_quality, minimum=1, maximum=100)
        save_kwargs["method"] = 6

    image.save(output, format=output_format, **save_kwargs)
    output.seek(0)
    return output, f"{original_name}-{tool}.{extension}", content_type


def remove_background(uploaded_file):
    uploaded_file.seek(0)
    result = remove(uploaded_file.read())
    return Image.open(BytesIO(result)).convert("RGBA")


def clamp_number(value, minimum, maximum):
    number = int(value)
    return max(minimum, min(maximum, number))
