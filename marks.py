import plotly.express as px
import csv
import numpy as np


#inversely related when one value goes up other one comes down-eg- coffee consumption increase hours of sleep decrease


def plotFigure(data_path): #plots the graph
   with open(data_path) as csv_file:
    df=csv.DictReader(csv_file)
    fig= px.scatter(df, x="Marks In Percentage",y="Days Present") 
    fig.show()


def getDataSource(data_path):
  marks=[]
  attendance=[]
  with open(data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
           marks.append(float(row["Marks In Percentage"])) #adds intake in the var
           attendance.append(float(row["Days Present"]))#adds hours in var
    
  return{"x": marks, "y":attendance} #x is intake and y is sleep



def findCorrelation(datasource):
    coorelation=np.corrcoef(datasource["x"], datasource["y"]) # giving us how much coorelated or not #coorcoef is coefficient coorealtion #x axis is the temperature, y avis is the sales
    print(f"Coorelation b/w marks and number of days present- {coorelation[0,1]}") #print the coorelation the index is the aise hii toh get the value

def setup():
    data_path= "marks.csv"
    datasource=getDataSource(data_path) #returning dictioniary is stored in datasource dictionary
    findCorrelation(datasource) #passing this to get the coorealtion of datasource
    plotFigure(data_path)#plots the graph

setup()