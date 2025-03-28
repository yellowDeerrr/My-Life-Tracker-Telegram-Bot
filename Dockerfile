# Use Python 3.9 slim image as base
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (or any port your app uses)
EXPOSE 5000

# Run your Python application
CMD ["python3", "main.py"]
