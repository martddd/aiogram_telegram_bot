from datetime import datetime, timedelta


def main():
  date_now = datetime.now() + timedelta(hours=3)

  day = date_now.day
  month = date_now.month
  year = date_now.year

  hour = date_now.hour
  minute = date_now.minute

  print(f"Привет сейчас {hour}:{minute}")


if __name__ == "__main__":
  main()
