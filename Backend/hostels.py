import requests
import json
url = "https://airbnb19.p.rapidapi.com/api/v2/searchPropertyByPlaceId"

querystring = {"placeId":"ChIJ7cv00DwsDogRAMDACa2m4K8","adults":"1","guestFavorite":"false","ib":"false","currency":"KES"}

headers = {
	"x-rapidapi-key": "37056513c9mshd8900f4fddc5dc7p11fdfbjsn010d4f8b3106",
	"x-rapidapi-host": "airbnb19.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

with open('response.json', 'w') as f:
    json.dump(response.json(), f, indent=4)
    
print(response.json())