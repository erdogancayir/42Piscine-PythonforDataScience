import matplotlib.pyplot as plt
from load_csv import load

def draw_country_life_expectancy(country: str):
    """
    Draw a line plot of the life expectancy over the years for a specified country.

    Args:
        country (str): The name of the country.

    Returns:
        None
    """
    # Load the data
    data = load("life_expectancy_years.csv")

    # Check if the data is loaded successfully
    if data is not None:
        # Check if the country is in the data
        if country in data['country'].values:
            # Filter the data for the specified country
            country_data = data[data['country'] == country]

            # Drop the 'country' column
            country_data = country_data.drop('country', axis=1)
            
            # Transpose the DataFrame for better plotting
            country_data = country_data.T

            # Convert index to integer for plotting
            country_data.index = country_data.index.astype(int)

            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(country_data)
            
            # Add title and labels
            plt.title(f'Life Expectancy Over the Years in {country}')
            plt.xlabel('Year')
            plt.ylabel('Life Expectancy')
            
            # Show the plot
            plt.show()
        else:
            print(f"{country} not found in the dataset.")
    else:
        print("Unable to load the dataset.")

# Replace 'France' with the country you're interested in
if (__name__ == "__main__"):
    draw_country_life_expectancy('Turkey')
