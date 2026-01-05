# AI Projects – Computer Vision & Generative AI

This repository contains three AI projects focused on solving practical
computer vision and document automation problems using Python and AI models.

---

## Project 1: RGB–Thermal Image Alignment

**Objective:**  
Align thermal images with RGB images captured from different cameras and
generate properly aligned thermal outputs.

**What was done:**
- Feature-based image alignment
- Batch processing of image pairs
- RGB images kept unchanged while thermal images were adjusted

**Core concepts:**
- Image registration
- Feature matching
- OpenCV pipelines

---

## Project 2: Image Change Detection

**Objective:**  
Detect and highlight changes between before-and-after images of the same scene.

**What was done:**
- Compared aligned image pairs
- Identified missing or changed objects
- Highlighted changes using bounding boxes / regions

**Core concepts:**
- Image comparison
- Difference detection
- Visual annotation

---

## Project 3: Automated Document Filling using LLMs

**Objective:**  
Automate document template filling by extracting structured information
from reports using Large Language Models.

**What was built:**
- Streamlit-based interface
- Upload document templates (.docx)
- Upload reports (.pdf)
- Extracted data using NLP + LLMs
- Generated auto-filled downloadable documents

**Core concepts:**
- NLP
- LLM reasoning
- Streamlit applications
- End-to-end automation

---

## Tech Stack
- Python
- OpenCV
- NumPy
- Streamlit
- NLP & LLM APIs
