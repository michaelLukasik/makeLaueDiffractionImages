#!usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os.path
import os, time
import glob
import time 
import cv2
import getTags
import imageMaker
import tools

## Quick and dirty solution for now, run this AFTER creating images with imageMaker.py

frameOrder = np.linspace(0,355,72)
varyingParameter = 'PHI'
gifPath = "C:\\Users\\Michael\\Documents\\Programming\\makeLaueDiffractionImages\\images\\EigenResults_CONFIG_1.e-7XPOS_5e-7DZDY_1e-5LEN_varryingPhi_1NX_100NY_100NZ_1e-11LAMBDA_primativeCENTERING_dolomiteNAME_CONFIG_\\filtered\\high"
tools.makeGif(gifPath, frameOrder, varyingParameter) 