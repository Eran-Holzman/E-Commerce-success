# E-Commerce-success
Analysis success of e-commerce websites by several KPI, with actionable insights results.
## Introduction
This project dives into the world of e-commerce, focusing specifically on the factors that contribute to the success of e-commerce websites. Success in the e-commerce industry is multi-dimensional and can be influenced by various factors. 

Each website ranked under those metrics to enable comprehensive view of performance, and allowing clear comparisons and identification of top performers.

## The data 
I got 2 seperate CSV files to work on in this project:

1. `Sites Data/`- All the fields about the sites information and their owners details including unique ID each site, the country it's based in, type, industry and the publish date.
1. `Sales Data/`- Table with all the transactions history of the websites including the unique ID for the site(foreign key), unique ID for the transaction, unique id for the customer, product name and price, date of transaction.

## Analysis Process
The analysis for the project was conducted in several stages:

1. **Data Cleaning and Preprocessing**: The raw data was cleaned and preprocessed using python and Excel. This included handling missing values, removing outliers, capitalize fixes, change variable type in order to improve efficiency.

2. **Exploratory Data Analysis (EDA)**: Conducted an exploratory analysis to understand the patterns and trends in the data. This included visualizing the distribution of different metrics, exploring correlations between variables, and identifying standout observations or trends that could inform further analysis.

3. **Metric-Based Analysis**: Based on the insights from the EDA, I performed a detailed analysis focusing on three key performance indicators (KPIs): 
1. Growth rate in revenue
2. Growth rate in number of sales
3. Customer acquistion rate

4. **Rating System Implementation**: After examining the KPIs, I devised a rating system for each e-commerce website based on its performance across these four metrics. The system aimed to provide a balanced view of performance, taking into account all selected KPIs in order to quantify the success - Growth rate in revenue (40%), Growth rate in number of sales (20%), Customer acquistion rate (20%). 
Each website was rated 1-10 based on those metrics in order to identify the properties of a "Successful" site for future prediction and improvement.

5. **Result Interpretation and Conclusion**: Based on the ratings and the analysis, I drew conclusions about what factors most strongly influence the success of an e-commerce website. I have translated these findings into a set of company actionable recommendations that could be used to enhance website performance and increase e-commerce success.


