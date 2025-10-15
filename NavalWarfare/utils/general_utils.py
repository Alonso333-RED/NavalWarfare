import random
import os
import json
from Warship import Warship

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
    
def store_warship(warship: Warship):
    file_name = f"main_content/warships_storage/{warship.name.replace(' ', '_').lower()}.json"
    with open(file_name, "w", encoding="utf-8") as warships_storage:
        json.dump(warship.to_dict(), warships_storage, indent=4, sort_keys=True, ensure_ascii=False)

def load_warship(name: str) -> Warship:
    file_name = f"main_content/warships_storage/{name.replace(' ', '_').lower()}.json"

    if not os.path.exists(file_name):
        raise FileNotFoundError(f"No se encontró el archivo para el barco '{name}'.")
    
    with open(file_name, "r", encoding="utf-8") as warships_storage:
        data = json.load(warships_storage)
    
    return Warship(**data)