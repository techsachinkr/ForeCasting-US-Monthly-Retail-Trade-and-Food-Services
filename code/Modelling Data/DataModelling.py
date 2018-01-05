"""
@author: SACHIN
"""
#ACF and PACF plots:
from statsmodels.tsa.stattools import acf, pacf
lag_acf = acf(ts_log_diff, nlags=80)
lag_pacf = pacf(ts_log_diff, nlags=80, method='ols')
#from pandas.tools.plotting import autocorrelation_plot
#autocorrelation_plot(ts)
#Plot ACF: 
plt.subplot(121) 
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/npy.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/npy.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/npy.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/npy.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()

from statsmodels.tsa.arima_model import ARIMA

from sklearn.metrics import mean_squared_error
X = ts.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(10,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
plt.plot(test,label='Actual Value')
plt.plot(predictions, color='red', label='Predictions')
plt.legend(loc='best')
plt.title('AR Model')
plt.show()
