from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
from functions import pageToCrawl
from functions import isSite
from functions import remove_url_anchor
from linkobj import LinkObj

import time
import requests
import os



from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sleeptime = 0.1

def crawlPage(indexUrl, domain, siteName, fileName, location):



    siteQueue = []
    crawledList = []
    badList = []   #for URLS that don't need to be printed
    redirectList = [] #List or URLS that are redirects to make sure they're not checked again.

    linkcount = 0

    indexLink = LinkObj(indexUrl, 0)
    siteQueue.append(indexLink)

    while siteQueue:
        site = siteQueue.pop()
        crawledList.append(site)
        #print("site: " + site)
        currentDepth = site.depthcount


        crawltest = pageToCrawl(site.url)
        if crawltest is True:


            try:

                page = urllib.request.urlopen(site.url)
                #page = "C:\\Users\\greg\\PycharmProjects\\crawler\\example.html"
                #soup = BeautifulSoup(open(page), 'html.parser')
                soup = BeautifulSoup(page, 'html.parser')

                anchorList = []
                for a in soup.find_all('a'):
                    try:
                        anchor = a['href']



                        anchor = remove_url_anchor(anchor)
                        if not str(anchor).startswith("#"):
                            if (domain == 'https://contracts.epa.gov') and ('node' in anchor):
                                anchor = urljoin(domain, anchor)
                            else:
                                anchor = urljoin(str(site.url), anchor)


                            if(' ' in anchor):
                                anchor = anchor.replace(' ', '%20')


                            if ((domain + siteName + '/') in anchor) and isSite(anchor):
                                if 'facebook' not in anchor and 'twitter' not in anchor and 'pinterest' not in anchor:
                                    if anchor not in anchorList:
                                        anchorList.append(anchor)
                    except KeyError:
                        pass
                        #print("keyerror with anchor: ")  # or some other fallback action

                # add domain and put to sitequeue
                for link in anchorList:
                    #print("link to add: " + link)

                    if str(link).startswith("/"):
                        wholeLink = domain + str(link)
                    elif ('https://' not in link) and ('http://' not in link):
                        wholeLink = domain + siteName +  '/' + link
                    else:
                        wholeLink = link

                    #print("Sitequeue Test : " + wholeLink)

                    wholeLinkObj = LinkObj(wholeLink, currentDepth+1)

                    if wholeLinkObj not in crawledList and wholeLinkObj not in siteQueue:
                        #print("Passed Sitequeue test: " + wholeLink)

                        siteQueue.append(wholeLinkObj)

                #print("(" + str(len(crawledList)) + " / " + str(len(siteQueue)) + ") crawled: " + site)

                time.sleep(sleeptime)
            except urllib.error.URLError:
                print("urlerror")
            except requests.exceptions.InvalidSchema:
                print("Invalid schema :" + site)
        elif crawltest is False:
            #print("don't crawl:" + site)
            badList.append(site)
        else:
            redirecturl = LinkObj(crawltest, currentDepth+1)

            #Add original URL to redirect list
            redirectList.append(site)
            #add new URL to crawl list IF IT HASN"T BEEN CRAWLED
            if redirecturl not in crawledList and redirecturl not in siteQueue:
                siteQueue.append(redirecturl)
                #check for domain?



            print("redirecting: " + site.url + " to " + redirecturl.url )

    currentPath = os.path.dirname(os.path.realpath(__file__))
    folderPath = currentPath + "\\crawledLinks"
    if (not os.path.exists(folderPath)):
        folder = currentPath + "\\crawledLinks"
        try:
            os.mkdir(folder)
        except OSError:
            print("Creation of the directory %s failed" % folder)
        else:
            print("Successfully created the directory %s " % folder)


    if (not os.path.exists(folderPath+ "\\crawledLinks\\intranet")):
        folder = currentPath + "\\crawledLinks\\intranet"
        try:
            os.mkdir(folder)
        except OSError:
            print("Creation of the directory %s failed" % folder)
        else:
            print("Successfully created the directory %s " % folder)


    if (not os.path.exists(folderPath+ "\\crawledLinks\\internet")):
        folder = currentPath + "\\crawledLinks\\internet"
        try:
            os.mkdir(folder)
        except OSError:
            print("Creation of the directory %s failed" % folder)
        else:
            print("Successfully created the directory %s " % folder)

    if (not os.path.exists(folderPath+ "\\crawledLinks\\smallsite")):
        folder = currentPath + "\\crawledLinks\\smallsite"
        try:
            os.mkdir(folder)
        except OSError:
            print("Creation of the directory %s failed" % folder)
        else:
            print("Successfully created the directory %s " % folder)

    f = open('crawledLinks//' + str(location) + "\\" + str(fileName) + ' Links.txt', 'w')
    f.write(indexUrl + " " + fileName + " " + siteName +'\n')


    for url in crawledList:
        if url not in badList:
            f.write(str(url.url) + '\n')


print("end")
