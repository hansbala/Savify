#!/bin/bash

: '
The following script is for Linux/UNIX only.
This script installs the necessary packages 
to get up and running.
The following packages are installed and 
upgraded-
1. pip (Including upgrade)
2. openpyxl (Used for reading the xlsx workbook)
3. youtube-dl (For stripping the mp3 off YouTube)
4. bs4 - BeautifulSoup(For clawing the webpage)
'
#Root user access needed for pip
sudo su

#Installing Pip and upgrading
sudo apt-get install python-setuptools python-dev build-essential -y
easy_install pip
pip install -U pip

#Installing openpyxl
pip install openpyxl

#Installing youtube-dl
pip install youtube-dl

#Installing BeautifulSoup
pip install bs4

#Installing ffmpeg
sudo apt-get install ffmpeg

clear
echo "Successfully installed everything..."
echo "Okay to exit and continue...."
echo "You can close this window now."
