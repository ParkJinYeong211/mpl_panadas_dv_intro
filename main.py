import pandas as pd
from matplotlib import pyplot as plt

country_data = pd.read_csv('countries.csv')
us = country_data[country_data.country == "United States"]
china = country_data[country_data.country == "China"]

plt.plot(us.year, -100 + 100 * us.population / us.population.iloc[0])
plt.plot(china.year, -100 + 100 * china.population / china.population.iloc[0])
plt.legend(["United States", "China"])
plt.xlabel("Year")
plt.ylabel("Population Growth (%)")
plt.title("Population of China and United States")

plt.show()