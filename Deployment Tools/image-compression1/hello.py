from pathlib import Path
from PIL import Image
import io

print("running hello.py")
def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    print("running function compress_image")
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if needed
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            # Optimize for web
            img.save(output_path, 'WEBP', quality=quality, optimize=True)
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

# Batch process images
paths = Path('Image').glob('*.jpg')
for p in paths:
    print("function called compress_image")
    try:
        compress_image(p, p.with_suffix('.webp'))
    except Exception as e:
        print(f"Error processing {p}: {e}")
