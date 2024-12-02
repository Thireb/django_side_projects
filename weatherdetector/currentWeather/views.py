from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=e55e5657f7b0b98a53e9a0b8b6216d6b').read()
        #print(len(res))
        json_data = json.loads(res)
        #print(json_data)
        data = {
            
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
            
        }
        
        #return render(request,'index.html',{'city':city})
    else:
        city = ''
        data = {}
    return render(request,'index.html',{'city':city, 'data':data})