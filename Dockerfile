# Set base image (host OS)
# The Django version we are using depends on Sequence which was moved in python 3.10. That's why we install 3.9. 
FROM python:3.9-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# By default, listen on port 8000
#EXPOSE 80
EXPOSE 8000

# Installing GDAL --> this is a dependancy not obtainable through PIP
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Set the working directory in the container
WORKDIR /src
RUN python3 manage.py loaddata projects/fixtures/topics.json
RUN python3 manage.py loaddata projects/fixtures/status.json
RUN python3 manage.py loaddata projects/fixtures/participationtasks.json
RUN python3 manage.py loaddata projects/fixtures/geographicextend.json
RUN python3 manage.py loaddata resources/fixtures/categories.json
RUN python3 manage.py loaddata resources/fixtures/themes.json
RUN python3 manage.py loaddata resources/fixtures/audiences.json
RUN python3 manage.py loaddata organisations/fixtures/organisation_types.json

# Specify the command to run on container start

# This is the "standard" local development server and thus should not be used
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#This starts the production Gunicorn wsgi process on all ports be aware that the wsgi can't serve static files. 
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "eucs_platform.wsgi" ]

# Check out the infrastructure/nginx folder for further information on the nginx webserver container configuration. 
