
import datetime
from datetime import datetime, timedelta
current_date = datetime.now()

def display_current_datetime():
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
 
display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(number_of_days)
    print(future_date.strftime("%Y-%m-%d"))

calculate_future_date()

