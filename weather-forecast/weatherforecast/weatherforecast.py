import requests
import urllib3
urllib3.disable_warnings()

class Weather:
    """
        Creates a weather object getting an apikey as input and either a city or lat and lon coordinates
    """
    def __init__(self,apikey,city=None,lat=None,lon=None):
        if city:
            url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=metric'
            req = requests.get(url,verify = False)
            self.data = req.json()
        elif lat and lon:
            url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=metric'
            req = requests.get(url,verify = False)
            self.data = req.json()
        else:
            raise TypeError("Provide  either city name or it's coordinates")
        
        if self.data['cod'] != "200":
            raise ValueError(self.data['message'])
            
    def next_day(self):
        return self.data['list'][:8]
    
    def next_day_simplified(self):
        for single_check in self.data['list'][:8]:
            print(single_check['dt_txt'], round(single_check['main']['temp']),single_check['weather'][0]['description'])
            
    def next_3_days_simplified(self):
        counter =0
        for single_check in self.data['list'][:24]:
            print(single_check['dt_txt'], round(single_check['main']['temp']),single_check['weather'][0]['description'])
            counter +=1
            if counter in [8,16]:
                print('Next 24 hours')

    
    
