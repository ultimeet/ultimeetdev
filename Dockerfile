# Use an official Python runtime as the base image
FROM python:3.11.3

# Set the working directory in the container
WORKDIR /ultimeet

# Copy the Python script into the container
COPY . .

# Install dependencies if needed (add this line if your project has dependencies)
# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory to the container
COPY . .

# Expose the port on which the application will listen
EXPOSE 8000

# Specify the command to run the Python script
CMD ["python", "manage.py", "runserver"]
