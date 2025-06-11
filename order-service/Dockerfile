# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install flask flask-cors

# Copy code
COPY app.py .

# Expose port
EXPOSE 5001

CMD ["python", "app.py"]
