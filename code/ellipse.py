
from jinja2 import Template

from folium.element import JavascriptLink, Figure #,  MacroElement
from folium.map import Popup, Icon, Marker


class ellipse(Marker):
    def __init__(self, location):
        """Creates a Ellipse marker plugin to append into a map like CircleMarker
        Parameters
        ----------
        location: list of 3 lists, default None
            1) Latitude and Longitude of centre (in my case centre of cluster of data points)
            2) Radius 1, Radius 2 (in my case standard deviation of latitude and of longitude of data points)
            3) Angle of tilt (in my case correlation between longitude and latitude obserations)
            Example:
            [[51.5, -0.09], [500, 100], 90]
        
        """
        super(ellipse, self).__init__(location)
        self._name = 'ellipse'

        #var ellipse = L.ellipse([51.5, -0.09], [500, 100], 90).addTo(map);
        self._template = Template(u"""
            {% macro script(this, kwargs) %}
            
            var {{this.get_name()}} = L.ellipse(
                [{{this.location[0][0]}},{{this.location[0][01]}}],
                [{{this.location[1][0]}},{{this.location[1][1]}}],
                {{this.location[2]}}
                )
                .addTo({{this._parent.get_name()}});
            {% endmacro %}
            """)
                
    def render(self, **kwargs):
        super(ellipse, self).render(**kwargs)

        figure = self.get_root()
        assert isinstance(figure, Figure), ("You cannot render this Element "
                                            "if it's not in a Figure.")

        figure.header.add_children(
            #JavascriptLink("https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/0.4.0/leaflet.markercluster.js"),  # noqa
            #JavascriptLink("https://raw.githubusercontent.com/jdfergason/Leaflet.Ellipse/master/l.ellipse.min.js"),
            JavascriptLink("http://d8a.solutions/elenas_cdn/l.ellipse.js"),    
        name='ellipse')

#        , {
#        color: 'green', 
#        fillColor: 'green',
#        fillOpacity: 0.5
#        }