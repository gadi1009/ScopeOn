# Use an official Node.js runtime as a parent image
FROM node:20-slim

# Set work directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Install http-server globally (or as a dev dependency if preferred)
RUN npm install -g http-server

# Copy project
COPY . . 

# Expose port
EXPOSE 3000

# Start the server
CMD ["npm", "run", "dev"]