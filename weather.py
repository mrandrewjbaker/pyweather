import requests


zip = input('Enter your zip code: ')
openWeather = 'http://api.openweathermap.org/data/2.5/weather?zip={},us'.format(zip)
apiKey = '&appid=7751c2d608d40feecf0e2ea229aa371e'




def getWeather(unit):

    url = openWeather + apiKey + unit
    
    res = requests.get(url)
    
    data = res.json()
    
    temp = data['main']['temp']
    temp = str(temp)
    
    city = data['name']
    
    print("It is " + temp + ' ' + 'in ' + city)


def chooseUnit():
    queryUnit = input('What unit would you like to use? F or C: ').lower()
    
    if queryUnit == 'c':
        unit = '&units=metric'
        
        getWeather(unit)
        
    elif queryUnit == 'f':
        unit = '&units=imperial'
        
        getWeather(unit)
        
    else:
        print('You have entered an invalid unit')
        chooseUnit()

        

def main():
    chooseUnit()
    

main()