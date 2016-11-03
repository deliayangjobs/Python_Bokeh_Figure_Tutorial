from bokeh.plotting import figure, output_file, show

p=figure(plot_width=500,plot_height=400,title="Earthquakes")

#p.circle([1,2,3,4,5],[5,6,5,5,3],size=[8,12,14,15,20],color="red",alpha=0.5)
#p.triangle([1,2,3,4,5],[5,6,5,5,3],size=5,color="red",alpha=0.5)
p.circle([1,2,3,4,5],[5,6,5,5,3],size=[i*2 for i in [8,12,14,15,20]],color="red",alpha=0.5)


output_file("Scatter_plotting.html")

show(p)
