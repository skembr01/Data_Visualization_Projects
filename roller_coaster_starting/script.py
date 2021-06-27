from numpy import angle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
# print(wood.head())
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
# print(steel.head())
# print(wood[wood.Name == 'El Toro'])

# write function to plot rankings over time for 1 roller coaster here:
def coaster_ranking(coaster_name, park, ranking_df):
    year_list = ranking_df['Year of Rank'][ranking_df.Name == coaster_name][ranking_df.Park == park]
    rank_list = ranking_df['Rank'][ranking_df.Name == coaster_name][ranking_df.Park == park]
    plt.plot(year_list, rank_list, color='orange', lw='5')
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
# two_coasters('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce', wood)








plt.clf()

# write function to plot top n rankings over time here:









plt.clf()

# load roller coaster data here:
coaster = pd.read_csv('roller_coasters.csv')
# print(coaster.head(10))
# print(coaster.speed.dtype)


# write function to plot histogram of column values here:
def quant_hist(df):
    for col in df.columns:
        if df[col].dtype == 'float64':
            plt.clf()
            sns.histplot(x=df[col])
            plt.show()
# quant_hist(coaster)









plt.clf()

# write function to plot inversions by coaster at a park here:
def park_inversions(df, park_name):
    inversions = df['num_inversions'][df['park'] == park_name]
    print(inversions.head())
    coasters = df['name'][df['park'] == park_name]
    plt.clf()
    ax = sns.barplot(x=coasters, y=inversions, color='green')
    ax.set_xticklabels(coasters, rotation=10)
    plt.legend(coasters)
    plt.show()
        


park_inversions(coaster, 'Disneyland Park')







plt.clf()

# write function to plot pie chart of operating status here:
def operating_pie(coaster):
    labels = coaster['status'].unique()
    vals = coaster['status']
    for i in range(len(vals)):
        if vals[i] == vals[0]:
            vals[i] = 0
        elif vals[i] == vals[1]:
            vals[i] = 1
        elif vals[i] == vals[2]:
            vals[i] = 2
        elif vals[i] == vals[3]:
            vals[i] = 3
        elif vals[i] == vals[4]:
            vals[i] = 4
        elif vals[i] == vals[5]:
            vals[i] = 5
        elif vals[i] == vals[6]:
            vals[i] = 6
        elif vals[i] == vals[7]:
            vals[i] = 7
        elif vals[i] == vals[8]:
            vals[i] = 8
        else:
            vals[i] = 9
    plt.pie(vals)
    plt.legend(labels)
    plt.show()
    # return vals

# print(operating_pie(coaster))







plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
