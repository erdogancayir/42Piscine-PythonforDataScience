import matplotlib.pyplot as plt
from load_csv import load

def draw_country_population(country1: str, country2: str):
    """
    Draw a line plot of the population over the years for two specified countries.

    Args:
        country1 (str): The name of the first country.
        country2 (str): The name of the second country.

    Returns:
        None
    """
    # Load the data
    data = load("population_total.csv")

    # Check if the data is loaded successfully
    if data is not None:
        # Check if the countries are in the data
        if country1 in data['country'].values and country2 in data['country'].values:
            # Filter the data for the specified countries
            country1_data = data[data['country'] == country1].drop('country', axis=1).T
            country2_data = data[data['country'] == country2].drop('country', axis=1).T
            
            # Limit data to years 1800 to 2050
            country1_data = country1_data.loc['1800':'2050']
            country2_data = country2_data.loc['1800':'2050']

            # Convert index to integer for plotting
            country1_data.index = country1_data.index.astype(int)
            country2_data.index = country2_data.index.astype(int)

            # Convert DataFrame to Series for correct plotting
            country1_data = country1_data.squeeze()
            country2_data = country2_data.squeeze()

            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(country1_data, label=country1)
            plt.plot(country2_data, label=country2)
            
            # Add title and labels
            plt.title(f'Population Over the Years in {country1} and {country2}')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.legend()
            
            # Show the plot
            plt.show()
        else:
            print("One or both countries not found in the dataset.")
    else:
        print("Unable to load the dataset.")

# Replace 'France' and 'Germany' with the countries you're interested in
if (__name__ == "__main__"):
    draw_country_population('Belgium', 'France')
