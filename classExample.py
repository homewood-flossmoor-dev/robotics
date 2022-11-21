from datetime import date

class Christmas:
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
      print("THERE ARE: ")
  #calculate them by hardcoding xmas date
  #substraction of the days
  def calculateDays(self):
    christmas_day = date(self.year, self.month, self.day)
    days_for_xmas = (christmas_day - date.today()).days
    return  days_for_xmas
  #print days
  def printDays(self):
    d = self.calculateDays()
    print(str(d) + " DAYS UNTIL BIRTHDAY!")

month = int(input("month in number pls"))
year = int(input("year"))
day = int(input("day"))

if month <= 0 or month > 12:
    print("Invalid month")
else:
    xmasDays = Christmas(year, month, day)
    xmasDays.printDays()
