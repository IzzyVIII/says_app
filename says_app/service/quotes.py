import requests

class QuotesService:
    @classmethod
    def get_quote(cls):
        url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

        querystring = {"token":"ipworld.info"}

        headers = {
            "X-RapidAPI-Key": "eef55b325bmsh1305927ed1bb23fp1557f3jsn2558bca4e9a8",
            "X-RapidAPI-Host": "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()