"""
Script with solutions for all workspace assignments in the Bivariate
Exploration of Data lesson.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def scatterplot_solution_1():
    """
    Solution for Question 1 in scatterplot practice: create a scatterplot of
    city vs. highway fuel mileage.
    """
    sol_string = ["Most of the data falls in a large blob between 10 and 30 mpg city",
                  "and 20 to 40 mpg highway. Some transparency is added via 'alpha'",
                  "to show the concentration of data. Interestingly, for most cars",
                  "highway mileage is clearly higher than city mileage, but for those",
                  "cars with city mileage above about 30 mpg, the distinction is less",
                  "pronounced. In fact, most cars above 45 mpg city have better",
                  "city mileage than highway mileage, contrary to the main trend. It",
                  "might be good to call out this trend by adding a diagonal line to",
                  "the figure using the `plot` function. (See the solution file for that code!)"]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('./data/fuel_econ.csv')

    plt.scatter(data = fuel_econ, x = 'city', y = 'highway', alpha = 1/8)
    # plt.plot([10,60], [10,60]) # diagonal line from (10,10) to (60,60)
    plt.xlabel('City Fuel Eff. (mpg)')
    plt.ylabel('Highway Fuel Eff. (mpg)')


def scatterplot_solution_2():
    """
    Solution for Question 2 in scatterplot practice: create a heat map of
    engine displacement vs. co2 production.
    """
    sol_string = ["In the heat map, I've set up a color map that goes from light",
                  "to dark, and made it so that any cells without count don't get",
                  "colored in. The visualization shows that most cars fall in a",
                  "line where larger engine sizes correlate with higher emissions.",
                  "The trend is somewhat broken by those cars with the lowest emissions,",
                  "which still have engine sizes shared by most cars (between 1 and 3 liters)."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('./data/fuel_econ.csv')

    bins_x = np.arange(0.6, fuel_econ['displ'].max()+0.4, 0.4)
    bins_y = np.arange(0, fuel_econ['co2'].max()+50, 50)
    plt.hist2d(data = fuel_econ, x = 'displ', y = 'co2', bins = [bins_x, bins_y], 
               cmap = 'viridis_r', cmin = 0.5)
    plt.colorbar()
    plt.xlabel('Displacement (l)')
    plt.ylabel('CO2 (g/mi)')


def violinbox_solution_1():
    """
    Solution for Question 1 in violin and box plot practice: plot the relationship
    between vehicle class and engine displacement.
    """
    sol_string = ["I used a violin plot to depict the data in this case; you might",
                  "have chosen a box plot instead. One of the interesting things",
                  "about the relationship between variables is that it isn't consistent.",
                  "Compact cars tend to have smaller engine sizes than the minicompact",
                  "and subcompact cars, even though those two vehicle sizes are smaller.",
                  "The box plot would make it easier to see that the median displacement",
                  "for the two smallest vehicle classes is greater than the third quartile",
                  "of the compact car class."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('./data/fuel_econ.csv')

    sedan_classes = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars', 'Midsize Cars', 'Large Cars']
    pd_ver = pd.__version__.split(".")
    if (int(pd_ver[0]) > 0) or (int(pd_ver[1]) >= 21): # v0.21 or later
        vclasses = pd.api.types.CategoricalDtype(ordered = True, categories = sedan_classes)
        fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses)
    else: # pre-v0.21
        fuel_econ['VClass'] = fuel_econ['VClass'].astype('category', ordered = True,
                                                         categories = sedan_classes)

    # plotting
    base_color = sb.color_palette()[0]
    sb.violinplot(data = fuel_econ, x = 'VClass', y = 'displ',
                  color = base_color)
    plt.xticks(rotation = 15)


def categorical_solution_1():
    """
    Solution for Question 1 in categorical plot practice: plot the relationship
    between vehicle class and fuel type.
    """
    sol_string = ["I chose a clustered bar chart instead of a heat map in this case",
                  "since there weren't a lot of numbers to plot. If you chose a heat",
                  "map, did you remember to add a color bar and include annotations?",
                  "From this plot, you can see that more cars use premium gas over",
                  "regular gas, and that the smaller cars are biased towards the",
                  "premium gas grade. It is only in midsize sedans where regular",
                  "gasoline was used in more cars than premium gasoline."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('./data/fuel_econ.csv')
    
    sedan_classes = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars', 'Midsize Cars', 'Large Cars']
    pd_ver = pd.__version__.split(".")
    if (int(pd_ver[0]) > 0) or (int(pd_ver[1]) >= 21): # v0.21 or later
        vclasses = pd.api.types.CategoricalDtype(ordered = True, categories = sedan_classes)
        fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses)
    else: # pre-v0.21
        fuel_econ['VClass'] = fuel_econ['VClass'].astype('category', ordered = True,
                                                         categories = sedan_classes)
    fuel_econ_sub = fuel_econ.loc[fuel_econ['fuelType'].isin(['Premium Gasoline', 'Regular Gasoline'])]

    # plotting
    ax = sb.countplot(data = fuel_econ_sub, x = 'VClass', hue = 'fuelType')
    ax.legend(loc = 4, framealpha = 1) # lower right, no transparency
    plt.xticks(rotation = 15)


def additionalplot_solution_1():
    """
    Solution for Question 1 in additional plots practice: plot the distribution
    of combined fuel efficiencies for each manufacturer with at least 80 cars.
    """
    sol_string = ["Due to the large number of manufacturers to plot, I've gone",
                  "with a faceted plot of histograms rather than a single figure",
                  "like a box plot. As part of setting up the FacetGrid object, I",
                  "have sorted the manufacturers by average mileage, and wrapped",
                  "the faceting into a six column by three row grid. One interesting",
                  "thing to note is that there are a very large number of BMW cars",
                  "in the data, almost twice as many as the second-most prominent",
                  "maker, Mercedes-Benz. One possible refinement could be to change",
                  "the axes to be in terms of relative frequency or density to",
                  "normalize the axes, making the less-frequent manufacturers",
                  "easier to read."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('./data/fuel_econ.csv')

    most_makes = fuel_econ['make'].value_counts().index[:18]
    fuel_econ_sub = fuel_econ.loc[fuel_econ['make'].isin(most_makes)]

    make_means = fuel_econ_sub.groupby('make').mean()
    comb_order = make_means.sort_values('comb', ascending = False).index

    # plotting
    g = sb.FacetGrid(data = fuel_econ_sub, col = 'make', col_wrap = 6, size = 2,
                     col_order = comb_order)
    # try sb.distplot instead of plt.hist to see the plot in terms of density!
    g.map(plt.hist, 'comb', bins = np.arange(12, fuel_econ_sub['comb'].max()+2, 2))
    g.set_titles('{col_name}')


def additionalplot_solution_2():
    """
    Solution for Question 2 in additional plots practice: plot the average
    combined fuel efficiency for each manufacturer with at least 80 cars.
    """
    sol_string = ["Seaborn's barplot function makes short work of this exercise.",
                  "Since there are a lot of 'make' levels, I've made it a horizontal",
                  "bar chart. In addition, I've set the error bars to represent the",
                  "standard deviation of the car mileages."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('./data/fuel_econ.csv')

    most_makes = fuel_econ['make'].value_counts().index[:18]
    fuel_econ_sub = fuel_econ.loc[fuel_econ['make'].isin(most_makes)]

    make_means = fuel_econ_sub.groupby('make').mean()
    comb_order = make_means.sort_values('comb', ascending = False).index

    # plotting
    base_color = sb.color_palette()[0]
    sb.barplot(data = fuel_econ_sub, x = 'comb', y = 'make',
               color = base_color, order = comb_order, ci = 'sd')
    plt.xlabel('Average Combined Fuel Eff. (mpg)')