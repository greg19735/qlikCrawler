from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
from functions import pageToCrawl
from functions import isSite
from functions import remove_url_anchor
import time
import requests


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sleeptime = 0.5

def crawlPage(startSite, domain, siteName, fileName):

    siteQueue = []
    crawledList = []
    badList = []   #for URLS that don't need to be printed
    redirectList = [] #List or URLS that are redirects to make sure they're not checked again.

    linkcount = 0
    siteQueue.append(startSite)

    while siteQueue:
        site = siteQueue.pop()
        crawledList.append(site)
        print("site: " + site)


        crawltest = pageToCrawl(site)
        if crawltest is True:


            try:

                page = urllib.request.urlopen(site)
                #page = "C:\\Users\\greg\\PycharmProjects\\crawler\\example.html"
                #soup = BeautifulSoup(open(page), 'html.parser')
                soup = BeautifulSoup(page, 'html.parser')

                anchorList = []
                for a in soup.find_all('a'):
                    try:
                        anchor = a['href']



                        anchor = remove_url_anchor(anchor)
                        if not str(anchor).startswith("#"):
                            if (domain == 'https://oamintra.epa.gov') and ('node' in anchor):
                                anchor = urljoin(domain, anchor)
                            else:
                                anchor = urljoin(site, anchor)


                            if(' ' in anchor):
                                anchor = anchor.replace(' ', '%20')


                            if ((domain + siteName + '/') in anchor) and isSite(anchor):
                                if 'facebook' not in anchor and 'twitter' not in anchor and 'pinterest' not in anchor:
                                    if anchor not in anchorList:
                                        anchorList.append(anchor)
                    except KeyError:
                        print("keyerror with anchor: ")  # or some other fallback action

                # add domain and put to sitequeue
                for link in anchorList:
                    print("link to add: " + link)

                    if str(link).startswith("/"):
                        wholeLink = domain + str(link)
                    elif ('https://' not in link) and ('http://' not in link):
                        wholeLink = domain + siteName +  '/' + link
                    else:
                        wholeLink = link

                    print("Sitequeue Test : " + wholeLink)

                    if wholeLink not in crawledList and wholeLink not in siteQueue:
                        print("Passed Sitequeue test: " + wholeLink)
                        siteQueue.append(wholeLink)

                print("(" + str(len(crawledList)) + " / " + str(len(siteQueue)) + ") crawled: " + site)

                time.sleep(sleeptime)
            except urllib.error.URLError:
                print("urlerror")
            except requests.exceptions.InvalidSchema:
                print("Invalid schema :" + site)
        elif crawltest is False:
            #print("don't crawl:" + site)
            badList.append(site)
        else:
            redirecturl = crawltest
            #Add original URL to redirect list
            redirectList.append(site)
            #add new URL to crawl list IF IT HASN"T BEEN CRAWLED
            if redirecturl not in crawledList and redirecturl not in siteQueue:
                siteQueue.append(redirecturl)
                #check for domain?



            print("redirecting: " + site + " to " + redirecturl )


    f = open('files/' + str(fileName) + ' Links.txt', 'w')
    f.write(startSite + " " + fileName + " " + siteName +'\n')


    for url in crawledList:
        if url not in badList:
            f.write(str(url) + '\n')


print("end")
