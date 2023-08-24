# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /winequality

# Copy the current directory contents into the container at /app
COPY . /winequality

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt  

# Run streamlit when the container launches
CMD python app.py 