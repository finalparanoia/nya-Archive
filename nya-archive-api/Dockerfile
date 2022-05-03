FROM python
#RUN apt install clang cmake boost dlib

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

ENV PYTHONUNBUFFERED=0
# Run app.py when the container launches
CMD ["python", "-u", "main.py"]
