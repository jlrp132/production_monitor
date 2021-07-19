# Get this figure: fig = py.get_figure("https://plotly.com/~zoo-dataset1/57/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~zoo-dataset1/57/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="canlendarheatmap", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~zoo-dataset1/57/").get_data()[0]["y"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "name": ["2-Sep 77.95 kLperday", "3-Sep 68.46 kLperday", "4-Sep 69.07 kLperday", "5-Sep 70.68 kLperday", "6-Sep 71.37 kLperday", "7-Sep 76.94 kLperday", "8-Sep 69.13 kLperday", "9-Sep 66.77 kLperday", "10-Sep 67.46 kLperday", "11-Sep 67.39 kLperday", "12-Sep 69.23 kLperday", "13-Sep 72.05 kLperday", "14-Sep 68.08 kLperday", "15-Sep 66.16 kLperday", "16-Sep 67.39 kLperday", "17-Sep 66.60 kLperday", "18-Sep 73.07 kLperday", "19-Sep 68.35 kLperday", "20-Sep 68.22 kLperday", "21-Sep 73.99 kLperday", "22-Sep 69.90 kLperday", "23-Sep 72.30 kLperday", "24-Sep 69.46 kLperday", "25-Sep 72.09 kLperday", "26-Sep 64.28 kLperday", "27-Sep 67.94 kLperday", "28-Sep 73.99 kLperday", "29-Sep 84.70 kLperday", "30-Sep 83.43 kLperday", "1-Oct 85.58 kLperday", "2-Oct 81.03 kLperday", "3-Oct 77.55 kLperday", "4-Oct 82.24 kLperday", "5-Oct 80.46 kLperday", "6-Oct 78.74 kLperday", "7-Oct 91.38 kLperday", "8-Oct 76.90 kLperday", "9-Oct 29.41 kLperday", "10-Oct 35.28 kLperday", "11-Oct 41.75 kLperday", "12-Oct 41.68 kLperday", "13-Oct 38.07 kLperday", "14-Oct 33.19 kLperday", "15-Oct 37.57 kLperday", "16-Oct 35.12 kLperday", "17-Oct 33.86 kLperday", "18-Oct 35.57 kLperday", "19-Oct 35.67 kLperday", "20-Oct 35.26 kLperday", "21-Oct 72.61 kLperday", "22-Oct 72.07 kLperday", "23-Oct 36.01 kLperday", "24-Oct 33.79 kLperday", "25-Oct 34.07 kLperday", "26-Oct 33.30 kLperday", "27-Oct 35.20 kLperday", "28-Oct 30.27 kLperday", "29-Oct 35.09 kLperday", "30-Oct 31.20 kLperday", "31-Oct 35.22 kLperday", "1-Nov 33.10 kLperday", "2-Nov 33.54 kLperday", "3-Nov 34.87 kLperday", "4-Nov 34.57 kLperday", "5-Nov 36.65 kLperday", "6-Nov 38.37 kLperday", "7-Nov 29.40 kLperday", "8-Nov 34.01 kLperday", "9-Nov 36.39 kLperday", "10-Nov 38.05 kLperday", "11-Nov 38.01 kLperday", "12-Nov 40.56 kLperday", "13-Nov 39.52 kLperday", "14-Nov 43.32 kLperday", "15-Nov 38.62 kLperday", "16-Nov 39.97 kLperday", "17-Nov 38.91 kLperday", "18-Nov 39.62 kLperday", "19-Nov 34.31 kLperday", "20-Nov 34.68 kLperday", "21-Nov 40.51 kLperday", "22-Nov 45.14 kLperday", "23-Nov 37.24 kLperday", "24-Nov 39.02 kLperday", "25-Nov 36.55 kLperday", "26-Nov 36.10 kLperday", "27-Nov 42.59 kLperday", "28-Nov 38.35 kLperday", "29-Nov 35.51 kLperday", "30-Nov 34.52 kLperday", "1-Dec 35.37 kLperday", "2-Dec 39.53 kLperday", "3-Dec 40.23 kLperday", "4-Dec 35.27 kLperday", "5-Dec 24.67 kLperday", "6-Dec 31.47 kLperday", "7-Dec 34.63 kLperday", "8-Dec 33.38 kLperday", "9-Dec 33.72 kLperday", "10-Dec 34.68 kLperday", "11-Dec 42.30 kLperday", "12-Dec 29.46 kLperday", "13-Dec 35.38 kLperday", "14-Dec 32.94 kLperday", "15-Dec 35.43 kLperday", "16-Dec 33.00 kLperday", "17-Dec 33.80 kLperday", "18-Dec 37.24 kLperday", "19-Dec 36.43 kLperday", "20-Dec 33.49 kLperday", "21-Dec 38.19 kLperday"], 
  "type": "heatmap", 
  "x": [36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 51, 52], 
  "y": [3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1], 
  "zmax": 91.38, 
  "zmin": 0, 
  "z": [77.95, 68.46, 69.07, 70.68, 71.37, 76.94, 69.13, 66.77, 67.46, 67.39, 69.23, 72.05, 68.08, 66.16, 67.39, 66.6, 73.07, 68.35, 68.22, 73.99, 69.9, 72.3, 69.46, 72.09, 64.28, 67.94, 73.99, 84.7, 83.43, 85.58, 81.03, 77.55, 82.24, 80.46, 78.74, 91.38, 76.9, 29.41, 35.28, 41.75, 41.68, 38.07, 33.19, 37.57, 35.12, 33.86, 35.57, 35.67, 35.26, 72.61, 72.07, 36.01, 33.79, 34.07, 33.3, 35.2, 30.27, 35.09, 31.2, 35.22, 33.1, 33.54, 34.87, 34.57, 36.65, 38.37, 29.4, 34.01, 36.39, 38.05, 38.01, 40.56, 39.52, 43.32, 38.62, 39.97, 38.91, 39.62, 34.31, 34.68, 40.51, 45.14, 37.24, 39.02, 36.55, 36.1, 42.59, 38.35, 35.51, 34.52, 35.37, 39.53, 40.23, 35.27, 24.67, 31.47, 34.63, 33.38, 33.72, 34.68, 42.3, 29.46, 35.38, 32.94, 35.43, 33, 33.8, 37.24, 36.43, 33.49, 38.19], 
  "inherit": False, 
  "text": ["2-Sep 77.95 kLperday", "3-Sep 68.46 kLperday", "4-Sep 69.07 kLperday", "5-Sep 70.68 kLperday", "6-Sep 71.37 kLperday", "7-Sep 76.94 kLperday", "8-Sep 69.13 kLperday", "9-Sep 66.77 kLperday", "10-Sep 67.46 kLperday", "11-Sep 67.39 kLperday", "12-Sep 69.23 kLperday", "13-Sep 72.05 kLperday", "14-Sep 68.08 kLperday", "15-Sep 66.16 kLperday", "16-Sep 67.39 kLperday", "17-Sep 66.60 kLperday", "18-Sep 73.07 kLperday", "19-Sep 68.35 kLperday", "20-Sep 68.22 kLperday", "21-Sep 73.99 kLperday", "22-Sep 69.90 kLperday", "23-Sep 72.30 kLperday", "24-Sep 69.46 kLperday", "25-Sep 72.09 kLperday", "26-Sep 64.28 kLperday", "27-Sep 67.94 kLperday", "28-Sep 73.99 kLperday", "29-Sep 84.70 kLperday", "30-Sep 83.43 kLperday", "1-Oct 85.58 kLperday", "2-Oct 81.03 kLperday", "3-Oct 77.55 kLperday", "4-Oct 82.24 kLperday", "5-Oct 80.46 kLperday", "6-Oct 78.74 kLperday", "7-Oct 91.38 kLperday", "8-Oct 76.90 kLperday", "9-Oct 29.41 kLperday", "10-Oct 35.28 kLperday", "11-Oct 41.75 kLperday", "12-Oct 41.68 kLperday", "13-Oct 38.07 kLperday", "14-Oct 33.19 kLperday", "15-Oct 37.57 kLperday", "16-Oct 35.12 kLperday", "17-Oct 33.86 kLperday", "18-Oct 35.57 kLperday", "19-Oct 35.67 kLperday", "20-Oct 35.26 kLperday", "21-Oct 72.61 kLperday", "22-Oct 72.07 kLperday", "23-Oct 36.01 kLperday", "24-Oct 33.79 kLperday", "25-Oct 34.07 kLperday", "26-Oct 33.30 kLperday", "27-Oct 35.20 kLperday", "28-Oct 30.27 kLperday", "29-Oct 35.09 kLperday", "30-Oct 31.20 kLperday", "31-Oct 35.22 kLperday", "1-Nov 33.10 kLperday", "2-Nov 33.54 kLperday", "3-Nov 34.87 kLperday", "4-Nov 34.57 kLperday", "5-Nov 36.65 kLperday", "6-Nov 38.37 kLperday", "7-Nov 29.40 kLperday", "8-Nov 34.01 kLperday", "9-Nov 36.39 kLperday", "10-Nov 38.05 kLperday", "11-Nov 38.01 kLperday", "12-Nov 40.56 kLperday", "13-Nov 39.52 kLperday", "14-Nov 43.32 kLperday", "15-Nov 38.62 kLperday", "16-Nov 39.97 kLperday", "17-Nov 38.91 kLperday", "18-Nov 39.62 kLperday", "19-Nov 34.31 kLperday", "20-Nov 34.68 kLperday", "21-Nov 40.51 kLperday", "22-Nov 45.14 kLperday", "23-Nov 37.24 kLperday", "24-Nov 39.02 kLperday", "25-Nov 36.55 kLperday", "26-Nov 36.10 kLperday", "27-Nov 42.59 kLperday", "28-Nov 38.35 kLperday", "29-Nov 35.51 kLperday", "30-Nov 34.52 kLperday", "1-Dec 35.37 kLperday", "2-Dec 39.53 kLperday", "3-Dec 40.23 kLperday", "4-Dec 35.27 kLperday", "5-Dec 24.67 kLperday", "6-Dec 31.47 kLperday", "7-Dec 34.63 kLperday", "8-Dec 33.38 kLperday", "9-Dec 33.72 kLperday", "10-Dec 34.68 kLperday", "11-Dec 42.30 kLperday", "12-Dec 29.46 kLperday", "13-Dec 35.38 kLperday", "14-Dec 32.94 kLperday", "15-Dec 35.43 kLperday", "16-Dec 33.00 kLperday", "17-Dec 33.80 kLperday", "18-Dec 37.24 kLperday", "19-Dec 36.43 kLperday", "20-Dec 33.49 kLperday", "21-Dec 38.19 kLperday"], 
  "colorbar": {"title": "vol(kL)"}, 
  "hoverinfo": "text", 
  "colorbar.1": {"title": "values"}, 
  "colorscale": [
    [0, "#440154"], [0.111111111111111, "#482878"], [0.222222222222222, "#3E4A89"], [0.333333333333333, "#31688E"], [0.444444444444445, "#26828E"], [0.555555555555556, "#1F9E89"], [0.666666666666667, "#35B779"], [0.777777777777778, "#6DCD59"], [0.888888888888889, "#B4DE2C"], [1, "#FDE725]
}
data = Data([trace1])
layout = {
  "title": "Calendar Heatmap of Daily Consumption", 
  "xaxis": {
    "title": "", 
    "mirror": True, 
    "ticklen": 0, 
    "showline": True, 
    "tickmode": "array", 
    "ticktext": ["Sep", "Oct", "Nov", "Dec"], 
    "tickvals": [37, 41, 46, 50]
  }, 
  "yaxis": {
    "title": "", 
    "mirror": True, 
    "showline": True, 
    "tickmode": "array", 
    "ticktext": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 
    "tickvals": [1, 2, 3, 4, 5, 6, 7]
  }, 
  "zaxis": {"title": "values"}
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)