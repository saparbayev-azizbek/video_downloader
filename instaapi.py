import requests
def insta(url1):

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":url1}

    headers = {
        "X-RapidAPI-Key": "9b269e452cmsh4c8ccdbe239e2c1p10c768jsn2631883be2d7",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    res = response.json()
    return res

#  insta("https://www.instagram.com/p/C3B-FMoINhN/?igsh=azk1ZnJsdXRzOXlh")