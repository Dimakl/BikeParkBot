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
        pts = [ geopy.Point(p[0],p[1]) for p in parkings]
        onept = geopy.Point(self.coords[0],self.coords[1])
        alldist = [ (p,geopy.distance.distance(p, onept).km) for p in pts ]
        nearest_point = sorted(alldist, key=lambda x: (x[1]))[0]
        return [[k[0][0], k[0][1]] for k in nearest_point]
