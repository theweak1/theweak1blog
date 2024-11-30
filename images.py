#! /usr/bin/env python3
import os
import re
import shutil

# Paths
posts_dir = "/home/theweak1/Work/portfolio/theweak1blog/content/posts/"
attachments_dir = "/home/theweak1/Documents/myVault/Attachments/"
static_images_dir = "/home/theweak1/Work/portfolio/theweak1blog/static/images/"

# Ensure static images directory exists
os.makedirs(static_images_dir, exist_ok=True)

# Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Find all image links in the format [[image.png]]
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        for image in images:
            # Prepare the Markdown-compatible link
            sanitized_image = image.replace(" ", "%20")
            markdown_image = f"![Image Description](/images/{sanitized_image})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Copy the image to the static images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            image_destination = os.path.join(static_images_dir, image)
            
            if os.path.exists(image_source):
                if not os.path.exists(image_destination):  # Avoid duplicate copies
                    shutil.copy(image_source, image_destination)
                print(f"Copied: {image_source} -> {image_destination}")
            else:
                print(f"Warning: Source image not found: {image_source}")

        # Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

