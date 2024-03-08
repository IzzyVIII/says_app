import requests

class QuotesService:
    @classmethod
    def get_quote(cls):
        url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

        querystring = {"token":"ipworld.info"}

        headers = {
            "X-RapidAPI-Key": "a545654756msh41215968af0133ap15acf5jsneb67a6cb1e2e",
            "X-RapidAPI-Host": "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()