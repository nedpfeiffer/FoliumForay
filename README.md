Folium Foray - a simple geospatial data analysis project 

I preprocessed, analyzed, and visualized geolocation data from my cell carrier over the span of 3 months, using PyPDF2, Excel, and pandas to clean the messy data then folium to visualize geolocation over time.

While I wish I could share the original data from the PDF I was working with, it contains tons of PII and I don't want to go through and redact it.

Some interesting take aways:

* Cell carrier geolocation isn't terribly accurate! Knowing my actual residence at the time, the reported geolocation was consistently skewed to the southwest.
* There is a significant gap in the data between 2019-06-11 and 2019-06-22 because I was in Spain; I was no longer on AT&T's network.
* Analyzing the data on a daily basis, instead of hourly, proved more effective for understanding my activities that summer; focusing too closely on details can obscure the overall patterns.
