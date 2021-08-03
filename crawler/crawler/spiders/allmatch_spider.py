import scrapy
from crawler.items import CrawlerItem


class AllMactchSpider(scrapy.Spider):           #klas
    name = "AllMatch"
    allowed_domains = ['openligadb.de']
    start_urls = [                                          #vzima url ot daden sait
        'https://api.openligadb.de/getmatchdata/bl1/2021'
    ]

    def parse(self, response):                 #metod
        item = CrawlerItem()                               #importvame klasa carawleritem() v item    
        jsonresponse = response.json()            #nz
        
        for AllMatches in jsonresponse:                  #cikul 

            item["Team1"] = AllMatches["team1"]["teamName"]    #vurti item postoqnno za da nameri danni na ime team1
            item["Team2"] = AllMatches["team2"]["teamName"]
            item["Data"] =  AllMatches["matchDateTime"]
            
            yield item
        print("-----------------------")
        print(item)
        print("--------------------------")

        

        #response.json()[0]["team1"]
        