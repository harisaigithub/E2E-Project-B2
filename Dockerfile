# Use the official Python image from DockerHub
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libmupdf-dev \
    libfreetype6-dev \
    libjpeg-dev \
    zlib1g-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run your application
CMD gunicorn --bind 0.0.0.0:8000 your_project.wsgi:application
