import os
import threading
import time
import config
from functions import checkLink
from functions import remove_url_anchor
from functions import pageToCrawl
from linkitem import LinkItem

from urllib.parse import urljoin

from functions import printresults
from bs4 import BeautifulSoup
from result import Result
from multifunct import linkCheckThread
from multifunct import noCheckThread


import urllib.request
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



path =  config.path
internetDirectory =  "\\crawledLinks\\internet"
intranetDirectory =  "\\crawledLinks\\intranet"
smallSiteDirectory =  "\\crawledLinks\\smallsite"
filepath = path + intranetDirectory
linkFilesNamesInternet = os.listdir(filepath)
linkFiles=[]
allResults=[]
domain = "https://www.epa.gov"

currentPath = os.path.dirname(os.path.realpath(__file__))
folderPath = currentPath + "\\results"
if (not os.path.exists(folderPath)):
    folder = currentPath + "/results"
    try:
        os.mkdir(folder)
    except OSError:
        print("Creation of the directory %s failed" % folder)
    else:
        print("Successfully created the directory %s " % folder)

#Internet Pages
for file in linkFilesNamesInternet:
    f = open(str(filepath) + "\\" + str(file), "r")
    if f.mode == 'r':
        contents = f.read().splitlines()
        #linkFiles.append(contents)
    f.close()

#find all Intranet pages.
filepath = path + intranetDirectory
linkFilesNamesIntranet = os.listdir(filepath)

for file in linkFilesNamesIntranet:
    f = open(str(filepath) + "\\" + str(file), "r")
    if f.mode == 'r':
        contents = f.read().splitlines()
        #linkFiles.append(contents)
    f.close()

filepath = path + smallSiteDirectory
linkFilesNamesIntranet = os.listdir(filepath)
#small sites
for file in linkFilesNamesIntranet:
    f = open(str(filepath) + "\\" + str(file), "r")
    if f.mode == 'r':
        contents = f.read().splitlines()
        linkFiles.append(contents)
    f.close()

resultDict={}
index = 0



#iterate through files, finding list of each site's links
for linkList in linkFiles:

    linkResults = []
    count = 0
    newdomain = ""
    newfilename = ""
    totalLinks = 0
    totalErrors = 0
    totalSuccess = 0




    #test link in linkList.
    for link in linkList:

        #For first link, this is the name of the website.
        if count is 0:
            str = link.split()

            newdomain =  str[0]
            newfilename =  str[1]
        else:


            if pageToCrawl(link) is True:#double check site.
                print("link: " + link)

                try:
                    page = urllib.request.urlopen(link)
                    soup = BeautifulSoup(page, 'html.parser')
                    siteTitle = soup.title.string

                    anchorList = []
                    for a in soup.find_all('a'):
                        try:
                            linkitem = LinkItem("def1", "def2")
                            anchor = a['href']


                            #print(anchor)
                            anchor = remove_url_anchor(anchor)
                            linkitem.anchortext = a.text


                            anchor = urljoin(domain, anchor)
                            if (' ' in anchor):
                                anchor = anchor.replace(' ', '%20')

                            linkitem.url = anchor
                            anchorList.append(linkitem)

                        except KeyError:
                            print("keyerror")  # or some other fallback action



                    #combine links
                    alllinks = []
                    alllinks = anchorList


                    threadList = []

                    #Create threads
                    dictSize = len(resultDict)
                    newlinkindex = 0
                    for testlink in alllinks:
                        #check all links:
                        #def linkCheckThread (testlink, resultDict, allResults, link, siteTitle):

                        # Check to see if tested
                        if testlink.url not in resultDict:
                            t1 = threading.Thread(target=linkCheckThread, args=(testlink, resultDict,allResults, link ,siteTitle, linkResults, newlinkindex))
                            newlinkindex = newlinkindex + 1
                        else:
                            t1 = threading.Thread(target=noCheckThread, args=(testlink, resultDict,allResults, link ,siteTitle, linkResults))
                        threadList.append(t1)

                    #start threads
                    for thread in threadList:
                        thread.start()

                    for thread in threadList:
                        thread.join()



                except urllib.error.HTTPError:
                    print("403 error forbidden.")
        print("b4count")
        print(count)
        count = count+1

    #print("linkCount: " + str(len(linkResults)))
    printresults(linkResults, newfilename +" Links" , path)





print("Finish")


