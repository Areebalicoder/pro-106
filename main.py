import numpy as np
import csv

def graph(path):
  with open(path) as csv_file:
    bh=csv.DictReader(csv_file)
    fig = px.scatter(bh, x="Temperature" , y="Ice-cream Sales( ₹ )")
    fig.show()

def get_dataStore(path):
  ice_S = []
  cold_S = []
  with open(path) as csv_file:
    bh=csv.DictReader(csv_file)
    for r in bh:
      ice_S.append(float(r["Temperature"]))
      cold_S.append(float(r["Ice-cream Sales( ₹ )"]))
  return{"x":ice_S,"y":cold_S}

def find_relation(path1):
  corelation = np.corrcoef(path1["x"],path1["y"])
  print(corelation[0,1])

path="data1.csv"
path1=get_dataStore(path)
find_relation(path1)
graph(path)
