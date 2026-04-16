import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
file_path = "letterboxd-data-test/watched.csv"
url = "https://api.themoviedb.org/3/search/movie"

try:
  with open(file=file_path, mode="r", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
      #print(f"{line[1]} | {line[2]}")
      params = {
          "api_key": api_key,
          "query": line[1],
      }

      response = requests.get(url, params=params)
      data = response.json()

      for movie in data["results"]:
        if movie["release_date"]: # as vezes o tmdb pode retornar filme sem data
          year = movie["release_date"][:4]
          if movie["title"].lower() == line[1].lower() and year == line[2]:
            print(f"{movie['title']} | {year} | {movie['id']}")

except FileNotFoundError:
  print("Cannot find the file")