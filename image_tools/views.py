from django.http import FileResponse
from django.shortcuts import render

from .services import process_image


TOOLS = [
    {
        "id": "grayscale",
        "name": "Grayscale",
        "description": "Turn a color image into black and white.",
    },
    {
        "id": "remove_background",
        "name": "Remove background",
        "description": "Cut out the subject and return a transparent PNG.",
    },
    {
        "id": "blur",
        "name": "Blur",
        "description": "Soften an image with a blur slider.",
    },
    {
        "id": "jpeg_to_png",
        "name": "JPEG to PNG",
        "description": "Convert a JPEG upload into a PNG file.",
    },
    {
        "id": "compress_webp",
        "name": "Compress to WebP",
        "description": "Make a smaller WebP copy of your image.",
    },
]


def home(request):
    context = {"tools": TOOLS, "selected_tool": "grayscale"}

    if request.method == "POST":
        selected_tool = request.POST.get("tool", "grayscale")
        context["selected_tool"] = selected_tool
        uploaded_file = request.FILES.get("image")

        if not uploaded_file:
            context["error"] = "Upload an image first."
            return render(request, "image_tools/home.html", context)

        try:
            output, filename, content_type = process_image(
                uploaded_file,
                selected_tool,
                blur_radius=request.POST.get("blur_radius", 3),
                webp_quality=request.POST.get("webp_quality", 80),
            )
        except ValueError as e:
            context["error"] = str(e)
            return render(request, "image_tools/home.html", context)

        return FileResponse(output, as_attachment=True, filename=filename, content_type=content_type)

    return render(request, "image_tools/home.html", context)