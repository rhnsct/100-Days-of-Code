import requests as rq
import os


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:

        self.url = str(os.environ.get('SHEET_URL')) + 'flightDeals/prices'

    def get_sheet(self):


        request = rq.get(self.url)
        return request.json()


