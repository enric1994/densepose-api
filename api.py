# !/usr/bin/env python2
# -*- coding: utf-8 -*-
# (c) Copyright 2019 Enric Moreu. All Rights Reserved.

from flask import Flask, request, send_file
from skimage.io import imread, imsave
import os
import numpy as np
import cv2
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST'])
def process_files():

	received_images = []
	images = request.files.to_dict()
	for image in images:
		file_name = images[image].filename
		logging.info('File received: {}'.format(file_name))
		npimg = np.fromfile(images[image], np.uint8)
		decoded_image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
		imageRGB = cv2.cvtColor(decoded_image , cv2.COLOR_BGR2RGB)
		received_images.append(imageRGB)

	# Do some operation using the received files and the parameters
	imsave('/densepose-api/tmp/tmp_result.png', received_images[0])

	logging.info('Applying densepose...')
	os.system('python2 /densepose/tools/infer_simple.py     --cfg /densepose/configs/DensePose_ResNet101_FPN_s1x-e2e.yaml     --output-dir /densepose-api/tmp     --image-ext png     --wts https://dl.fbaipublicfiles.com/densepose/DensePose_ResNet101_FPN_s1x-e2e.pkl     /densepose-api/tmp/tmp_result.png')	

	# Return one file
	resp = send_file(open('/densepose-api/tmp/tmp_result_IUV.png'), mimetype='image/png')
	return resp

app.run(host="0.0.0.0", port=5000)
