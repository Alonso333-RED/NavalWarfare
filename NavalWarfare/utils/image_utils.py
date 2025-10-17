import os
from PIL import Image
from utils import storage_utils

def color_splash(location: str, red: int = 0, green: int = 0, blue: int = 0, 
                 strength: float = 0.5, new_name: str = None) -> Image.Image:

    original_image_path = storage_utils.get_relative_path(location)
    img = Image.open(original_image_path).convert("RGBA")
    image_name = os.path.basename(original_image_path)

    r, g, b, a = img.split()
    r = r.point(lambda i: int(i * (1 - strength) + red * strength))
    g = g.point(lambda i: int(i * (1 - strength) + green * strength))
    b = b.point(lambda i: int(i * (1 - strength) + blue * strength))

    tinted = Image.merge("RGBA", (r, g, b, a))

    if new_name is None:
        output_name = f"{os.path.splitext(image_name)[0]}_tinted.png"
    else:
        output_name = new_name if new_name.lower().endswith(".png") else f"{new_name}.png"

    output_path = os.path.join(os.path.dirname(original_image_path), output_name)

    tinted.save(output_path)
    print(f"Tinted image saved as {output_name}")

    return tinted
