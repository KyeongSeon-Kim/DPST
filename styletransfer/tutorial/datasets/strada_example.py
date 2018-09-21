#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Made by KKS in DPS Laboratory with J.Kim @CAU

import os
import subprocess
import sys


styleDir = ""
style = sys.argv[1]
styleDir = ("style_image/" + style)
str(styleDir)
#print(styleDir)

if sys.argv[1] == "--help": 
    print("===========================================================")
    print("STRADA sample code executing example")
    print("-----------------------------------------------------------")
    print("")
    print("")
    print("     strada_example.py --help               Show this help message")
    print("")
    print("     strada_example.py Modern_art           Transfer all images where 'Modern_art' folder")
    print("")
    print("     strada_example.py style.jpg            Transfer content image with style.jpg images's style")
    print("")


else :
    if os.path.isfile(styleDir) :
        output_fname = styleDir+("_trans.jpg")
        #Make the sentences of instruction
        inst_sentence= ("python run_main.py --content content.jpeg "+"--style "+styleDir+" --output "+output_fname)

        #Show where the Park Ji-sung works.
	print ("////////////////////////////////////////////////")
        #print (inst_sentence)
        print ("Let's start to transfer the image " + styleDir)
        print ("////////////////////////////////////////////////")

        #Start to run!!
        subprocess.call(inst_sentence, shell=True)
    else :    
        for root, dirs, files in os.walk(styleDir):
            for fname in files:
                input_fname = os.path.join(root, fname)
                temp = (input_fname.split("."))[0]
                output_fname = temp+("_trans.jpg")

    	        #Make the sentences of instruction
                inst_sentence= ("python run_main.py --content content.jpeg "+"--style "+input_fname+" --output "+output_fname)

                #Show where the Park Ji-sung works.
	        print ("////////////////////////////////////////////////")
                #print (inst_sentence)
                print ("Let's start to transfer the image " + input_fname)
                print ("////////////////////////////////////////////////")

                #Start to run!!
                subprocess.call(inst_sentence, shell=True)
    
