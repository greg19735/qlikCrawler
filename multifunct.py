from functions import checkLink
from result import Result
import time

#multithread functions

def linkCheckThread (testlink, resultDict, allResults, link, siteTitle, linkResults, newlinkindex):

    #how long to wait based network strain

    #wait in seconds
    waitTime = .02


    #not tested
    if testlink.url.startswith("https://") or testlink.url.startswith("http://"):

        #IF URL THAT NEEDS TESTING, PAUSE.
        time.sleep(newlinkindex * waitTime)

        print("Checking :" + testlink.url)
        code = checkLink(testlink.url)
        result = Result(link, testlink.url, code, testlink.anchortext, "date", siteTitle )
        allResults.append(result)
        resultDict[testlink.url] = code
    else:
        result = Result(link, testlink.url, "non url", testlink.anchortext, "date", siteTitle)

    linkResults.append(result)


def noCheckThread (testlink, resultDict, allResults, link, siteTitle, linkResults ):
    code = resultDict[testlink.url]
    result = Result(link, testlink.url, code, testlink.anchortext, "date", siteTitle)
    linkResults.append(result)