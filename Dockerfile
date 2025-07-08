FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY flask.py /app1.py

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python3", "/app.py"]
