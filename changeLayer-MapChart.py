

from Spotfire.Dxp.Application.Visuals import *
v = viz.As[VisualContent]()
for k in v.Layers:
    if k.Title == “mapchartLayerName”:
        if k.Enabled == True:
            k.Enabled = False
        else:
            k.Enabled = True

