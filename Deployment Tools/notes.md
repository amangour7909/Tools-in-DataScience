# Image Compression for App Deployment

Image compression is crucial for optimizing storage and bandwidth when deploying applications, especially when dealing with numerous images. Here's a concise guide on image compression techniques and a Python code workflow for compressing images.

# key things to note
    - libraries - pathlib: handle paths, PIL:to compress image
    - Path from pathlib, Image(key package to handle image compression) from PIL
    - required things - input path, output path then open image of input path with Image 
    - save it in the required format with output path and image compression done.

## Key Concepts

- **Image Dimensions**: The width and height of an image in pixels significantly affect its file size.
- **Lossless Compression**: Formats like PNG and WebP preserve the exact data of the image, resulting in no quality loss.
- **Lossy Compression**: Formats like JPEG and WebP remove some data to reduce file size, which may lead to quality loss.
- **Vector Formats**: SVG images can be scaled without losing quality, making them ideal for graphics that can be vectorized.
- **WebP Format**: A modern image format that supports both lossy and lossless compression, offering a good balance between quality and file size.

## Rule of Thumb (as of 2025)

1. **Use SVG**: If the image is vector-based or can be converted to a vector format, use SVG.
2. **Use Lossy WebP**: For raster images, reduce the dimensions as much as possible and save them as lossy WebP for optimal compression.

## Python Code Workflow

The provided Python code demonstrates how to compress images using the Pillow library and save them in the WebP format.

### Workflow

1. **Import Libraries**: Import necessary modules (`Path` from `pathlib`, `Image` from `PIL`, and `io`).

2. **Define `compress_image` Function**:
   - **Parameters**: Takes `input_path`, `output_path`, and an optional `quality` parameter (default is 85).
   - **Open Image**: Use `Image.open()` to open the image file.
   - **Convert Mode**: If the image is in 'RGBA' mode, convert it to 'RGB' to ensure compatibility with WebP.
   - **Save Image**: Save the image in WebP format with specified quality and optimization.

3. **Batch Process Images**:
   - **Get Image Paths**: Use `Path('images').glob('*.jpg')` to get all JPEG images in the 'images' directory.
   - **Compress Each Image**: Iterate over each image path and call `compress_image` to convert and save it as WebP.

This workflow efficiently compresses images, reducing file sizes while maintaining reasonable quality, which is essential for web applications.

