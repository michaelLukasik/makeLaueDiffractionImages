import numpy as np 
import pandas as pd
import glob
import matplotlib.pyplot as plt
from tools import bandPassFilter
import cv2

def sumWF(sim_wfRe, sim_wfIm,totalWF):
    totalWF[:,0] += sim_wfRe
    totalWF[:,1] += sim_wfIm
    
def plotAverage(totalWF):
    intensity = np.sqrt(totalWF[:,0] **2 + totalWF[:,1] **2)
    intensity = np.asarray(intensity) / np.linalg.norm(intensity) 
    intensity = np.reshape(intensity,(int(2.3e-6/2e-9), int(2.3e-6/2e-9)))#np.reshape(intensity,(int(wall_len/dzdy), int(wall_len/dzdy)))
    plt.imshow(np.asarray(intensity), cmap = "gray_r")
    plt.imsave("./averageIntensityB10DNA_PSIaveraged_0NXYZ_1Points_5degspacing.png", intensity,cmap = "gray")
    plt.show()
    
def bandPassFilterDNA():
    gBlur = 21
    saveStr = "averageIntensityB10DNA_PSIaveraged_0NXYZ_1Points_5degspacing.png"
    filteredImage = bandPassFilter(r"./"+saveStr, 400, 5 , 111)
    filteredImage = cv2.GaussianBlur(filteredImage, (gBlur,gBlur), 0)
    thresh = cv2.threshold(filteredImage, 18, 255, cv2.THRESH_BINARY_INV)[1]
    print(np.size(thresh[1]) / 3)
    cv2.line(thresh, (769, 1150), (381,0), (45, 45, 255), thickness=1)
    cv2.line(thresh, (381, 1150), (769,0), (45, 45, 255), thickness=1)
    plt.figure(figsize=(10,10))
    plt.imshow(np.asarray(thresh))   
    plt.imsave("./BPFilterTH_"+saveStr ,thresh,cmap = "gray")

    plt.show()
    
    
    
def averageDNA():
    #size_str = "3NX_3NY_3NZ" # [psi: 0, 10 ] [theta: 5,355 ] 
    size_str = "0NX_0NY_0NZ" # [psi: 0,5,10,15,345,350,355] [theta: 5,10,350,355 ]
    screen_str = "*1e-3XPOS_2e-9DZDY_2.3e-6LEN*"
    basePath = r"C:\Users\Michael\Documents\Programming\laueDiffractionResults\csvFiles\\"
    psi0Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_0PSI*"+size_str+"*.csv" )
    psi5Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_5PSI*"+size_str+"*.csv" )
    psi10Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_10PSI*"+size_str+"*.csv")
    psi15Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_15PSI*"+size_str+"*.csv" )
    psi345Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_345PSI*"+size_str+"*.csv" )
    psi350Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_350PSI*"+size_str+"*.csv")
    psi355Files =  glob.glob(basePath + screen_str+"*_0THETA_*PHI_355PSI*"+size_str+"*.csv" )
    
    theta5Files =  glob.glob(basePath + screen_str+"*_5THETA_*PHI_0PSI*"+size_str+"*.csv" )
    theta10Files = glob.glob(basePath + screen_str+"*_10THETA_*PHI_0PSI*"+size_str+"*.csv" )
    theta350Files = glob.glob(basePath + screen_str+"*_350THETA_*PHI_0PSI*"+size_str+"*.csv" )    
    theta355Files =  glob.glob(basePath + screen_str+"*_355THETA_*PHI_0PSI*"+size_str+"*.csv" )

    for i in [psi0Files,psi10Files,psi5Files]:
    #for i in [theta10Files,theta5Files,psi0Files,theta350Files,theta355Files,
    #          psi10Files,psi5Files,psi350Files,psi355Files]:
        print(np.size(i))

    
    
    
    testfile = pd.read_csv(psi0Files[0] ,header = None , dtype = np.float32, na_values = "-nan(ind)")
    totalWF = np.zeros((testfile[0].size,2), dtype = np.float32)
    del testfile
    
    for i,file in enumerate(psi0Files):
        print("Working on file number " + str(i+1)+ " of "+str(len(psi0Files)) + ": "+file)
        file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
        sumWF(file_temp[0],file_temp[1],totalWF)
    
    
    #for i,file in enumerate(psi5Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(psi5Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    #for i,file in enumerate(psi10Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(psi10Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    #for i,file in enumerate(psi15Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(psi15Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)

    #for i,file in enumerate(psi345Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(psi350Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    #for i,file in enumerate(psi355Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(psi355Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
        
        
    ####

        
    #for i,file in enumerate(theta5Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(theta5Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    #for i,file in enumerate(theta10Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(theta10Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    
    #for i,file in enumerate(theta350Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(theta350Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    #for i,file in enumerate(theta355Files):
    #    print("Working on file number " + str(i)+ " of "+str(len(theta355Files)) + ": "+file)
    #    file_temp = pd.read_csv(file,header = None , dtype = np.float32, na_values = "-nan(ind)")
    #    sumWF(file_temp[0],file_temp[1],totalWF)
    
    plotAverage(totalWF)
    
        

#averageDNA()
bandPassFilterDNA()


#"C:\Users\Michael\Documents\Programming\laueDiffractionResults\csvFiles\"EigenResults_CONFIG_1e-3XPOS_2e-9DZDY_2.3e-6LEN_0THETA_150PHI_10PSI_3NX_3NY_3NZ_1e-11LAMBDA_primativeCENTERING_B10DNANAME_CONFIG_.csv"