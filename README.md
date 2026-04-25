# Image Multiformat Tool

A Django web application for processing images. Upload an image, choose a tool, and download the processed result.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-green.svg)

## Features

| Tool | Description |
|------|-------------|
| 🔳 Grayscale | Convert color images to black and white |
| ✂️ Remove Background | Cut out the subject with transparent PNG |
| 🌫️ Blur | Soften images with adjustable blur radius |
| 📄 JPEG to PNG | Convert JPEG to PNG format |
| 🗜️ Compress to WebP | Create smaller WebP files |

## Tech Stack

- **Backend**: Python 3.11+, Django 5.x
- **Image Processing**: Pillow, rembg
- **Frontend**: Tailwind CSS, Alpine.js

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/img-multiformat.git
cd img-multiformat

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install django pillow rembg

# Run the server
python manage.py runserver
```

## Screenshots

### Main Interface
<img width="1902" height="969" alt="image" src="https://github.com/user-attachments/assets/0f46666c-7f4b-4f7a-b044-6bece23b0051" />

### Choose a Tool
<img width="1918" height="965" alt="image" src="https://github.com/user-attachments/assets/aa4422be-fdde-4492-8731-cf6fafc6c258" />

### Upload & Process
<img width="3164" height="2700" alt="127 0 0 1_8000_ (1)" src="https://github.com/user-attachments/assets/2ba2e8b2-768e-4eb7-a09b-bfe5372b38c3" />

### Result

#### Blur

<img width="1610" height="500" alt="before-after-comparison" src="https://github.com/user-attachments/assets/783dcb8a-5054-43f4-b240-8c63bcb43098" />

#### Remove Background

<img width="1610" height="500" alt="before-after-comparison (2)" src="https://github.com/user-attachments/assets/2259721b-39cc-45a3-93af-204e1a6ba704" />

#### Grayscale

<img width="1610" height="500" alt="before-after-comparison (1)" src="https://github.com/user-attachments/assets/589b2f05-b812-4360-b337-63cbe8be71ae" />


### Try it and let me know your thoughts. 
