import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", color='blue')

    # Create first line of best fit for all data
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = pd.Series(range(1880, 2051))
    y1 = res1.slope * x1 + res1.intercept
    plt.plot(x1, y1, 'r', label='Fit: All Data')

    # Create second line of best fit from year 2000
    df_recent = df[df["Year"] >= 2000]
    res2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x2 = pd.Series(range(2000, 2051))
    y2 = res2.slope * x2 + res2.intercept
    plt.plot(x2, y2, 'green', label='Fit: 2000-Present')

    # Customize plot
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.grid(True)

    # Save and return
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
