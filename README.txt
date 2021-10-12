This generic app will allow you to easily import GenBank files and work with them.

SETUP

1. Define in the dockerfile which python version you want to use.
2. Define which python packages your script needs in requirements.txt
Be careful with package dependancies - it's best to define the version of each package.


3. Name your script main_script.py

4. Load genbank files into the directory 'genbank files'


2. Check Docker is installed.
e.g.

docker --version

nb. If docker doesn't run its probably because the daemon isn't running. 
- Make sure WSL 2 is running.
- Make sure docker desktop has started up and the symbol is green.


4. Build the docker image. This will take a long time if you have lots of dependancies and packages.
e.g.

docker build -t my-analysis-app .

5. Run the docker image

runs the docker image, keeps the container open, mounts the directory so that you can edit as you go and opens a bash shell.
e.g.

docker run -it --rm  -v "%CD%":/app my-analysis-app /bin/bash


6. run your scripts

python main.py



https://www.youtube.com/watch?v=YFUhdxI4kcA