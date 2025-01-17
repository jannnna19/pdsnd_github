import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

from ast import Break


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       cities =["chicago", 'new york city', 'washington']   
       city = input('Please Ener the name of City you want to explore').lower()
       if city not in cities:
        print("invalid inpu")
       else:
           break
    # get user input for month (all, january, february, ... , june)
    while True:
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     month = input("please select the month \n January , February, March , April, May, June, all").lower()
     if month not in months:
      print("invalid inpu")
     else:
          break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
     days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
     day = input("please select the days \n from sunday to saturday ").lower()
     if day not in days:
      print("invalid inpu")
     else:
          break

    print('-'*40)
    return city,month,day
     

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_Month = df['month'].mode()[0]
    print('Most Common Month:',common_Month)

    # TO DO: display the most common day of week
    common_dow =df['day_of_week'].mode()[0]
    print('Most Common DOW:',common_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_Shour= df['hour'].mode()[0]
    print('Most Common Start Hour:',common_Shour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_st = df['Start Station'].mode()[0]
    print("the most commonly used start station is ", start_st)

    # TO DO: display most commonly used end station
    end_st = df['End Station'].mode()[0]
    print("the most commonly used End station is", end_st)

    # TO DO: display most frequent combination of start station and end station trip

    combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(combination.split("||")))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print("Total Travel Time:",total_time)

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print("Avrage Travel Time:",mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of user types \n ",df["User Type"].value_counts());

    # TO DO: Display counts of gender
    if 'gender' in df:
      print("count of user gender \n ",df["Gender"].value_counts());

    # TO DO: Display earliest, most recent, and most common year of birth


def user_stats_birthyeare(df):
    if 'Birth Year' in df:
     birth_year=df['Birth Year']
    # the most common birth year
     most_common_year = birth_year.value_counts().idxmax()
     print("The most common birth year:{}").format(most_common_year)
    # the most recent birth year
     most_recent = birth_year.max()
     print("The most recent birth year:{}").format(most_recent)
    # the most earliest birth year
     earliest_year = birth_year.min()
     print("The most earliest birth year:{}").format(earliest_year)

     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)
    
def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        

def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)
       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)
       display_data(df)

       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
