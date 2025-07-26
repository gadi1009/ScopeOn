# Use an official Node.js runtime as a parent image
FROM node:20-slim

# Set work directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Install http-server globally
RUN npm install -g http-server

# Copy project files
COPY . . 

# Build Tailwind CSS
RUN npx tailwindcss -i ./src/input.css -o ./dist/output.css --config tailwind.config.js --minify

# Expose port
EXPOSE 3000

# Start the HTTP server
CMD npm run start