# E-Commerce-success
Analysis success of e-commerce websites by several KPI, with actionable insights results.
## Introduction
This project dives into the world of e-commerce, focusing specifically on the factors that contribute to the success of e-commerce websites. Success in the e-commerce industry is multi-dimensional and can be influenced by various factors. 

Each website ranked under those metrics to enable comprehensive view of performance, and allowing clear comparisons and identification of top performers.

## The data 
I got 2 seperate CSV files to work on in this project:

1. `Sites Data/`- All the fields about the sites information and their owners details including unique ID each site, the country it's based in, type, industry and the publish date.
2. `Sales Data/`- Table with all the transactions history of the websites including the unique ID for the site(foreign key), unique ID for the transaction, unique id for the customer, product name and price, date of transaction.

## Analysis Process
The analysis for the project was conducted in several stages:

1. **Data Cleaning and Preprocessing**: The raw data was cleaned and preprocessed using python and Excel. This included handling missing values, removing outliers, capitalize fixes, change variable type in order to improve efficiency.

2. **Exploratory Data Analysis (EDA)**: Conducted an exploratory analysis to understand the patterns and trends in the data. This included visualizing the distribution of different metrics, exploring correlations between variables, and identifying standout observations or trends.

<p align="center">
  <img src="images/total%20sales%20by%20country.jpg" alt="Total Sales by Country" width="450" height="250"/>
</p>
<p align="center">
  <img src="images/top%2010%20selling%20industries.jpg" alt="top sales industries" width="450" height="250"/>
</p>


3. **Metric-Based Analysis**: Based on the insights from the Exploratory Data Analysis (EDA), I performed a detailed analysis focusing on three key performance indicators (KPIs):
   - Growth rate in revenue
   - Growth rate in number of sales
   - Customer acquisition rate
These KPIs were evaluated and measured by their respective values from previous periods, both quarterly and annually.

4. **Rating System Implementation**: After examining the KPIs, I devised a rating system for each e-commerce website based on its performance across these four metrics. The system aimed to provide a balanced view of performance, taking into account all selected KPIs in order to quantify the success - Growth rate in revenue (40%), Growth rate in number of sales (20%), Customer acquistion rate (20%). 
Each website was rated 1-10 based on those metrics in order to identify the properties of a "Successful" site for improvement and success prediction.
<p align="center">
  <img src="images/average%sales%20per%20industry.jpg" alt="average" width="450" height="250"/>
</p>

<p align="center">
  <img src="images/industries%20average%20rank-top%2010.jpg" alt="average sales industry" width="450" height="250"/>
</p>

5. **Data Visualization**: Alongside the metric-based analysis, I created visual representations of the data and findings using Tableau and various Python libraries (like matplotlib, seaborn, and plotly). These visualizations designed to clearly communicate trends, patterns, and standout findings.

6. **Result Interpretation and Conclusion**: Based on the ratings, the visuallisation I drew conclusions about what factors most strongly influence the success of an e-commerce website. These findings have been translated into a set of actionable recommendations that could be used to enhance website performance and increase e-commerce success.


