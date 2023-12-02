#!usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os.path
import os 
import glob
import time 
import cv2
import getTags
import imageMaker
import tools
#import averageDNA

class cfg:  ## Config Parameters, Change these depending on what you are plotting
    centering = "primative" + "CENTERING_"
    name = "dolomite" + "NAME_"
    xpos = "1.e-7" + "XPOS_" 
    dzdy = "5e-7" + "DZDY_"
    len = "1e-5" + "LEN_"
    theta = "0" + "THETA_" 
    psi = "0" + "PSI_" 
    phi = "0" + "PHI_" 
    nx = "1" + "NX_"
    ny = "100" + "NY_"
    nz = "100" + "NZ_"
    Lambda = "1e-11" + "LAMBDA_"
    manualConfiguration = False
    cmap = "gray" ## Or any matplotlib cmap you want
    zoom = 1. ## zooms into the center of the sceen by a factor of [x]
    running = "*PHI_" ## If running over a number of images at a specific angle, specify what running angle you need here. 
    lowPassTh = 100
    highPassTh = 100
    bandPassThL = 130  # Must be higher than the bandPassThH Filter Number
    bandPassThH = 10
    gBlur = 1
    filterImages = 1.

defaultImages = ['/raw/','/fft/','/shiftedfft/']
imagesToCreate = ['/filtered/']

str_folderTag, str_angleTag = getTags.getFolderAngleTag(cfg.manualConfiguration, cfg)
fullCSVTag = getTags.getFullCSVTag(str_angleTag, cfg)
fullSaveFolderTag = getTags.getFullSaveTag(str_folderTag, cfg)
savePath = "images/"
saveFolder = "EigenResults_CONFIG_"+fullSaveFolderTag+"CONFIG_"

## path for gif maker, just copy and paste from Windows
gifPath = "C:\\Users\\Michael\\Documents\\Programming\\makeLaueDiffractionImages\\images\\EigenResults_CONFIG_1.e-7XPOS_5e-7DZDY_1e-5LEN_varryingPhi_1NX_100NY_100NZ_1e-11LAMBDA_primativeCENTERING_dolomiteNAME_CONFIG_\\filtered\\high"

files = glob.glob("csvFiles/EigenResults_CONFIG_"+fullCSVTag+"CONFIG_.csv")
print("csvFiles/EigenResults_CONFIG_"+fullCSVTag+"CONFIG_.csv")


if len(files) == 0:
    print("NO FILES FOUND WITH:")
    print("/csvFiles/EigenResults_CONFIG_"+fullCSVTag+"CONFIG_.csv")
    print("Check file name and try again")
    exit()

### Create the directories to place our images in
tools.makeDefaultFolders(savePath, saveFolder)
for imageTypeTag in imagesToCreate:
    tools.makeFilteredImageFolder(savePath, saveFolder, imageTypeTag, '/')
    tools.makeFilteredImageFolder(savePath, saveFolder, imageTypeTag, '/low/')
    tools.makeFilteredImageFolder(savePath, saveFolder, imageTypeTag, '/high/')
    tools.makeFilteredImageFolder(savePath, saveFolder, imageTypeTag, '/band/')

### Create the raw and default Images
for file in files:
    print("Working on: " + file)
    simData = imageMaker.readCSV(file)
    imageMaker.makeDefaultImages(simData, file, savePath, saveFolder, cfg)
    imageMaker.makeShiftedFFT(simData, file, savePath, saveFolder, cfg)
if cfg.filterImages:
    images = glob.glob(savePath + saveFolder + "/raw/*.png")
    for image in images:
        imageMaker.makeLowPassFilter(image, savePath, saveFolder, radius = cfg.lowPassTh, gBlur = cfg.gBlur) 
        imageMaker.makeHighPassFilter(image, savePath, saveFolder, radius = cfg.highPassTh, gBlur = cfg.gBlur)
        imageMaker.makeBandPassFilter(image, savePath, saveFolder, radius = cfg.bandPassThL, outer_radius = cfg.bandPassThH, gBlur = cfg.gBlur)
        
# Make gif at directed folder, defined above
tools.makeGif(gifPath) 
#averageDNA.averageDNA(cfg)
#imageMaker.plotDNA        
        
