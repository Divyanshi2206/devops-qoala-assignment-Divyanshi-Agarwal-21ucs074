FROM python:3.9

# WORKDIR /appp

# COPY appy.py /app

# RUN pip install flask netiface

# EXPOSE "eight thousand"

# CMD ["pythn", "app.py"]


# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container's working directory
COPY app.py /app/

# Install the required Python packages
RUN pip install flask netifaces

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
