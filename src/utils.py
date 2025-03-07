import folium 
import geopandas as gpd 
from shapely.geometry import Point 
import random 

random.seed(100)


def monte_carlo_sampling(polygon, num_points=10):
    """
    Generates a specified number of random points within a given polygon.

    This function samples random points by generating coordinates within the 
    bounding box of the polygon and checking if they fall inside the polygon. 
    It continues generating points until the required number is reached.

    Parameters:
    - polygon (shapely.geometry.Polygon): The polygon within which points should be sampled.
    - num_points (int, optional): The number of random points to generate. Default is 100.

    Returns:
    - list of shapely.geometry.Point: A list of points inside the polygon.

    Note:
    - This method uses a rejection sampling approach, which may be inefficient 
      for complex or irregularly shaped polygons with large holes.
    """
    points = []
    minx, miny, maxx, maxy = polygon.bounds
    while len(points) < num_points:
        random_point = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(random_point):
            points.append(random_point)
    return points


def plot_sampled_points(sampled_points, base_map, map_object):
    """
    Plots sampled points on a Folium map as a separate layer.

    This function takes a list of sampled points, converts them into a GeoDataFrame, 
    ensures they have the correct CRS (EPSG:4326) for mapping, and adds them to 
    the provided Folium map as a `FeatureGroup`.

    Parameters:
    - sampled_points (list of shapely.geometry.Point): List of sampled points to be plotted.
    - base_map (geopandas.GeoDataFrame): The base map containing spatial reference (CRS).
    - map_object (folium.Map): The Folium map to which the points will be added.

    Returns:
    - folium.Map: The updated map with the sampled points layer.

    Note:
    - The function automatically reprojects the points and the base map to EPSG:4326 if needed.
    - The added layer can be toggled using the LayerControl feature.
    """
    points_gdf = gpd.GeoDataFrame(geometry=sampled_points, crs=base_map.crs)

    if points_gdf.crs.to_string() != "EPSG:4326":
        points_gdf = points_gdf.to_crs(epsg=4326)
    if base_map.crs.to_string() != "EPSG:4326":
        base_map = base_map.to_crs(epsg=4326)

    point_layer = folium.FeatureGroup(name="Sampled Points", overlay=True, control=True)

    for _, row in points_gdf.iterrows():
        point = row.geometry
        folium.CircleMarker(
            location=[point.y, point.x],  # (lat, lon)
            radius=3,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.7
        ).add_to(point_layer)

    point_layer.add_to(map_object)

    folium.LayerControl(collapsed=False).add_to(map_object)

    return map_object  

