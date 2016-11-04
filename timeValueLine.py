from bokeh.plotting import figure, output_file, show
import pandas

p=figure(plot_width=500,plot_height=250,x_axis_type="datetime",responsive=True)

p.title="Earthquake"
p.title_text_color="Orange"
p.title_text_font="times"
p.title_text_font_style="italic"

p.yaxis.minor_tick_line_color="Yellow"

p.xaxis.axis_label="Times"
p.yaxis.axis_label="Value"

#p.circle([1,2,3,4,5],[5,6,5,5,3],size=[8,12,14,15,20],color="red",alpha=0.5)
#p.triangle([1,2,3,4,5],[5,6,5,5,3],size=5,color="red",alpha=0.5)
#p.circle([1,2,3,4,5],[5,6,5,5,3],size=[i*2 for i in [8,12,14,15,20]],color="red",alpha=0.5)

df=pandas.read_csv("table.csv", parse_dates=["Date"])

p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)

#p.line([1,2,3,4,5],[5,6,5,5,3],line_width=2,color="red",alpha=0.5)

output_file("Scatter_plotting.html")

show(p)
