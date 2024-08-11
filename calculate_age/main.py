from datetime import datetime

def calculate_age(dob):
    today = datetime.today()
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    
    # Calculate the age in years
    age_years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age_years -= 1
    
    # Calculate the age in days, minutes, and seconds
    age_days = (today - birth_date).days
    age_seconds = (today - birth_date).total_seconds()
    age_minutes = age_seconds / 60
    
    return age_years, age_days, age_minutes, age_seconds

# Get user input for date of birth
dob = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    age_years, age_days, age_minutes, age_seconds = calculate_age(dob)
    print(f"Your age is: {age_years} years")
    print(f"Your age in days: {age_days} days")
    print(f"Your age in minutes: {age_minutes:.2f} minutes")
    print(f"Your age in seconds: {age_seconds:.2f} seconds")
except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
