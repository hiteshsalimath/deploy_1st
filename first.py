import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#loading dataset
data_iris = pd.read_csv("/home/hiteshsalimath/Documents/ADV_PYTHON/Datasets/Iris.csv")

#dataframe in website:
st.dataframe(data_iris)

# Display dataset description
st.write(data_iris.describe())

# Filter data for Setosa species
setosa = data_iris[data_iris['Species'] == 'Iris-setosa']

#hist
histo = st.selectbox('Select a Feature', data_iris.columns)
histo_x = st.selectbox('Select a Feature for X axis', data_iris.columns)
histo_y = st.selectbox('Select a Feature for Y axis', data_iris.columns)

fig, ax = plt.subplots()
ax.hist(data_iris[histo], bins=30)
ax.set_xlabel(histo)
ax.set_ylabel('Frequency')
st.pyplot(fig)


#scattar
feature = st.selectbox('select a feature', data_iris.columns)
feature_x = st.selectbox('Select feature for X axis', data_iris.columns)
feature_y = st.selectbox('Select feature for Y axis', data_iris.columns)
fig, ax = plt.subplots()
plt.scatter(data=data_iris, x = feature_x, y = feature_y, alpha=0.5)
st.pyplot(fig)


#3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
x = data_iris['SepalWidthCm']
y = data_iris['SepalLengthCm']

figure = ax.scatter(x,y)

ax.set_xlabel("sepal Width")
ax.set_ylabel("Sepal Length")
ax.set_zlabel("z-axis")
st.pyplot(fig)

#basemap

fig = plt.figure(figsize=(15,15))

m = Basemap()
m.drawcoastlines(linewidth = 1.0, linestyle = 'solid', color='black')
m.drawcountries(linewidth = 1.0, linestyle = 'solid', color='w')
m.drawmeridians(range(0,360,20), color = 'k', linewidth = 1.0, linestyle = 'dashed')
m.fillcontinents(color='maroon', lake_color = 'aqua')
m.drawmapboundary(color='k', linewidth=1.0, fill_color= 'lightblue', zorder=None, ax=None)
m.drawstates(linewidth=0.5, linestyle='solid', color='black', antialiased=1, ax=None, zorder=None)


x,y = m(80,22)
plt.plot(x,y,'ok',markersize = 2 , color = 'yellow')
plt.text(x,y,'INDIA',fontsize = 12, color = 'yellow')
plt.title("Coastline", fontsize = 20, pad = 30)
st.pyplot(fig)
