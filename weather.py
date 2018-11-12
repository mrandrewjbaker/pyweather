#! /usr/bin/python3
import os
import requests
import time

request = requests


refreshTime = os.environ.get('REFRESH_TIME', 2)


class weatherConfig:
    pass


class apiInformation:
    pass

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
        
    else:
        _ = os.system('clear')


def setApiInformation():
    setPostalCode = 'http://api.openweathermap.org/data/2.5/weather?zip={},'.format(weatherConfig.zip)
    setRegion = setPostalCode + '{}'.format(weatherConfig.region)
    setOpenWeather = setRegion
    apiInformation.openWeather = setOpenWeather
    apiInformation.apiKey = '&appid=7751c2d608d40feecf0e2ea229aa371e'



# Have user set loop    
def setWeatherLoop():
    queryLoop = input('Do you want to continously update the weather? Y or N ').lower()
   
    if queryLoop == 'y':
       weatherConfig.weatherLoopOn = True
       
    
    elif queryLoop == 'n':
        weatherConfig.weatherLoopOn = False


# Have user set location based on zip
def setLocation():
    weatherConfig.region = input('Enter your region (us,de, jp, etc): ')
    weatherConfig.zip = input('Enter your postal code: ')

    
    

# Have user set unit F or C
def setUnit():
    queryUnit = input('What unit would you like to use? F or C: ').lower()
    
    if queryUnit == 'c':
        weatherConfig.unit = '&units=metric'
        
        
        
    elif queryUnit == 'f':
        weatherConfig.unit = '&units=imperial'
        
    else:
        print('You have entered an invalid unit')
        setUnit()





# Have user set their config: loop?, zip?, unit?  
def setWeatherConfig():
    setWeatherLoop()
    setLocation()
    setUnit() 





def weatherLoop():
    
    while weatherConfig.weatherLoopOn == True:
        global currentTime
        currentTime = str(time.time())
        
        getWeather();
        
        time.sleep(int(refreshTime))
    pass
    


def getWeather():
    

    url = apiInformation.openWeather + apiInformation.apiKey + weatherConfig.unit
    
    
    response = request.get(url)
    
    data = response.json()
    
    
    temp = data['main']['temp']
    temp = str(temp)
    
    city = data['name']
    
    weatherStatement = "It is " + temp + ' ' + 'in ' + city
    
    if weatherConfig.weatherLoopOn == True:
        print(weatherStatement, end='\r', flush=True)
    else:
        print(weatherStatement)
    
    



def main():

    setWeatherConfig()
    
    setApiInformation()
    
    clear()
    
    weatherLoop()
    
    getWeather()

main()