# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend app
COPY fastapi_app.py .

# Expose port
EXPOSE 10000

# Run
CMD ["python", "fastapi_app.py"]