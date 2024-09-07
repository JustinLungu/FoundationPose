#!/bin/bash

# remove any existing container "foundationpose"
docker rm -f foundationpose

'''
Example
realpath $0 --> returns /home/justin/my_project/docker/run_docker.sh
dirname $(realpath $0) --> /home/justin/my_project/docker
etc.
'''
echo "Project directory: $(dirname $(dirname $(realpath $0)))"
# set the project directory (assumed to be the parent of the 'docker' directory)
PROJECT_DIR=$(dirname $(dirname $(realpath $0)))


# run the Docker container
xhost +  # for container GUI
docker run --gpus all \
  --env NVIDIA_DISABLE_REQUIRE=1 \
  -it \
  --network=host \
  --name foundationpose \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  -v $PROJECT_DIR:/app \
  -v /home:/home \
  -v /mnt:/mnt \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /tmp:/tmp \
  --ipc=host \
  -e DISPLAY=${DISPLAY} \
  -e GIT_INDEX_FILE \
  foundationpose:latest \
  bash -c "cd /app && bash"