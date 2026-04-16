import sys

from Timeline import Timeline

from PyQt5.QtWidgets import QApplication
from interface import TimelineWindow

file_path = "letterboxd-data-test/watched.csv"

def main():
  timeline = Timeline()
  timeline.get_data_from_csv(file_path)

  print(timeline)
  print(f"Total: {timeline.total_movies()}")

  app = QApplication(sys.argv)
  window = TimelineWindow()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()