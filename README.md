# DensePose API Docker
GPU powered API that recieves an image and returns the DensePose UVmask:

### Input
![alt text](https://raw.githubusercontent.com/facebookresearch/DensePose/master/DensePoseData/demo_data/demo_im.jpg)

### Output
![alt text](https://raw.githubusercontent.com/facebookresearch/DensePose/master/DensePoseData/infer_out/demo_im_IUV.png)

## Dependencies
* Docker
* Docker-Compose
* nvidia-Docker
* A NVIDIA GPU

## Usage
1. From the `docker` folder run: `docker-compose up -d` 

After building the Docker container, the API will start.

You can check the status of the container with: `docker ps -a`

2. On the main folder run: `python send_files.py` 



