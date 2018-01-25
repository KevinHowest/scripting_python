import bs4
import urllib.request as request

#VRAAG 7

def splitDomains(domains_string):
    return(domains_string.split(','))

domains = splitDomains("RBD,PIWI,ERM,RA,DAM")

#VRAAG 8

def XMLrequest(domains_list):
    XML_list = []
    for domain in domains_list:
        url =  "http://pfam.xfam.org/family/" + domain + "?output=xml"
        
        with request.urlopen(url) as response:
            pfamXML = bs4.BeautifulSoup(response.read(),"html.parser")
        XML_list.append(pfamXML)
    return XML_list
XML = XMLrequest(domains)

#VRAAG 9

def extractFromXML(XML_list):
    for XML_string in XML_list:
        description = XML_string.select('description')
        GO_terms = XML_string.select('go_terms term')        
        count = 0
        print('description:', description[0].text.strip())
        
        #Loop over de verschillende GO termen, want er kunnen er meer zijn per domein
        for i in GO_terms:
            count += 1
            print('GO_term ' + str(count) + ': ' + i.text.strip())
    
extractFromXML(XML)