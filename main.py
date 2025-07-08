import requests

url = "https://www.tecan.com"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    scraped_html = response.text  # This is what we send to ChatGPT
else:
    scraped_html = ""
print(scraped_html)
