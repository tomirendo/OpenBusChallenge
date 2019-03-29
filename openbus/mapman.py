import folium
from collections import Iterable
TLV_COORD = (32.0853, 34.7818)

class MapMan:    # map manual.
    def __init__(self, *args, point_size=6, line_width=6, **kwargs):
        
        KWARGS_DEFULST = {'location': TLV_COORD, 'zoom_start': 10, 'width': 640, 'height': 480}
        
        for key in KWARGS_DEFULST:
            if not key in kwargs:
                kwargs[key] = KWARGS_DEFULST[key]
        
        self.map = folium.Map(**kwargs)
        
        points = []
        routes = []
        
        for arg in args:
                
            if isinstance(arg[0], Iterable):
                route = folium.PolyLine(arg, color='#ff00ff', weight=line_width, opacity=.7)
                routes.append(route)
                
            else:
                point = folium.CircleMarker(arg, radius=point_size, color='#0080bb', 
                                            fill_color='#0080bb')
                points.append(point)
                
        [route.add_to(self.map) for route in routes]
        [point.add_to(self.map) for point in points]
            
                
            
    
    
    def _repr_html_(self):
        return self.map._repr_html_()

