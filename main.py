import sys
import requests
import csv

""" file_path = "letterboxd-data-test/watched.csv"
api_key = "42af91267b3fbbe8742a22c7ff38af3c"
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
  print("Cannot find the file") """

file_path = "letterboxd-data-test/watchlist.csv"

class Timeline(dict):
  def __str__(self):
    output = ""
    for k in self.keys():
      output += f"{k}: {self[k]}\n"
    return output
  def total_movies(self):
    total = 0
    for k in self.values():
      total += k
    return total

timeline = Timeline({"1870s":0,"1880s":0,"1890s":0,
            "1900s":0,"1910s":0,"1920s":0,"1930s":0,"1940s":0,"1950s":0,"1960s":0,"1970s":0,"1980s":0,"1990s":0,
            "2000s":0,"2010s":0,"2020s":0})

try:
  with open(file=file_path, mode="r", newline="") as file:
    reader = csv.reader(file)

    for line in reader:
      try:
        year = (int(line[2]) // 10) * 10
        key = f"{year}s"
        timeline[key] += 1
      except:
        pass

except FileNotFoundError:
  print("Cannot find the file")

print(timeline)
print(timeline.total_movies())