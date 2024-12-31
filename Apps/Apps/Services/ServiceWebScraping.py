from dataclasses import dataclass


@dataclass
class ServiceWebScraping:
    urlBase: str = ""
    headers =  {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

    def PeticionGet(self):
        pass
