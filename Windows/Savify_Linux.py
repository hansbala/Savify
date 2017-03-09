#!/usr/bin/python

#COPYRIGHT(C) 2017 HANS BALA

"""
FOR WINDOWS
NOT FOR LINUX/OS X
--------------------------
--------------------------
----------HANS------------
----------BALA------------
--------------------------
--------------------------
------(  *   *  )---------
-------(   |   )----------
--------(  ^  )-----------
--------------------------
---PLAGARISM IS HARMFUL---
-------FOR HEALTH---------
"""
from openpyxl import *;
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

def header():
    print "THIS SOFTWARE IS COPYRIGHT(C) PROTECTED."
    print "CHECK THE FOLDER LICENSE FOR DETAILS."

def searchYoutube(trackname):
    textToSearch = trackname
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    return "https://youtube.com" + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']

def downloadYoutube(link):
    command = 'youtube-dl --no-warnings --extract-audio --audio-format mp3 -o ' + the_path+ '"%(title)s.%(ext)s" ' + link
    os.system(command)
    print "Song Downloaded"

if __name__ == "__main__":
    header()
    filen = raw_input("Enter the filename: ")+".xlsx"
    the_path = os.path.expanduser('~') + "//Music//Spotify//"
    wb = load_workbook(filename=filen)
    ws = wb.active
    if not os.path.exists(the_path):
      os.makedirs(the_path)
    song_name = ""
    artist_name = ""
    pos = 0
    for i in range(1, 1000000):
      song_name = ""
      artist_name = ""
      string = (ws["A"+str(i)].value)
      if(string==None):
        break
      arr = string.split(" ")
      for i in range(0, len(arr)):
              if arr[i] == u"\u2013":
                  pos = i
                  break
              try:
                  song_name = song_name + str(arr[i]) + " "
              except:
                  continue
      for i in range(pos+1, len(arr)):
              try:
                  artist_name = artist_name + str(arr[i]) + " "
              except:
                  continue
      print "Downloading: "
      print song_name
      print artist_name
      name = song_name + " " + artist_name
      link = searchYoutube(name)
      downloadYoutube(link)
    os.system('cls')
    print "ALL SONGS DOWNLOADED. SAFE TO EXIT"
    while(1>0):
        pass
