# # # from django.shortcuts import render
# # # import requests

# # # def index(request):
# # #     api_key = '5a017a7e4a82cc77a41e222836657d7b'
# # #     city = request.GET.get('city','London')
# # #     url = f"https://api.openweathermap.org/weather/2.5/weather?q={city}&appid={api_key}&units=metric"
# # #     response = requests.get(url)
# # #     weather = response.json()
# # #     print(weather)

# # #     if response.status_code == 200 and 'main' in weather:
# # #             context = {
# # #                 'city': city,
# # #                 'temperature': weather['main']['temp'],
# # #                 'description': weather['weather'][0]['description'],
# # #                 # 'icon': weather['weather'][0]['icon'],
# # #                 # 'humidity': weather['main']['humidity'],
# # #                 # 'wind_speed': weather['wind']['speed'],
# # #             }
# # #     else:
# # #             context = {
# # #                  'error': weather.get('message','city not found'),
# # #             }

# # #     return render(request, 'weather/index.html', context)

# # from django.shortcuts import render
# # import requests

# # def index(request):
# #     api_key = '5a017a7e4a82cc77a41e222836657d7b'
# #     city = request.GET.get('city', 'London')
# #     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# #     response = requests.get(url)

# #     # 🔍 Add a check before .json()
# #     if response.status_code == 200:
# #         try:
# #             weather = response.json()
# #             context = {
# #                 'city': city,
# #                 'temperature': weather['main']['temp'],
# #                 'description': weather['weather'][0]['description'],
# #                 'icon': weather['weather'][0]['icon'],
# #                 'humidity': weather['main']['humidity'],
# #                 'wind_speed': weather['wind']['speed'],
# #             }
# #         except ValueError:
# #             context = {'error': 'Failed to decode weather data.'}
# #     else:
# #         context = {
# #             'error': f"API error {response.status_code}: {response.text}"
# #         }

# #     return render(request, 'weather/index.html', context)



# from django.shortcuts import render
# import requests

# def index(request):
#     api_key = '5a017a7e4a82cc77a41e222836657d7b'
#     city = request.GET.get('city', 'London')
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#     print("Fetching weather for:", city)
#     print("API URL:", url)

#     try:
#         response = requests.get(url)
#         print("Status Code:", response.status_code)
#         print("Raw Response:", response.text)  # 👈 Print this!

#         if response.status_code == 200:
#             try:
#                 weather = response.json()
#                 context = {
#                     'city': city,
#                     'temperature': weather['main']['temp'],
#                     'description': weather['weather'][0]['description'],
#                     'icon': weather['weather'][0]['icon'],
#                     'humidity': weather['main']['humidity'],
#                     'wind_speed': weather['wind']['speed'],
#                 }
#             except ValueError as e:
#                 print("JSON decode error:", e)
#                 context = {'error': 'Could not decode weather data from API.'}
#         else:
#             context = {
#                 'error': f"API error {response.status_code}: {response.text}"
#             }

#     except requests.RequestException as e:
#         print("Request failed:", e)
#         context = {'error': 'Failed to connect to the weather service.'}

#     return render(request, 'weather/index.html', context)
    
from django.shortcuts import render
import requests

def index(request):
    api_key = '5a017a7e4a82cc77a41e222836657d7b'
    weather = {}

    if request.method == 'POST':
        city = request.POST.get('city', 'London')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            print("Status:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:
                data = response.json()
                weather = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                }
            else:
                weather = {
                    'error': f"City not found or API error. ({response.status_code})"
                }
        except Exception as e:
            weather = {
                'error': f"Error fetching data: {e}"
            }

    return render(request, 'weather/index.html', {'weather': weather})
