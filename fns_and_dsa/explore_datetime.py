from datetime import datetime,timedelta,date

def display_current_datetime():

    current_date = datetime.now()
    print("Current date and time:",current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():

    days = int(input("Enter the number of days: "))
    future_date = datetime.now() + timedelta(days= days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()