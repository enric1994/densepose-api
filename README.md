# DensePose API Docker
GPU powered Docker API that recieves an image and returns the DensePose UVmask:

### Input
<img src="https://raw.githubusercontent.com/facebookresearch/DensePose/master/DensePoseData/demo_data/demo_im.jpg" width="40%">

### Output
<img src="https://raw.githubusercontent.com/facebookresearch/DensePose/master/DensePoseData/infer_out/demo_im_IUV.png" width="40%">

## Dependencies
* Any Linux distribution and a GPU (RTX GPUs not working yet)
* [Docker](https://gist.github.com/enric1994/3b5c20ddb2b4033c4498b92a71d909da)
* [Docker-Compose](https://gist.github.com/enric1994/3b5c20ddb2b4033c4498b92a71d909da)
* [nvidia-Docker](https://github.com/NVIDIA/nvidia-docker#ubuntu-16041804-debian-jessiestretchbuster)

## Usage
1. From the `docker` folder run: `docker-compose up -d` 

After building the Docker container (it can take a while), the API will start.

You can check the status of the container with: `docker ps -a`

You can also see what's going on inside the container with `docker logs densepose-api -f`

2. On the main folder run: `python send_files.py` 

If it's the first time you send an image to the API it can take a while as it will download the DensePose model (607MB)

This will send `demo_im.jpg` to the API using the Python requests package.

Feel free to modify the script and add it to your pipeline

Tested on Ubuntu 18.04 with a GTX 1060 GPU

## Advantages
* You don't have to install Caffe
* You don't have to install CUDA
* Very easy to integrate in any pipeline, only a HTTP request needed.
* The API will be isolated from your code. No dependency errors
* Did I mention that you don't need to install Caffe?
