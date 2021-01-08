import ipywidgets as widgets
from datetime import date
from ipyleaflet import Map, Polygon, basemaps


def pick_date_range():
    from_day = widgets.DatePicker(
        description='From day',
        disabled=False,
        value=date(2020, 12, 1)
    )
    to_day = widgets.DatePicker(
        description='To day',
        disabled=False,
        value=date(2020, 12, 31)
    )

    display(from_day)
    display(to_day)

    return from_day, to_day


def pick_percentage_slider():
    percentage = widgets.IntSlider(
        value=15,
        min=0,
        max=100,
        step=1,
        description='Porcentaje de nubosidad',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d'
    )
    display(percentage)
    return percentage


class MapRegion():
    def __init__(self):
        self.map = Map(center=(37.9, -1.4), zoom=9, basemap=basemaps.OpenStreetMap.HOT)

        polygon = Polygon(
            locations=[[]],
            color="green",
            fill_color="green"
        )

        def handle_click(**kwargs):
            if kwargs.get('type') == 'click':
                pol = next(
                    layer for layer in self.map.layers if isinstance(layer, Polygon))
                coords = kwargs.get('coordinates')
                if (len(polygon.locations) == 0):
                    pol.locations[0].extend([coords, coords])
                else:
                    pol.locations[0].insert(1, coords)

                self.map.remove_layer(pol)
                other = Polygon(
                    locations=pol.locations,
                    color="green",
                    fill_color="green"
                )
                self.map.add_layer(other)

            if kwargs.get('type') == 'contextmenu':
                pol = next(layer for layer in self.map.layers if isinstance(layer, Polygon))
                self.map.remove_layer(pol)
                other = Polygon(
                    locations=[[]],
                    color="green",
                    fill_color="green"
                )
                self.map.add_layer(other)

        self.map.on_interaction(handle_click)
        self.map.add_layer(polygon)
        display(self.map)
    
    def get_region(self):
        locations = [[]]

        for layer in self.map.layers:
            if isinstance(layer, Polygon):
                locations[0] = [[loc[1], loc[0]] for loc in layer.locations[0]]
                
        if (len(locations[0]) > 0):
            locations[0].append(locations[0][0])
        
        return locations[0]


def pick_tile(tiles):
    tile_selector = widgets.Dropdown(
        options=tiles,
        value=None,
        description='Tile:',
        disabled=False,
    )
    display(tile_selector)
    return tile_selector
 
