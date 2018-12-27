# IMC-DataScience Project 2018

This is a class project for IMC Data Science class with Pouya Yousefi. The project consists of two django applications (one for UI and the other for API) running on separate django servers on top of separate docker images. The docker images are built and run using docker-compse. The project's aim is to predict purchses of users based on their social constructs (age, city, marital status) during Black Friday using a machine learning model we built to perform those predictions. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

**You need to have docker installed on your machine.**

In order to run the project on Docker, you can either:
* 1. Make sure to set your docker machine's IP address to 192.168.99.100.
* 2. Add your docker machine's IP address to the project settings file under:
MainGUI\MainGUI\setting.py
```
ALLOWED_HOSTS = ['<your_docker_machine_ip>', '192.168.99.100', 'localhost', '127.0.0.1']	
```

There are **two** shell scripts called "start" under the following directories, **make sure that their EOL conversion is set to UNIX (LF):**
* /HandleRequests
* /MainGUI

### Building & Running
You have to build the docker-compose file first to download the machine learning model.

```
docker-compose build
```
Docker will download the model from a google drive since the model's size is greater than 100 MB which is the maximum that Github allows.
```
docker-compose up
```

### You should be able to access the application at **<docker_machine_ip>:5001**
