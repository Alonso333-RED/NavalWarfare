import random
import os
import json
import shutil
import arcade
from utils.image_utils import color_splash
from Warship import Warship

def execute_sound(sound):
    sound_folder_path = get_relative_path("NavalWarfare/sounds")
    if not os.path.exists(sound_folder_path):
        raise FileNotFoundError(f"No se encontró la carpeta de audio.")
    loaded_sound = arcade.load_sound(f"{sound_folder_path}/{sound}")
    arcade.play_sound(loaded_sound)

def load_file(location: str):
    return get_relative_path(location)

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
    warships_storage_dir = get_relative_path("NavalWarfare/main_content/warships_storage")
    warship_dir = os.path.join(warships_storage_dir, warship.name.replace(" ", "_").lower())
    os.makedirs(warship_dir, exist_ok=True)
    file_path = os.path.join(warship_dir, f"{warship.name.replace(' ', '_').lower()}.json")

    base_name = warship.name.replace(" ", "_").lower()
    if warship.default_sprite:
        abs_sprite_path = get_relative_path(warship.default_sprite)
        if os.path.exists(abs_sprite_path):

            default_file_name = f"{base_name}_default.png"
            destination_path = os.path.join(warship_dir, default_file_name)
            shutil.copy2(abs_sprite_path, destination_path)

            project_dir = get_project_path()
            relative_sprite_path = os.path.relpath(destination_path, project_dir)
            warship.default_sprite = relative_sprite_path

            damaged_file_name = f"{base_name}_damaged.png"
            color_splash(location=relative_sprite_path, red=255, new_name=damaged_file_name)
            warship.damaged_sprite = os.path.relpath(
                os.path.join(warship_dir, damaged_file_name),
                project_dir
            )

            repaired_file_name = f"{base_name}_repaired.png"
            color_splash(location=relative_sprite_path, green=255, new_name=repaired_file_name)
            warship.repaired_sprite = os.path.relpath(
                os.path.join(warship_dir, repaired_file_name),
                project_dir
            )

        else:
            print(f"ERROR: No se encontró la imagen default_sprite: {abs_sprite_path}")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            warship.to_dict(),
            file,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )

def load_warship(name: str) -> Warship:
    warships_storage_dir = get_relative_path("NavalWarfare/main_content/warships_storage")
    warship_folder = os.path.join(warships_storage_dir, name.lower().replace(' ', '_'))
    warship_file_path = os.path.join(warship_folder, f"{name.lower().replace(' ', '_')}.json")
    
    if not os.path.isfile(warship_file_path):
        raise FileNotFoundError(f"No se encontró el archivo JSON para el barco '{name}' en {warship_file_path}")

    with open(warship_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return Warship(**data)


def load_all_warships():
    warships = []
    warships_storage_dir = get_relative_path("NavalWarfare/main_content/warships_storage")

    if not os.path.exists(warships_storage_dir):
        raise FileNotFoundError(f"No se encontró la carpeta de almacenamiento de barcos en {warships_storage_dir}")

    for folder_name in os.listdir(warships_storage_dir):
        warship_folder = os.path.join(warships_storage_dir, folder_name)
        if os.path.isdir(warship_folder):
            warship_file_path = os.path.join(warship_folder, f"{folder_name}.json")
            if os.path.isfile(warship_file_path):
                with open(warship_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    warship = Warship(**data)
                    warships.append(warship)
            else:
                print(f"Advertencia: No se encontró el archivo JSON para el barco en {warship_file_path}")
    
    return warships