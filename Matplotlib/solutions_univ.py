"""
Script with solutions for all workspace assignments in the Univariate
Exploration of Data lesson.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def bar_chart_solution_1():
    """
    Solution for Question 1 in bar chart practice: create a bar chart of
    Pokemon species introduced by generation.
    """
    sol_string = ["I used seaborn's countplot function to generate this chart.",
                  "I also added an additional argument so that each bar has the same color."]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('./data/pokemon.csv')

    base_color = sb.color_palette()[0]
    sb.countplot(data = pokemon, x = 'generation_id', color = base_color)


def bar_chart_solution_2():
    """
    Solution for Question 2 in bar chart practice: create a sorted bar chart of
    relative type frequencies.
    """
    sol_string = ["I created a horizontal bar chart since there are a lot of",
                  "Pokemon types. The unique() method was used to get the",
                  "number of different Pokemon species. I also added an xlabel",
                  "call to make sure it was clear the bar length represents",
                  "a relative frequency."]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('./data/pokemon.csv')
    pkmn_types = pokemon.melt(id_vars = ['id','species'], 
                          value_vars = ['type_1', 'type_2'], 
                          var_name = 'type_level', value_name = 'type').dropna()

    # get order of bars by frequency
    type_counts = pkmn_types['type'].value_counts()
    type_order = type_counts.index

    # compute largest proportion
    n_pokemon = pkmn_types['species'].unique().shape[0]
    max_type_count = type_counts[0]
    max_prop = max_type_count / n_pokemon

    # establish tick locations and create plot
    base_color = sb.color_palette()[0]
    tick_props = np.arange(0, max_prop, 0.02)
    tick_names = ['{:0.2f}'.format(v) for v in tick_props]

    base_color = sb.color_palette()[0]
    sb.countplot(data = pkmn_types, y = 'type', color = base_color, order = type_order)
    plt.xticks(tick_props * n_pokemon, tick_names)
    plt.xlabel('proportion')


def histogram_solution_1():
    """
    Solution for Question 1 in histogram practice: create a histogram of
    Pokemon special defense values.
    """
    sol_string = ["I've used matplotlib's hist function to plot the data.",
                  "I have also used numpy's arange function to set the bin edges.",
                  "A bin size of 5 hits the main cut points, revealing a smooth,",
                  "but skewed curves. Are there similar characteristics among",
                  "Pokemon with the highest special defenses?"]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('./data/pokemon.csv')

    bins = np.arange(20, pokemon['special-defense'].max()+5, 5)
    plt.hist(pokemon['special-defense'], bins = bins)


def scales_solution_1():
    """
    Solution for Question 1 in scales and transformation practice: create a
    histogram of Pokemon heights.
    """
    sol_string = ["There's a very long tail of Pokemon heights. Here, I've",
                  "focused in on Pokemon of height 6 meters or less, so that I",
                  "can use a smaller bin size to get a more detailed look at",
                  "the main data distribution."]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('./data/pokemon.csv')

    bins = np.arange(0, pokemon['height'].max()+0.2, 0.2)
    plt.hist(data = pokemon, x = 'height', bins = bins)
    plt.xlim((0,6))


def scales_solution_2():
    """
    Solution for Question 2 in scales and transformation practice: create a
    histogram of Pokemon weights.
    """
    sol_string = ["Since Pokemon weights are so skewed, I used a log transformation",
                  "on the x-axis. Bin edges are in increments of 0.1 powers of ten,",
                  "with custom tick marks to demonstrate the log scaling."]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('./data/pokemon.csv')

    bins = 10 ** np.arange(-1, 3.0+0.1, 0.1)
    ticks = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
    labels = ['{}'.format(val) for val in ticks]

    plt.hist(data = pokemon, x = 'weight', bins = bins)
    plt.xscale('log')
    plt.xticks(ticks, labels)
    plt.xlabel('Weight (kg)')
