import random
import os
from datetime import datetime
def main():
    user_name = os.getlogin()
    print(f"Programmer:  '{user_name}'")
    time = datetime.now()
    date = time.strftime("%B %d, %Y @ %H:%M:%S")
    print(f'Lab 15.3 {date} \n')

    rain_list = []
    months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    total = 0
    highest = 0
    lowest = float(10)

    user = input("Enter your name: ")
    for month in months:
        rainfall = float(input(f"Enter the rainfall for {month}: "))
        rain_list.append(rainfall)
        total += rainfall
        if rainfall < lowest:
            lowest = rainfall
        if rainfall > highest:
            highest = rainfall
    average = total / 12
    print(f"\n{user}, here are the results:")
    print(f"Total rainfall: {total: .2f}")
    print(f"Average rainfall: {average: .2f}")
    print(f"Highest rainfall: {highest: .2f}")
    print(f"Lowest rainfall: {lowest: .2f}")

if __name__ == '__main__':
    main()