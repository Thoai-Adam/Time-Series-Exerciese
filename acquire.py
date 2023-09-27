import pandas as pd
import requests

# Function to acquire people data from SWAPI
def acquire_people_data():
    url = 'https://swapi.dev/api/people/'
    # Make API request and parse JSON response
    response = requests.get(url)
    data = response.json()
    # Create a DataFrame from the data
    people_df = pd.DataFrame(data['results'])
    # Save to a CSV file
    people_df.to_csv('people.csv', index=False)

# Function to acquire planets data from SWAPI
def acquire_planets_data():
    # Similar process as above for planets data
    url = 'https://swapi.dev/api/planets/'
    # Make API request and parse JSON response
    response = requests.get(url)
    data = response.json()
    # Create a DataFrame from the data
    planets_df = pd.DataFrame(data['results'])
    # Save to a CSV file
    planets_df.to_csv('planets.csv', index=False)

# Function to acquire starships data from SWAPI
def acquire_starships_data():
    # Similar process as above for starships data
    url = 'https://swapi.dev/api/starships/'
    # Make API request and parse JSON response
    response = requests.get(url)
    data = response.json()
    # Create a DataFrame from the data
    starships_df = pd.DataFrame(data['results'])
    # Save to a CSV file
    starships_df.to_csv('starships.csv', index=False)

# Function to combine data from separate DataFrames
def combine_data():
    people_df = pd.read_csv('people.csv')
    planets_df = pd.read_csv('planets.csv')
    starships_df = pd.read_csv('starships.csv')
    # Combine the DataFrames as needed
    combined_df = pd.concat([people_df, planets_df, starships_df], axis=0)
    return combined_df

# Function to acquire Open Power Systems Data for Germany
def acquire_german_power_data():
    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
    # Use pandas to read data from the URL into a DataFrame
    german_power_df = pd.read_csv(url)
    return german_power_df

if __name__ == "__main__":
    # Call your functions to acquire and process data as needed
    acquire_people_data()
    acquire_planets_data()
    acquire_starships_data()
    combined_data = combine_data()
    german_power_data = acquire_german_power_data()
    # Perform further data analysis or processing as required
