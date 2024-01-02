# Use an ARM64-based Python image
FROM arm64v8/python:3.11

# Set the working directory to /app
WORKDIR /src

# Copy only the requirements file to leverage Docker cache
COPY src/requirements.txt .
COPY package*.json ./src/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Specify the command to run on container start
CMD ["npm", "start"]


