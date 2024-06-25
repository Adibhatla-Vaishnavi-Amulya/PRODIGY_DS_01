#Installing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
#Importing excel file
df=pd.read_excel(r"C:\Users\snmur\OneDrive\Desktop\Internship_Prodigy\Task - 01_Data.xls")
print(df.head(10))
top_10_least_populated=df.head(10)
#Extracting data for plotting
x=top_10_least_populated['COUNTRY NAME']
y=top_10_least_populated['POPULATION GROWTH PERCENTAGE']
#Bar graph customization
#Step:01 Plot the bar graph
plt.bar(x,y,color=("#E9967A","#8FBC8F","#483D8B","#696969","#CD5C5C","#20B2AA","#D2B48C","#ADD8E6","#DB7093","#9370DB"))
#Step:02 Define font properties
font1={"family":"serif","color":"#2F4F4F","weight":"bold","size":"20"}
font2={"family":"serif","color":"#2F4F4F","weight":"semibold","size":"15"}
#Step:03 Setting titles and labels
plt.title("Population growth percentage of least populated countries in 2022",fontdict=font1,loc="center")
plt.xlabel("Country",fontdict=font2,loc="center")
plt.ylabel("Population growth in %",fontdict=font2,loc="center")
#Step:04 Setting up grid properties
plt.grid(axis="both",color="#000000",linestyle="solid",linewidth=0.5)
#Step:05 Displaying the graph
plt.show()


