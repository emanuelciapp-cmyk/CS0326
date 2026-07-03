import requests

BASE_URL = "http://192.168.50.101"

def check_methods(path):
    url = BASE_URL + path
    response = requests.options(url)
    allowed = response.headers.get("Allow", "No Allow header found")
    print(f"Metodi abilitati su {path}: {allowed}")

if __name__ == "__main__":
    path = input("Inserisci il path da controllare: ")
    check_methods(path)
