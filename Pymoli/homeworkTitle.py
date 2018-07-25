
#dependencies
import pandas as pd
import numpy as np[InternetShortcut]
URL=http://localhost:8889/notebooks/Pymoli_Pandas_HW.ipynb#


#map to the path of data set
data_file = "purchase_data.csv"

# read the file with pandas data frame; pymoli_df["Price"] = pymoli_df["Price"].map("${:.2f}".format)...
#if used, error in average price calc as can't characterize string to float!!!!

pymoli_df = pd.read_csv(data_file)

pymoli_df.head()

# # Player Count total Number of Players
total_players = pymoli_df ["SN"].nunique()
print("Number of total players " + str(total_players))

###Purchase Analysis (Total)---------------------------------------------------------------------------------------------------

#Number of Unique Items
unique_items = len(pymoli_df["Item ID"].unique())
unique_items

# Average Purchase Price; can't convert to to_numeric function
average_price = pymoli_df["Price"].mean()
average_price

#Total Number of Purchases
number_of_purchases = len(pymoli_df)
number_of_purchases

#Total Revenue
total_revenue = pymoli_df ["Price"].sum()
total_revenue

###***purchasing Analysis (Total) summary_df1
df1 = pd.DataFrame({
    "Number of Unique Items": [unique_items],
    "Average Price" :[average_price],
    "Number of Purchases" :[number_of_purchases],
    "Total Revenue" :[total_revenue],
})
                                    
df1.head()

###Gender Demographics----------------------------------------------------------------------------------------------------------

# Count of Male, Female, Other/ Non-Disclosed Players
gender_count = pymoli_df ["Gender"].value_counts()
gender_count

#Gender Percentage
gender_percentage = (gender_count/total_players)*100
gender_percentage.round(2)

###***Gender Demographic summary_df2
df2 = pd.DataFrame({"Gender Count": gender_count, "Gender Percentage": gender_percentage.round(2)})
    
df2.head()

###Purchasing Analysis (Gender)-------------------------------------------------------------------------------------------------

#Purchase Count by Gender
Purchase_Count_by_Gender = pymoli_df.groupby("Gender")["SN"].count()

Purchase_Count_by_Gender

#Average Purchase Price by Gender
Average_Purchase_Price_by_Gender = pymoli_df.groupby("Gender")["Price"].mean()
Average_Purchase_Price_by_Gender.round(2)

#Total Purchase Value by Gender
Total_Purchase_Value_by_Gender = pymoli_df.groupby("Gender")["Price"].sum()
Total_Purchase_Value_by_Gender.round(2)

#Average Purchase Total per Person by Gender
Average_Purchase_Total_perPerson_by_Gender = Total_Purchase_Value_by_Gender/ gender_count
Average_Purchase_Total_perPerson_by_Gender.round(2)

###***Purchasing Analysis (Gender)_df3

#Purchasing Analysis by Gender
df3 = pd.DataFrame({"Purchase Count" : Purchase_Count_by_Gender, 
                    "Average Purchase Price" : Average_Purchase_Price_by_Gender.round(2),
                    "Total Purchase Value" : Total_Purchase_Value_by_Gender, 
                    "Avg Purchase Total per Person" : Average_Purchase_Total_perPerson_by_Gender.round(2)})

df3.head()
                    

### Age Demographics * The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)

#Establish bins for age groups

age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]

group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"] 

#Categorize the existing players using the age bins. Hint: use pd.cut()

pymoli_df["Age Groups"] = pd.cut(pymoli_df["Age"], age_bins, labels = group_names)
pymoli_df.head()

#Calculate count per age group

count_per_age_group = pymoli_df.groupby("Age Groups")["SN"].count()

count_per_age_group

# Calculate percentage of age grp count

AgeGroups_percentage = (count_per_age_group/total_players)*100
AgeGroups_percentage.round(2)

#summary data with Percentage of Players and Total Count_df4

df4 = pd.DataFrame({"Player Percentage per age group" : AgeGroups_percentage.round(2), 
                    "Age Group Count" : count_per_age_group})

df4                    

# Purchase Count by age group
purchase_count = pymoli_df.groupby("Age Groups")["SN"].count()
purchase_count

# Average Purchase Price by Age Groups

Average_Purchase_Price_by_Age_Groups = pymoli_df.groupby("Age Groups")["Price"].mean()
Average_Purchase_Price_by_Age_Groups.round(2)


# Total Purchase Value

Total_Purchase_Price_by_Age_Groups = pymoli_df.groupby("Age Groups")["Price"].sum()
Total_Purchase_Price_by_Age_Groups.round(2)


# Average Purchase Total per Person by Age Group

Average_Purchase_Total_per_Person_per_Age_Groups = Total_Purchase_Price_by_Age_Groups/count_per_age_group
Average_Purchase_Total_per_Person_per_Age_Groups.round(2)

#Purchase Analysis (Age)_df5

df5 = pd.DataFrame({"Purchase Count" : purchase_count, 
                    "Average Purchase Price" : Average_Purchase_Price_by_Age_Groups.round(2), 
                    "Total Purchase Value" : Total_Purchase_Price_by_Age_Groups, 
                    "Average Purchase Total per Person": Average_Purchase_Total_per_Person_per_Age_Groups.round(2)})
df5.head(10)

### Top Five Spenders

# Purchase_Count by All
df6 = pymoli_df ["SN"].value_counts()
df6


# Total Purchase Price by All

df7 = pymoli_df.groupby ("SN")["Price"].sum()

df7

# Average Purchase Price by All
df8 = df7/df6
df8

#create spender_df9 with df6, df7, df8

df9 = pd.DataFrame({"Purchase Count": df6,
                    "Average Purchase Price" : df8,
                    "Total Purchase Value": df7})

df9.head()

# Identify the the top 5 spenders in the game by total purchase value

Top_five_spenders = df9.sort_values(["Total Purchase Value"], ascending=False)
Top_five_spenders.head()


# MOST POPULAR item analysis

# Purchase Count
df10 = pymoli_df.groupby(["Item ID", "Item Name"])["SN"].count()

#Item Price
df11 = pymoli_df.groupby(["Item ID", "Item Name"])["Price"].mean()

#Total Purchase Value
df12 = pymoli_df.groupby(["Item ID", "Item Name"])["Price"].sum()

# Convert to DataFrame

df13 = pd.DataFrame({"Purchase Count":df10,
                     "Item Price":df11,
                     "Total Purchase Value":df12,
                    })

df13.head()

Most_Popular_items = df13.sort_values(["Purchase Count"], ascending=False)
Most_Popular_items.head()

Most_Profitable_items = df13.sort_values(["Total Purchase Value"], ascending=False)
Most_Profitable_items.head()

### Three observable trends based on the data:

# * Most Players are Male and most purchases are made by Male; they contributed to almost 83% of revenue. 
# * Most players and buyers are in age group range 20-24 years; almost 63.4% of total players are in this age group.
# * Most popular item was also the most profitable item, "Oathbreaker, Last Hope of the Breaking Storm"