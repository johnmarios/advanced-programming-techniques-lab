# Slim Python base image
FROM python:3.11-slim

# buffering
ENV PYTHONUNBUFFERED=1
# Set environment variable for GPIO access
ENV GPIOZERO_PIN_FACTORY=lgpio
# Set the working directory inside the container
WORKDIR /lab6


# Copy requirements file and install dependencies
COPY requirements.txt .
# Install lgpio dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    swig \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copy the library folder
COPY pirlib/ pirlib/

COPY consumer.py .
COPY producer.py .

# Create output directory
RUN mkdir -p /lab6/output

# Default command when the container starts
CMD ["python", "--version"]
#there is already command in compose file
