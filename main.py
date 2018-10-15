import argparse
import os
import shapefile
import sys
from shapely import geometry

# Constants

SHPFILE_PATH = os.path.join(os.getcwd(), "CO_neighborhood_bounds", "ZillowNeighborhoods-CO.shp")
EXPECTED_FIELDS = ["DeletionFlag", "State", "County", "City", "Name", "RegionID"]
DEFAULT_COORDINATES = (40.018423, -105.279782)


# Classes

class Neighborhood:
    def __init__(self, feature):
        geo_interface = feature.shape.__geo_interface__
        self.shape = geometry.shape(geo_interface)

        # Metadata about the neighborhood: ID, name, city, county, state
        record = feature.record
        assert len(record) == 5, \
            "Expected exactly 5 record fields, but got " + len(record)
        [self.state, self.county, self.city, self.name, self.region_id] = record

    def contains(self, point):
        return self.shape.contains(point)
    
    def __str__(self):
        return "{}, City of {}, {} — {} County (Region ID {})".format(
            self.name,
            self.city,
            self.state,
            self.county,
            self.region_id
        )
    

# Functions

def main(coordinates):
    # Define our target location as a Point.
    # Note that our shapefiles are defined in Longitude, Latitude.
    target_location = geometry.Point(coordinates[1], coordinates[0])

    # Load the shapefile.
    shape = shapefile.Reader(SHPFILE_PATH)
    field_names = [field[0] for field in shape.fields]
    assert field_names == EXPECTED_FIELDS, \
        "shape.fields did not look as expected"

    # Iterate through the features of the shapefile.
    # Each feature represents a different neighborhood.
    for feature in shape.shapeRecords():
        neighborhood = Neighborhood(feature)
        if neighborhood.contains(target_location):
            print("Neighborhood found:", neighborhood)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Latitude", type=float)
    parser.add_argument("Longitude", type=float)
    try:
        args = parser.parse_args(sys.argv[1:])
        coordinates = (args.Latitude, args.Longitude)
    except:
        print("Using default coordinates:", DEFAULT_COORDINATES, "\n")
        coordinates = DEFAULT_COORDINATES
    main(coordinates)