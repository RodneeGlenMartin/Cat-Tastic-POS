import os
import sys
import subprocess

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

source_img_path = r"C:\Users\Rodnee\.gemini\antigravity\brain\5b5e84c9-c311-4758-81d6-8485d6958f4c\media__1779897246767.png"
base_res_path = r"D:\Documents\GitHub\Cat-Tastic-POS\app\src\main\res"

sizes = {
    "mdpi": 48,
    "hdpi": 72,
    "xhdpi": 96,
    "xxhdpi": 144,
    "xxxhdpi": 192
}

try:
    img = Image.open(source_img_path).convert("RGBA")
    
    for density, size in sizes.items():
        mipmap_dir = os.path.join(base_res_path, f"mipmap-{density}")
        os.makedirs(mipmap_dir, exist_ok=True)
        
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        
        resized_img.save(os.path.join(mipmap_dir, "ic_launcher.png"))
        resized_img.save(os.path.join(mipmap_dir, "ic_launcher_round.png"))
        
    print("Icons generated successfully!")
except Exception as e:
    print(f"Error: {e}")
