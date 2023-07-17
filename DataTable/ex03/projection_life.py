import matplotlib.pyplot as plt
from load_csv import load

def draw_projection_for_year(year: str):
    """
    Draw a scatter plot of life expectancy vs GNP per capita for a given year.

    Args:
        year (str): The year for which the data will be plotted.

    Returns:
        None
    """
    # Load the datasets
    gnp_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")

    # Check if the data is loaded successfully
    if gnp_data is not None and life_expectancy_data is not None:
        # Filter the data for the specified year
        gnp_year = gnp_data[['country', year]]
        life_expectancy_year = life_expectancy_data[['country', year]]

        # Merge the two datasets on the 'country' column
        merged_data = gnp_year.merge(life_expectancy_year, on='country', how='inner')
        
        # Rename columns for clarity
        merged_data.columns = ['Country', 'GNP', 'Life Expectancy']

        # Plot
        plt.figure(figsize=(10, 6))
        plt.scatter(merged_data['GNP'], merged_data['Life Expectancy'])
        
        # Add title and labels
        plt.title(f'Life Expectancy vs GNP for Year {year}')
        plt.xlabel('GNP per Capita')
        plt.ylabel('Life Expectancy')
        
        # Show the plot
        plt.show()

    else:
        print("Unable to load one or both datasets.")

if (__name__ == "__main__"):
    draw_projection_for_year('1900')
