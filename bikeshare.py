import time
import pandas as pd
import numpy as np
import calendar     #Provide Useful Function Related To The Calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose a city from chicago, new york city, washington").lower().strip()
        if city not in CITY_DATA:
            print('Please choose a correct city name')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter a month from January to June, or type 'all' to dispaly all available months: ").lower().strip()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months and month != 'all':
            print("Please enter a correct month name")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a day of the week, or type 'all' to display all days: ").lower().strip()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day not in days and day != 'all':
            print("Please enter a correct day name")

    print('-'*40)
    return city, month, day


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
    #Load Data File Into DataFrame
    df = pd.read_csv(CITY_DATA[city])
    
    #Convert 'Start Time' Column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Add Two New Column 'month' and 'day_of_week' by extracting them from 'Start Time' Column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #Filter By Month
    if month != 'all':
        months = ['january', 'february', 'march', 'apri', 'may', 'june']
        month = months.index(month)+1
        
        #Filter By Month To Create New DataFrame
        df = df[ df['month'] == month ]
        
    #Filter By Day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def display_raw_data(df):
    """
        Display subsequent of raws of data according to user answer.
        Args:
            df - Pandas DataFrame containig city data filtered by month and day returned from load_data() function
    """
    i = 0
    answer = input('Would You Like to display the first 5 rows of the data? [yes/no]').lower()
    pd.set_option('display.max_columns',None)
    
    while True:
        if answer == 'no':
            break
        print(df[i:i+5])
        answer = input('Would You Like to display the next 5 rows of the data? [yes/no]').lower()
        i+=5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month: ',calendar.month_name[common_month])  #calendart used to get the name of month from the month number
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day: ',common_day) 
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common hour: ',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common Used Start Station: ',common_start )

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common Used Start Station: ',common_end )

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + '--' + df['End Station'])
    print('Most Frequent Combination Of Start Station and End Station Trip: ',common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time :',total_time + 'Seconds OR', total_time/(60*60), 'hours' )
    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print('Average Travel Time :',average_time + 'Seconds OR', average_time/(60*60), 'hours' )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Counts Of Users Type: ',count_user_type)      

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n Counts of Genders:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\n Earliest Year Of Birth:\n' ,earliest_birth_year )
        recent_birth_year = int(df['Birth Year'].max())
        print('\n Recent Year Of Birth:\n' ,recent_birth_year )
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\n Common Year Of Birth:\n' ,common_birth_year )
          
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
