from crawler import crawlPage
from websiteobj import WebsiteObj




internetSites = [WebsiteObj("https://www.epa.gov/faca",'faca',"https://www.epa.gov", "/faca", ".txt", "internet", False ),
               WebsiteObj("https://www.epa.gov/careers",'careers',"https://www.epa.gov", "/careers", ".txt", "internet", False ),
               WebsiteObj("https://www.epa.gov/grants",'grants',"https://www.epa.gov", "/grants", ".txt", "internet", False) ,
               WebsiteObj("https://www.epa.gov/nscep",'nscep',"https://www.epa.gov", "/nscep", ".txt", "internet", False),
               WebsiteObj("https://www.epa.gov/greeningepa", 'greeningepa', "https://www.epa.gov", "/greeningepa", ".txt", "internet", False) ]

intranetSites = [WebsiteObj("https://intranet.epa.gov/oarm/orbo/index.html",'orom',"https://intranet.epa.gov", "/oarm/orbo", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/ogd/",'ogd',"https://intranet.epa.gov", "/ogd", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/oarm/",'oarm',"https://intranet.epa.gov", "/oarm", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/oa/",'oa',"https://intranet.epa.gov", "/oa", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/ohr/",'ohr',"https://intranet.epa.gov", "/ohr", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/oarm/",'oarm',"https://intranet.epa.gov", "/oarm", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/oms/ei/",'oei',"https098879://intranet.epa.gov", "/oms/ei", ".txt", "intranet", True),
               WebsiteObj("https://contracts.epa.gov/",'contracts',"https://contracts.epa.gov", "", ".txt", "intranet", True) ,
               WebsiteObj("https://rtfusion.rtp.epa.gov/services/intranet/index.cfm", 'rtpfusion', "https://rtpfusion.rtp.epa.gov", "/services/intranet/index.cfm", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/rtp/", 'rtp', "https://intranet.epa.gov", "/rtp", ".txt", "intranet", True),
               WebsiteObj("https://rtfusion.rtp.epa.gov/services/intranet/index.cfm", 'rtp', "https://intranet.epa.gov", "/rtp", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/gis/  ", 'gis', "https://intranet.epa.gov", "/gis", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/forms/", 'forms', "https://intranet.epa.gov", "/forms", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/cpic/", 'cpic', "https://intranet.epa.gov", "/cpic", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/cx/", 'cx', "https://intranet.epa.gov", "/cx", ".txt", "intranet", True),
               WebsiteObj("https://intranet.epa.gov/oamintra/CPOD/",'CPOD',"https://intranet.epa.gov", "/oamintra/CPOD", ".txt", "intranet", True),
               WebsiteObj("https://purchasecard.epa.gov/",'purchasecard',"https://purchasecard.epa.gov", "", ".txt", "intranet", True),
               WebsiteObj("https://contracts.epa.gov/",'contracts',"https://contracts.epa.gov", "", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/potomacyard/",'potomacyard',"https://intranet.epa.gov", "/potomacyard", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/hqhs/",'hqhs',"https://intranet.epa.gov", "/hqhs", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/hqsecurity/",'hqsecurity',"https://intranet.epa.gov", "/hqsecurity", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/securitytraining/",'securitytraining',"https://intranet.epa.gov", "/securitytraining", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/ssd/",'ssd',"https://intranet.epa.gov", "/ssd", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/sustainablesolutions/",'sustainablesolutions',"https://intranet.epa.gov", "/sustainablesolutions", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/transportation/",'transportation',"https://intranet.epa.gov", "/transportation", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/desktop/",'desktop',"https://intranet.epa.gov", "/desktop", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/hqchem/",'hqchem',"https://intranet.epa.gov", "/hqchem", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/librarynetwork/",'librarynetwork',"https://intranet.epa.gov", "/librarynetwork", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/fdmsinfo/",'fdmsinfo',"https://intranet.epa.gov", "/fdmsinfo", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/icr/",'icr',"https://intranet.epa.gov", "/icr", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/records/",'records',"https://intranet.epa.gov", "/records", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/accessibility/",'accessibility',"https://intranet.epa.gov", "/accessibility", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/diversity/",'diversity',"https://intranet.epa.gov", "/diversity", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/policy/",'policy',"https://intranet.epa.gov", "/policy", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/cdx/",'cdx',"https://intranet.epa.gov", "/cdx", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/usability/",'usability',"https://intranet.epa.gov", "/usability", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/webdev/",'webdev',"https://intranet.epa.gov", "/webdev", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/privacy/",'privacy',"https://intranet.epa.gov", "/privacy", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/mobiledevices/",'mobiledevices',"https://intranet.epa.gov", "/mobiledevices", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/remoteaccess/",'remoteaccess',"https://intranet.epa.gov", "/remoteaccess", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/goanywhere/",'goanywhere',"https://intranet.epa.gov", "/goanywhere", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/myworkplaceinfo/",'myworkplaceinfo',"https://intranet.epa.gov", "/myworkplaceinfo", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/vdi/",'vdi',"https://intranet.epa.gov", "/vdi", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/rtpgis/",'rtpgis',"https://intranet.epa.gov", "/rtpgis", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/windows10/",'windows10',"https://intranet.epa.gov", "/windows10", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/atlassian/",'atlassian',"https://intranet.epa.gov", "/atlassian", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/faca/",'faca',"https://intranet.epa.gov", "/faca", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/oms/",'oms',"https://intranet.epa.gov", "/oms", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/ssc/",'ssc',"https://intranet.epa.gov", "/ssc", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/qic/",'qic',"https://intranet.epa.gov", "/qic", ".txt", "intranet", True),
WebsiteObj("https://cfint.rtpnc.epa.gov/oito/dss/index.cfm",'dds',"https://cfint.rtpnc.epa.gov", "/oito/dss", ".txt", "intranet", True),
WebsiteObj("https://cfint.rtpnc.epa.gov/oito/fdcci",'fdcci',"https://cfint.rtpnc.epa.gov", "/oito/fdcci", ".txt", "intranet", True),
WebsiteObj("https://cfint.rtpnc.epa.gov/oito/itarchitecture",'itarchitecture',"https://cfint.rtpnc.epa.gov", "/oito/itarchitecture", ".txt", "intranet", True),
WebsiteObj("https://cfint.rtpnc.epa.gov/oito/ittraining/index.cfm",'ittraining',"https://cfint.rtpnc.epa.gov", "/oito/ittraining", ".txt", "intranet", True),
WebsiteObj("https://cfint.rtpnc.epa.gov/oito/mailinglists/index.cfm",'mailinglists',"https://cfint.rtpnc.epa.gov", "/oito/mailinglists", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/eiam/",'eiam',"https://intranet.epa.gov", "/eiam", ".txt", "intranet", True),

                 ]


test = [
    #WebsiteObj("http://cincinnati.epa.gov/index.asp",'cinci',"https://cincinnati.epa.gov", "/", ".txt", "intranet", True),
WebsiteObj("https://intranet.epa.gov/securitytraining/",'securitytraining',"https://intranet.epa.gov", "/securitytraining", ".txt", "intranet", True),
WebsiteObj("https://cincinnati.epa.gov/",'cinci',"https://cincinnati.epa.gov", "", ".txt", "intranet", False),
WebsiteObj("https://intranet.epa.gov/hqhs/",'hqhs',"https://intranet.epa.gov", "/hqhs", ".txt", "intranet", False)


                 ]




#oamintra now contracts

allsites = test
#allsites = intranetSites + internetSites


for site in allsites:
    if site.active is True:
        crawlPage(site.url, site.domain, site.sitename, site.filename, site.folder)
    #print("done " + str(site.url))
