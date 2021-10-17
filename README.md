# Docker-Image-Template-for-Python-Datascience
A generic Docker Package for building bespoke Python data science apps and running them in a mounted, open, dev container

Deployment:

1. Clone into a local directory

2. Open commandline and navigate into the directory

// cd #the-path-to-your-directory-here

3. Build the Docker Image

// docker build -t datascience_app .

-t: Tags the new image with the nickname datascience_app

Docker will then build the image from the Dockerfile template and install the python packages listed in requirements.txt

4. Run the docker container

// docker run -it --rm -v "%CD%":/app datascience_app /bin/bash

-it: interactive mode

--rm: remove the container and associated data on close.

-v: volume mount. Mounts the stated directory (in this case "%CD%" denotes the current working directory for windows) to the container (denoted by /app) so that files, scripts and data on your local computer can be accessed in the container.

/bin/bash: opens a new bash terminal and logs you into the container.
