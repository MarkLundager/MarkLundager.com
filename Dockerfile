FROM arm64v8/python:3.11
WORKDIR /app

# Copy the backend code to the container
COPY backend/ .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change to the frontend directory
WORKDIR /app/frontend

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Install frontend dependencies
RUN npm install

# Build the frontend
RUN npm run build

# Expose the port your app runs on
EXPOSE 8000

# Change back to the /app directory
WORKDIR /app

# Specify the command to run on container start
CMD ["python", "backend/src/app.py"]


