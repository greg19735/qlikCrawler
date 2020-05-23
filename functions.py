
import requests
import urllib


def remove_url_anchor(url):
    return url[:url.index('#')] if '#' in url else url

def checkLink(url):

    request = ""
    code= ""
    try:
        request = requests.get(url, verify=False, timeout=5)

        code = request.status_code
    except requests.exceptions.SSLError:
        code = "SSL Error"
        print("SSL Error")
    except requests.exceptions.ConnectionError:
        code = "Connection Error"
        print("no site")
    except KeyError:
        code = "Key Error"
        print("keyerror")
    except requests.exceptions.InvalidSchema:
        code = "Invalid Schema"
        print("invalid schema")
    except requests.exceptions.ReadTimeout:
        code = "Timeout"
        print("ReadTimeout")
    except urllib.error.HTTPError:
        code = "Forbidden"
        print("HTTP Error 403: Forbidden")
    except requests.exceptions.TooManyRedirects:
        code = "TooManyRedirects"
        print("Too Many Redirects")



    return code


def printresults(resultlist, filename, path):

    filelocname = path + '\\results\\' + str(filename) + '.txt'

    f = open(filelocname, 'w')

    f.write('OriginPage	LinkToPage	LinkToPageStatus	LinkToPageTitle	OriginPageDate	OriginPageTitle\n')

    for result in resultlist:
        try:
            if False:
                print(
                    "origin: " + result.originpage + '\t' + "LinkToPage: " + result.LinkToPage + '\t' + "LinkToPageStatus: " + str(result.LinkToPageStatus) + '\t' + "LinkToPageTitle: " + result.LinkToPageTitle + '\t' + "OriginPageDate: " + result.OriginPageDate + '\t' + "OriginPageTitle: " + result.OriginPageTitle + '\n')

            f.write(
                removeNonAscii(result.originpage.strip()) + '\t' + removeNonAscii(result.LinkToPage.strip()) + '\t' + str(result.LinkToPageStatus).strip() + '\t' + removeNonAscii(result.LinkToPageTitle.strip()) + '\t' + removeNonAscii(result.OriginPageDate.strip()) + '\t' + removeNonAscii(result.OriginPageTitle.strip()) + '\n')

        except UnicodeEncodeError:
            print("it's a unicode error")
    f.close()



def printNow(resultlist, filename, path):

    filelocname = path + '\\results\\' + str(filename) + '.txt'

    f = open(filelocname, 'w')

    f.write('OriginPage	LinkToPage	LinkToPageStatus	LinkToPageTitle	OriginPageDate	OriginPageTitle\n')

    for result in resultlist:
        try:
            if False:
                print(
                    "origin: " + result.originpage + '\t' + "LinkToPage: " + result.LinkToPage + '\t' + "LinkToPageStatus: " + str(result.LinkToPageStatus) + '\t' + "LinkToPageTitle: " + result.LinkToPageTitle + '\t' + "OriginPageDate: " + result.OriginPageDate + '\t' + "OriginPageTitle: " + result.OriginPageTitle + '\n')

            f.write(
                removeNonAscii(result.originpage.strip()) + '\t' + removeNonAscii(result.LinkToPage.strip()) + '\t' + str(result.LinkToPageStatus).strip() + '\t' + removeNonAscii(result.LinkToPageTitle.strip()) + '\t' + removeNonAscii(result.OriginPageDate.strip()) + '\t' + removeNonAscii(result.OriginPageTitle.strip()) + '\n')

        except UnicodeEncodeError:
            print("it's a unicode error")
    f.close()

def isURL(stringTest):
    URL = False
    if str(stringTest).startswith('https://'):
        URL = True
    elif str(stringTest).startswith('http://'):
        URL = True
    elif str(stringTest).startswith('www.'):
        URL = True
    elif '.com' in stringTest:
        URL = True
    elif '.gov' in stringTest:
        URL = True
    elif '.test' in stringTest:
        URL = True

    return URL

def isSite(url):
    bool = True
    if str(url).endswith('.pdf'):
        bool = False
    elif str(url).endswith('.wmv'):
        bool = False
    elif str(url).endswith('.doc'):
        bool = False
    elif str(url).endswith('.docx'):
        bool = False
    elif str(url).endswith('.ppt'):
        bool = False
    elif str(url).endswith('.pptx'):
        bool = False

    return bool



def pageToCrawl(url):
    crawl = False
    code= ""
    try:
        request = requests.get(url, verify=False)
        #print(request.headers['Content-Type'])
        print(request.status_code)

        print(request.headers['Content-Type'])
        if request.headers['Content-Type']:

           if (request.status_code is 200) and (str(request.headers['Content-Type']).startswith('text/html')):
               if request.url != url:
                   crawl = request.url
                   print("redirect")
               else:
                   crawl = True
           else:
                print("code: " + str(request.status_code) +" not crawling: " + url + "file type; "+ request.headers['Content-Type'])

    except requests.exceptions.SSLError:
        print("SSL Error")
    except requests.exceptions.ConnectionError:
        print("no site")
    except KeyError:
        print("keyerror")
    except requests.exceptions.InvalidSchema:
        print("invalid schema")
    except urllib.error.HTTPError:
        print("403 error forbidden.")
    except requests.exceptions.MissingSchema:
        print("missing schema")


    return crawl


def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
