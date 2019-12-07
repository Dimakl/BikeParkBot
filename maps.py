import logging
import geopy
import geopy.distance
logger = logging.getLogger(__name__)


class Path:
    def __init__(self, coords):
        self.coords = coords

    """
    view 500-1000m of bike parkings
    """
    def gen_overview_map(self):
        pass

    """
    generate map image with route
    """
    def gen_route_to(self, parking_coords):
        pass

    def find_n_nearest(self, n, parkings):
        # your data
        ccoordinate_list = [(37.7718513, 55.639926), (37.655829000192, 55.71449030019)]
        coordinate = (37.52508949, 55.75611045)
        # the solution
        pts = [ geopy.Point(p[0],p[1]) for p in ccoordinate_list ]
        onept = geopy.Point(coordinate[0],coordinate[1])
        alldist = [ (p,geopy.distance.distance(p, onept).km) for p in pts ]
        nearest_point = sorted(alldist, key=lambda x: (x[1]))[0] #
        pass
