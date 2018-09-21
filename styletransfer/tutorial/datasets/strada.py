# Copyright 2018 The DPS Laboratory. All Rights Reserved.
#
#
#
#
# shilhang:from tutorial.strada import input_data
# https://github.com/dps-lab
#
#
#
#
#
"""Functions for downloading and reading Style transfer data(to be continued)."""
# if fail to download, please download the raw data at 'git clone https://github.com/KyeongSeon-Kim/STRADA.git'

import os
#This is for easy downloading through URL
import urllib2

DEFAULT_SOURCE_URL = "http://rlar2146.dothome.co.kr/styletransfer/tutorial/datasets/"
MODIFY_SOURCE_URL = "default"
# DEFAULT_SOURCE_URL = "http://dpslab.re.kr/STRADA/"

#Showing the command
def __help__():
    print("===========================================================")
    print("STRADA has 2 commands below")
    print("-----------------------------------------------------------")
    print("")
    print("")
    print("     show_label          Showing the label of style images")
    print("")
    print("     down_cdata_sets      Downloading and reading the style transfer content data")
    print("")
    print("     down_sdata_sets      Downloading and reading the style transfer style data")
    print("")

#Showing the style label to user
def show_label():
    stylelabel=["Baroque","Mannerism","Modern_art","Neoclassicism","Renaissance","Rococo","Romanticism","Symbolism"]
    return stylelabel

#Downloading and reading the content data
def down_cdata_sets():
    #Directory created
    try : 
        if not(os.path.isdir("tutorial/datasets/")):
            os.makedirs(os.path.join("tutorial/datasets/"))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create DIR")
            raise
    MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL+"content_image.zip"
    #File download
    f=open("tutorial/datasets/content_image.zip",'wb')
    header = {'User-Agent':'Mozilla/5.0','referer':'http://rlar2146.dothome.co.kr'}
    #to prevent fail download
    req = urllib2.Request(MODIFY_SOURCE_URL,headers=header)

    response = urllib2.urlopen(req)
    print("Content dataset will be download soon...")
    f.write(response.read())
    print("Download completed!")
    f.close()


#Downloading and reading the style data
def down_sdata_sets(style):
    if style == "all" :
        MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + dpst + ".zip"
    elif style == "Baroque" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Mannerism" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Modern_art" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Neoclassicism" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Renaissance" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Rococo" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Romanticism" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    elif style == "Symbolism" :
	MODIFY_SOURCE_URL = DEFAULT_SOURCE_URL + style + ".zip"
    else :
        print("Please enter the right style. The style is follow as")
        print(show_label())
        return style
    
    #Directory created
    try : 
        if not(os.path.isdir("tutorial/datasets/style_image/")):
            os.makedirs(os.path.join("tutorial/datasets/style_image/"))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create DIR")
            raise

    #File download
    f=open("tutorial/datasets/style_image/"+style+'.zip','wb')
    header = {'User-Agent':'Mozilla/5.0','referer':'http://rlar2146.dothome.co.kr'}
    #to prevent fail download
    req = urllib2.Request(MODIFY_SOURCE_URL,headers=header)

    response = urllib2.urlopen(req)
    print(style+" dataset will be download soon...")
    f.write(response.read())
    print("Download completed!")
    f.close()


"""

f=open(style+'zip','wb')
#header = {'User-Agent':'Mozilla/5.0','referer':'http://dpslab.re.kr'}
header = {'User-Agent':'Mozilla/5.0','referer':'http://rlar2146.dothome.co.kr'}

req = urllib2.Request(MODIFY_SOURCE_URL,headers=header)

response = urllib2.urlopen(req)
f.write(response.read())
f.close()
"""

