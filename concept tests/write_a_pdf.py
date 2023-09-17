import requests
import subprocess
url = "https://yakpdf.p.rapidapi.com/pdf"

payload = {
	"source": { "html": "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"></head><body><h1>Hello World!</h1></body></html>" },
	"pdf": {
		"format": "A4",
		"scale": 1,
		"printBackground": True
	},
	"wait": {
		"for": "navigation",
		"waitUntil": "load",
		"timeout": 2500
	}
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "bdcfc6c8bfmsh72e05c5c4aea2d7p143be8jsn82017204f123",
	"X-RapidAPI-Host": "yakpdf.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
subprocess.Popen(response, shell=True)
# print(response.json())