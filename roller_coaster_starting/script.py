import pandas as pd
import matplotlib.pyplot as plt


# load rankings data here:
wood = pd.read_csv('roller_coaster_starting/Golden_Ticket_Award_Winners_Wood.csv')
print(wood.head())
steel = pd.read_csv('roller_coaster_starting/Golden_Ticket_Award_Winners_Steel.csv')
print(steel.head())
# print(wood[wood.Name == 'El Toro'])

# write function to plot rankings over time for 1 roller coaster here:
def coaster_ranking(coaster_name, park, ranking_df):
    year_list = ranking_df['Year of Rank'][ranking_df.Name == coaster_name][ranking_df.Park == park]
    rank_list = ranking_df['Rank'][ranking_df.Name == coaster_name][ranking_df.Park == park]
    plt.plot(year_list, rank_list, color='yellow')
    plt.title('{} Ranking by Year'.format(coaster_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.gca().invert_yaxis()
    plt.show()
# coaster_ranking('El Toro', 'Six Flags Great Adventure', wood)








plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_coasters(coaster_name1, coaster_name2, park1, park2, ranking_df):
    year_list1 = ranking_df['Year of Rank'][ranking_df.Name == coaster_name1][ranking_df.Park == park1]
    year_list2 = ranking_df['Year of Rank'][ranking_df.Name == coaster_name2][ranking_df.Park == park2]
    master_year_list = []
    for val in year_list1:
        master_year_list.append(val)
    for val in year_list2:
        if master_year_list.count(val) == 0:
            master_year_list.append(val)
    print(master_year_list)
    rank_list1 = ranking_df['Rank'][ranking_df.Name == coaster_name1][ranking_df.Park == park1]
    rank_list2 = ranking_df['Rank'][ranking_df.Name == coaster_name2][ranking_df.Park == park2]
    plt.plot(year_list1, rank_list1, color='red')
    plt.plot(year_list2, rank_list2, color='blue')
    plt.legend([coaster_name1, coaster_name2])
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('Two Coasters Rankings by Year')
    plt.gca().invert_yaxis()
    plt.show()
two_coasters('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce', wood)








plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
