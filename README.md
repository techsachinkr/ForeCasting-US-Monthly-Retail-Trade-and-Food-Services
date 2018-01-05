# ForeCasting-US-Monthly-Retail-Trade-and-Food-Services
Time Series forecasting for United States Monthly Retail Trade and Food Services

Dataset

Used publicly available Time-series dataset of US Monthly Retail Trade and Food Services provided by United States Census Bureau.
It consists time series data for timerange Jan 1992 till Oct 2017 and the more details are as follows:
i) Datavalues : - Main file containing sales figures in million dollars scale for the respective time,trading segment and categories as mentioned.
ii) Datatypes :- File containing datatypes codes and mapping
iii) Categories :- Exact Retail segments codesmapping to their description.
iv) Timeperiods :-  Contains mapping of timeperiod codes used in datavalues to the respective time period.

## Steps followed

### i) Cleaning Data

a) Filtering out datatype value 1 rows i.e. retail sales data from orginal dataset.
b) Now, filtering out values with no seasonality adjusted to ensure we are starting our analysis on untouched or raw data.
c) Removing the rows with no sales values given
d) Grouping and summing up sales data of different retail categories for the respective months.

### ii) Data Exploration and Analysis

a) Plotting the data to check stationarity

![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/salesdata%20plot.png)

Now since in the above plot we can see that there is overall increasing trend so now we can check stationarity by following methods:
 i) Plotting Rolling Statistics: 
 
 
![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/rolling%20mean%20and%20std%20plot.png)

ii) Dickey-Fuller Test: 
```
Results of Dickey-Fuller Test:
Test Statistic                  -4.062481
p-value                          0.001116
#Lags Used                      15.000000
Number of Observations Used    283.000000
Critical Value (1%)             -3.453670
Critical Value (5%)             -2.871808
Critical Value (10%)            -2.572241
dtype: float64
```
![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/dickey-fuller%20test%20plot.png)


(b) Removing Trend and Seasonality

Two techniques applied which are:-

i) Differencing

![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/differencing_output_plot.png)

ii) Decomposition

![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/decomposition_output_plot.png)

### Modelling Data

(a) Finding optimal ARIMA model order parameters

i) Plotting ACF (Autocorrelation Function) to find optimal value of p

![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/acf-plot.png)

After looking into plot,most optimal value with postive correlation appears to be 10 so i'llbe using 10 as value of p.

ii) Plotting PACF (Partial Autocorrelation Function) to find optimal value of q

![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/pacf-plot.png)

After looking into plot,most optimal value with postive correlation appears to be 10 so i'llbe using 10 as value of p.

iii) Creating ARIMA model with p as 10 ,difference parameter d as 1, and q parameter as 0

![alt text](https://github.com/techsachinkr/ForeCasting-US-Monthly-Retail-Trade-and-Food-Services/blob/master/output%20plots/ARIMA-Plot.png)

So we got our final predictions with Test MSE: 26111455464.179
