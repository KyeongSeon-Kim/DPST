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
print(styleDir)

"""
def example(style) :

    styleDir = ("style_image/" + style)
    str(styleDir)

    for root, dirs, files in os.walk(styleDir):
        for fname in files:
            input_fname = os.path.join(root, fname)
            temp = (input_fname.split("."))[0]
            output_fname = temp+("_trans.jpg")

	    #Make the sentences of instruction
            inst_sentence= ("python run_main.py --content content_image/310_1.jpg "+"--style "+input_fname+" --output "+output_fname)
            #Show where the Park Ji-sung works.
	    print ("////////////////////////////////////////////////")
            #print (inst_sentence)
            print ("Let's start to transfer the image " + input_fname)
            print ("////////////////////////////////////////////////")

            #Start to run!!
            subprocess.check_output(inst_sentence, shell=True)
            #subprocess.call(inst_sentence, shell=True)
    
"""
for root, dirs, files in os.walk(styleDir):
    for fname in files:
        input_fname = os.path.join(root, fname)
        temp = (input_fname.split("."))[0]
        output_fname = temp+("_trans.jpg")

	#Make the sentences of instruction
        inst_sentence= ("python run_main.py --content content_image/310_1.jpeg "+"--style "+input_fname+" --output "+output_fname)

        #Show where the Park Ji-sung works.
	print ("////////////////////////////////////////////////")
        #print (inst_sentence)
        print ("Let's start to transfer the image " + input_fname)
        print ("////////////////////////////////////////////////")

        #Start to run!!
        subprocess.call(inst_sentence, shell=True)

