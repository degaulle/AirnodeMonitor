# AirnodeMonitor

An air pollution monitor and visualizer using Airnode data and Google Map API

# User Guide
Welcome to Airnode Monitor, a multi-function visualization tool to give a visual representation of air pollution. It is designed both for scientists to analyze their data and further conduct their research and for citizens to have a clear visual comparison of the air pollution in major countries and major cities. 

Navigation(for both scientists and citizens):
The first layer of the website is a general overview of the comparison of air pollution level on a national level. The "pollution ranked by country" button links to the world health organization's ranking of countries' air pollution levels released in 2015, and the "explore country" button links to a treemap visualization of the currently most polluted countries in the world, with a larger area representing a higher pollution level.
The second layer of the website is the zoomable world map that allows comparison of air pollution on a more detailed city level. The pollution data collected from monitors are shown in the form of a heatmap, with green color representing the lowest level of air pollution and the red color representing the highest level of air pollution. There are three toolbars at the top of the map, "Toggle Heatmap" allows you to enable or disable the heatmap; "Change gradient" allows you to change the color of the visual representation and "Change opacity" allows you to modify the opacity of the heatmap. With these functions, you can navigate the map and view the pollution level around each major cities and compare them.

Loading data(for scientists):
For scientists to load their air pollution data on to the world map, they can export the GPS and pollution level data from their air pollution sensor (like air visual node) as a csv file into the leaflet.html page.

# About Us
We are a team of undergraduates at Yale aiming to design a web-based application for both scientists and citizens to have a visualization of the air pollution data. We think that people nowadays are becoming numb to numbers and we need visual representation of air pollution.
We want to give a comparison of air pollution level in different countries and in different cities. However, due to limited access to data, we can only get data from all countries on a general level and data from most big cities in U.S. However, our application can accomodate all kinds of data so if in the future more detailed data is available, a more detailed map can be shown.
We are running on flask on a local host.
For the visualized map we are using Google's developer's tool for heatmap. We use the weight function to allow different gradient of color to show on the heatmap which represents the air pollution level. So the latitude longtitude and weight are all inputted from the air pollution data with the weight being the level of pollution.
We have many failed attempts like trying to use the leaflet map and color all the counties base on the air pollution level (but we failed to load the color patches) or to use an API key to import database into the google heatmap but the data base won't load. So we eventually decided to have the scientist user to export their data as a csv file and copy and paste the data into the html page.
For the images at the bottom of the webpage we made the CSS automatically resize the images and enabled a flexible grid using flexbox.

Reference:
http://airvisual.com/user/api
https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap
