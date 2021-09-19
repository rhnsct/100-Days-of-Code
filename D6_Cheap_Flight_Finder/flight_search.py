import os
import requests as rq

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        
        self.api_key = str(os.environ.get("FS_API"))
        self.url = "https://tequila-api.kiwi.com/"

    def location_search(self, cities):
        
        url = self.url + "locations/query"

        emp_list = []

        for city in cities:
            parameters = {
            "apikey": self.api_key,
            "term": city,
            "location_types": "city",
            "limit": 1,

            }

            request = rq.get(url, params=parameters)
            emp_list.append(request)
        
        return emp_list
    
    def location_handle(self, cities):

        list_cities = self.location_search(cities)

        list_codes = {city["locations"][0]["name"]: "code" for city in list_cities}
                    

        

    pass