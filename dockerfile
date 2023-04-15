# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app's port
EXPOSE 5000

# Define environment variables for MongoDB
ENV MONGO_HOST=localhost
ENV MONGO_PORT=27017
ENV MONGO_DB=mydatabase
ENV MONGO_COLLECTION=mycollection

# Start MongoDB and the Flask app with docker-compose
CMD ["docker-compose", "up"]
