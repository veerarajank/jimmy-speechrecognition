from urllib import response
import requests
import json
class covidstats:
    url="https://covid-193.p.rapidapi.com/statistics"
    headers={
            "x-rapidapi-host": "covid-193.p.rapidapi.com",
            "x-rapidapi-key": "782dec1a54mshd130381f5ab1905p1768c2jsn46a9ec6a9bdf"
        }
    dict_val=dict()
    ## Add the key and value in dictionary
    def add(self,key,value):
        self.dict_val[key]=value
    ## get the values from API
    def gethttp(self,query_string):
        response=requests.request("GET",self.url,headers=self.headers,params=query_string)
        return response
    ## get covid stats based on country
    def covidstatscall(self,country):
        query_string={"country":country}
        jsonobj=json.loads(self.gethttp(query_string).text)["response"][0]
        self.add("active",jsonobj["cases"]["active"])
        self.add("critical",jsonobj["cases"]["critical"])
        return self.dict_val
        
    