from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start=datetime.datetime(2016,8,1)
end=datetime.datetime(2016,11,1)
df=data.DataReader(name="GOOG", data_source="google", start=start, end=end)

p=figure(x_axis_type='datetime',width=1000,height=300,responsive=True)
p.title="Candlestick Chart"
p.grid.grid_line_alpha=0.3

p.segment(df.index, df.High, df.index, df.Low, color="Black")

hour_12=12*60*60*1000
def inc_dec(c, o):
    if c > o:
        return "Increase"
    if c < o:
        return "Decrease"
    return "Equal"

df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"], hour_12,
    df.Height[df.Status=="Increase"], fill_color="#CCFFFF", line_color="black")

p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hour_12,
    df.Height[df.Status=="Decrease"], fill_color="#FF3333", line_color="black")

script1, div1 = components(p)    #this is a turple with JS code and HTML code
cdn_js=CDN.js_files
cdn_css=CDN.css_files

print(cdn_js)
#output_file("stock_analysis.html")
#show(p)
#print(tmp)
