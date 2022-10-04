from os import write
from tkinter import Y

from numpy import true_divide
from RsNGA import *

CH_ONE = 1
CH_TWO = 2
MODEL = 'USB0::0x0AAD::0x0197::5601.8002k05-101076::INSTR'
INSTR_DEBOUNCING = 0.5
DECIMAL_VAL = 3
DERIVATIVE_TOLERANCE = 0.00001
PLATEAU_DURATION = 3
LOG = False

POWER_DURATION = 10 # in seconds
MAX_VOLTAGE_CH_ONE = 100
MAX_CURRENT_CH_ONE = 0.001
MAX_VOLTAGE_CH_TWO = 5
MAX_CURRENT_CH_TWO = 0.005
INST_MODE = "OFF"
stop_when_plateau = False

powersupply = RsNGA(MODEL,logmode=LOG,mode=INST_MODE,debouncing=INSTR_DEBOUNCING)
powersupply.powerChannels(POWER_DURATION,MAX_VOLTAGE_CH_ONE, MAX_CURRENT_CH_ONE,log_data=True)
powersupply.closePowerSupply()

'''
#plot data
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows = 4, cols = 1, vertical_spacing=0.1,subplot_titles=("voltage","current","power","derivative to Power"))
fig.add_trace(go.Scatter(x = powersupply.data[f"ch{CH}"]["seconds"], y = powersupply.data[f"ch{CH}"]["voltage"]), row=1, col=1)
fig.add_trace(go.Scatter(x = powersupply.data[f"ch{CH}"]["seconds"], y = powersupply.data[f"ch{CH}"]["current"]), row=2, col=1)
fig.add_trace(go.Scatter(x = powersupply.data[f"ch{CH}"]["seconds"], y = powersupply.data[f"ch{CH}"]["power"]), row=3, col=1)
fig.add_trace(go.Scatter(x = powersupply.data[f"ch{CH}"]["seconds"], y = powersupply.derivative), row=4, col=1)
fig.add_trace(go.Scatter(x = powersupply.plateua_x, y = powersupply.plateua_y,marker = dict(color = "blue",size = 7),mode = "markers"),row = 4, col = 1)

fig.update_layout(height= 1200,width=1000,title_text = "width: 0.7, length: 3 scissors, conductive height: 5layers, SMP height: 2 layers")

fig['layout']['xaxis']['title']='seconds(t)'
fig['layout']['xaxis2']['title']='seconds(t)'
fig['layout']['xaxis3']['title']='seconds(t)'
fig['layout']['xaxis4']['title']='seconds(t)'
fig['layout']['yaxis']['title']='voltage(V)'
fig['layout']['yaxis2']['title']='current(A)'
fig['layout']['yaxis3']['title']='power(W)'
fig['layout']['yaxis4']['title']='dW/dt'

fig.write_html("data.html")
fig.show()
'''