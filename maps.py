import logging
import geopy
import geopy.distance
logger = logging.getLogger(__name__)
from config import APP_CODE, APP_ID, WIDTH, HEIGHT, PPI, LINE_WIDTH, STREET_VIEW_TYPE, LINE_COLOR, DEST_COLOR
from requests import get
from io import BytesIO
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
        target_url = "https://image.maps.api.here.com/mia/1.6/routing"
        start="{0},{1}".format(*self.coords)
        dest = "{0},{1}".format(*parking_coords)

        params = {
            "app_id": APP_ID,
            "app_code": APP_CODE,
            "waypoint0": start,
            "waypoint1": dest,
            "w": WIDTH,
            "h": HEIGHT,
            #"ppi": PPI,
            "lw": LINE_WIDTH,
            "t": STREET_VIEW_TYPE,
            "lc": LINE_COLOR,
            "poix0": "{0};{1};{1};11;.".format(dest, DEST_COLOR),

        }
        resp = get(target_url, params=params)
        return BytesIO(resp.content)


    def find_n_nearest(self, n, parkings):
        pts = [geopy.Point(p[0], p[1]) for p in parkings]
        onept = geopy.Point(self.coords[0], self.coords[1])
        alldist = [(p, geopy.distance.distance(p, onept).km) for p in pts]
        nearest_point = sorted(alldist, key=lambda x: (x[1]))[:n]
        return [[k[0][0], k[0][1]] for k in nearest_point]
