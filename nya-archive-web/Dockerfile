FROM nginx
#RUN apt install clang cmake boost dlib

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./html /app/html
COPY ./nginx.conf /etc/nginx/nginx.conf

# Make port 80 available to the world outside this container
EXPOSE 9889

# Run app.py when the container launches
# CMD ["", "-u", "main.py"]
