import pandas
from bokeh.plotting import figure, output_file, show

p=figure(plot_width=500,plot_height=400,title="Temperature and Air Pressure",tools='pan,resize',logo=None)
p.title_text_color="Gray"
p.title_text_font="times"
p.title_text_font_style="bold"

p.yaxis.minor_tick_line_color=None
p.xaxis.minor_tick_line_color=None

p.yaxis.axis_label="Pressure(hPa)"
p.xaxis.axis_label="Temperature(C)"

df=pandas.read_excel("verlegenhuken.xlsx",sheetname=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
p.circle(df["Temperature"],df["Pressure"],size=0.5,color="blue")

output_file("Solution9.html")
show(p)
