from crawler import crawlPage
from websiteobj import WebsiteObj




internetSites = [WebsiteObj("https://www.epa.gov/faca",'faca',"https://www.epa.gov", "/faca", ".txt", "internet", True),
               WebsiteObj("https://www.epa.gov/contracts",'contracts',"https://www.epa.gov", "/contracts", ".txt", "internet", True),
               WebsiteObj("https://www.epa.gov/careers",'careers',"https://www.epa.gov", "/careers", ".txt", "internet", True),
               WebsiteObj("https://www.epa.gov/grants",'grants',"https://www.epa.gov", "/grants", ".txt", "internet", True),
               WebsiteObj("https://www.epa.gov/nscep",'nscep',"https://www.epa.gov", "/nscep", ".txt", "internet", True),
               WebsiteObj("https://www.epa.gov/greeningepa", 'greeningepa', "https://www.epa.gov", "/greeningepa", ".txt", "internet", True) ]

intranetSites = [WebsiteObj("https://intranet.epa.gov/oarm/orbo/index.html",'orom',"https://intranet.epa.gov", "/oarm/orbo", ".txt", "intranet", False),
               WebsiteObj("https://intranet.epa.gov/ogd/",'ogd',"https://intranet.epa.gov", "/ogd", ".txt", "intranet", False),
               WebsiteObj("https://intranet.epa.gov/oarm/",'oarm',"https://intranet.epa.gov", "/oarm", ".txt", "intranet", False),
               WebsiteObj("https://intranet.epa.gov/oa/",'oa',"https://intranet.epa.gov", "/oa", ".txt", "intranet", False),
               WebsiteObj("https://intranet.epa.gov/ohr/",'ohr',"https://intranet.epa.gov", "/ohr", ".txt", "intranet", False),
               WebsiteObj("https://contracts.epa.gov/",'contracts',"https://contracts.epa.gov", "", ".txt", "intranet", False),
               WebsiteObj("https://oamintra.epa.gov/node/27",'oamintra',"https://oamintra.epa.gov", "", ".txt", "intranet", False),
               WebsiteObj("https://www.epa.gov/greeningepa", 'greeningepa', "https://www.epa.gov", "/greeningepa", ".txt", "intranet", False) ]

allsites = internetSites + intranetSites


for site in allsites:
    if site.active is True:
        crawlPage(site.url, site.domain, site.sitename, site.filename)
    #print("done " + str(site.url))