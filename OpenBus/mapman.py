import folium
TLV_COORD = (32.0853, 34.7818)

class MapMan:    # map manual.
    def __init__(self, *args, **kwargs):
        
        KWARGS_DEFULST = {'location': TLV_COORD, 'zoom_start': 10, 'width': 640, 'height': 480}
        
        for key in kwargs_defults:
            if not key in kwargs:
                kwargs[key] = kwargs_defults[key]
        
        self.map = folium.Map(**kwargs)
        
        points = []
        routes = []
        
        for arg in args:
            if (type(arg[0]) == float) or (type(arg[0]) == int):
                point = folium.CircleMarker(arg, radius=1, color='#0080bb', 
                                            fill_color='#0080bb')
                points.append(point)
                
            else:
                route = folium.PolyLine(arg, color='#00b08b', weight=2, opacity=.5)
                route.append[route]
                
        [route.add_to(self.map) for route in routes]
        [point.add_to(self.map) for point in points]
            
                
            
    
    
    def _repr_html_(self):
        return self.map._repr_html_()
