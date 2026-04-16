import csv

class Timeline(dict):
  def __init__(self):
    super().__init__({"1870s":0,"1880s":0,"1890s":0,
                      "1900s":0,"1910s":0,"1920s":0,"1930s":0,"1940s":0,"1950s":0,"1960s":0,"1970s":0,"1980s":0,"1990s":0,
                      "2000s":0,"2010s":0,"2020s":0})
  
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
  
  def get_data_from_csv(self, file_path):
    try:
      with open(file=file_path, mode="r", newline="") as file:
        reader = csv.reader(file)

        for line in reader:
          try:
            year = (int(line[2]) // 10) * 10
            key = f"{year}s"
            self[key] += 1
          except:
            pass
      return self

    except FileNotFoundError:
      return f"Error: File not found"