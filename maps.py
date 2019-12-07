import logging
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

    def find_n_nearest(self, n):
        pass

