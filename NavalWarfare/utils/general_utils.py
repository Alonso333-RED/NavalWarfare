import random
import os

def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_project_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(current_dir))
    return project_dir

def get_relative_path(*path_segments):
    project_dir = get_project_path()
    return os.path.join(project_dir, *path_segments)

def get_images(folder):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    images = []

    for file in os.listdir(folder):
        if any(file.lower().endswith(ext) for ext in allowed_extensions):
            images.append(os.path.join(folder, file))

    return images

def get_random_image(folder):
    full_folder_path = get_relative_path(folder)
    
    images = get_images(full_folder_path)
    
    if images:
        return random.choice(images)
    else:
        return None
