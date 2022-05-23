# This might not work because the photo isn't JPEG or JPG and have EXIF data or the location services are disabled when said image was tooken
# Written by open-jj | https://github.com/open-jj

from exif import Image

with open(input("Input File Directory:\n"), "rb") as image_file:
    image = Image(image_file)
    
images = [image] #image2

if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
else:
    status = "does not contain any EXIF information."

image_members = []

for image in images:
    image_members.append(dir(image))

for index, image_member_list in enumerate(image_members):
    print(f"Image {index} contains {len(image_member_list)} members:")
    print(f"{image_member_list}\n")

def format_dms_coordinates(coordinates):
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""

def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees

def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
    
    decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
    url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
    return url

def degrees_to_direction(degrees):
    COMPASS_DIRECTIONS = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E", 
        "ESE", 
        "SE", 
        "SSE",
        "S", 
        "SSW", 
        "SW", 
        "WSW", 
        "W", 
        "WNW", 
        "NW", 
        "NNW"
    ]
    
    compass_directions_count = len(COMPASS_DIRECTIONS)
    compass_direction_arc = 360 / compass_directions_count
    return COMPASS_DIRECTIONS[int(degrees / compass_direction_arc) % compass_directions_count]

def format_direction_ref(direction_ref):
    direction_ref_text = "(true or magnetic north not specified)"
    if direction_ref == "T":
        direction_ref_text = "True north"
    elif direction_ref == "M":
        direction_ref_text = "Magnetic north"
    return direction_ref_text

def format_altitude(altitude, altitude_ref):
    altitude_ref_text = "(above or below sea level not specified)"
    if altitude_ref == 0:
        altitude_ref_text = "above sea level"
    elif altitude_ref == 1:
        altitude_ref_text = "below sea level"
    return f"{altitude} meters {altitude_ref_text}"

def format_speed_ref(speed_ref):
    speed_ref_text = "(speed units not specified)"
    if speed_ref == "K":
        speed_ref_text = "km/h"
    elif speed_ref == "M":
        speed_ref_text = "mph"
    elif speed_ref == "N":
        speed_ref_text = "knots"
    return speed_ref_text

for index, image in enumerate(images):
    print("----------------------------")
    print(f"DEVICE INFORMATION - IMAGE {index}")
    print("----------------------------")
    print(f"MAKE: {image.get('make', 'UNKNOWN')}")
    print(f"MODEL: {image.get('model', 'UNKNOWN')}")
    print(f"MAKER_NOTE: {image.get('maker_note', 'UNKNOWN')}")
    print(f"SOFTWARE: {image.get('software', 'UNKNOWN')}")
    print(f"APERTURE_VALUE: {image.get('aperture_value', 'UNKNOWN')}")
    print(f"BRIGHTNESS_VALUE: {image.get('brightness_value', 'UNKNOWN')}")
    print(f"COLOR_SPACE: {image.get('color_space', 'UNKNOWN')}")
    print(f"DATE_TIME: {image.get('date_time', 'UNKNOWN')}")
    print(f"DATETIME_DIGITIZED: {image.get('datetime_digitized', 'UNKNOWN')}")
    print(f"DATETIME_ORIGINAL: {image.get('datetime_original', 'UNKNOWN')}")
    print(f"EXPOSURE_BIAS_VALUE: {image.get('exposure_bias_value', 'UNKNOWN')}")
    print(f"EXPOSURE_MODE: {image.get('exposure_mode', 'UNKNOWN')}")
    print(f"FLASH: {image.get('flash', 'UNKNOWN')}")
    print(f"SHUTTER_SPEED_VALUE {image.get('shutter_speed_value', 'UNKNOWN')}")
    print(f"WHITE_BALANCE: {image.get('white_balance', 'UNKNOWN')}")
    print(f"GPS_DATESTAMP: {image.get('gps_datestamp', 'UNKNOWN')}")
    print(f"EXIF_VERSION: {image.get('exif_version', 'UNKNOWN')}")
    print(f"X_RESOLUTION: {image.get('x_resolution', 'UNKNOWN')}")
    print(f"Y_RESOLUTION: {image.get('y_resolution', 'UNKNOWN')}")
    print(f"ORIENTATION: {image.get('orientation', 'UNKNOWN')}")
    print(f"PIXEL_X_DIMENSION: {image.get('pixel_x_dimension', 'UNKNOWN')} pixels")
    print(f"PIXEL_Y_DIMENSION: {image.get('pixel_y_dimension', 'UNKNOWN')} pixels")
    print(f"PIXEL_DIMENSIONS: " + str(image.get('pixel_x_dimension', 'UNKNOWN')) + " x " + str(image.get('pixel_y_dimension', 'UNKNOWN')))
    print(f"SCENE_CAPTURE_TYPE: {image.get('scene_capture_type', 'UNKNOWN')}")
    print(f"LENS MAKE: {image.get('lens_make', 'UNKNOWN')}")
    print(f"LENS MODEL: {image.get('lens_model', 'UNKNOWN')}")
    print(f"LENS SPECIFICATION: {image.get('lens_specification', 'UNKNOWN')}")
    print(f"DATE/TIME TAKEN {image.get('datetime.original', 'UNKNOWN')}.{image.get('subsec_time_original', 'UNKNOWN')} {image.get('offset_time', 'UNKNOWN')}")
    print(f"LATITUDE: {image.get('gps_latitude', 'UNKNOWN')} {image.get('gps_latitude_ref', 'UNKNOWN')}")
    print(f"LONGITUDE: {image.get('gps_longitude', 'UNKNOWN')} {image.get('gps_longitude_ref', 'UNKNOWN')}")
    print(f"LATITUDE (DMS): {format_dms_coordinates(image.get('gps_latitude', 'UNKNOWN'))} {image.get('gps_latitude_ref', 'UNKNOWN')}")
    print(f"LONGITUDE (DMS): {format_dms_coordinates(image.get('gps_longitude', 'UNKNOWN'))} {image.get('gps_longitude_ref', 'UNKNOWN')}")
    print(f"LATITUDE (DD): {dms_coordinates_to_dd_coordinates(image.get('gps_latitude', 'UNKNOWN'), image.get('gps_latitude_ref', 'UNKNOWN'))}")
    print(f"LONGITUDE (DD): {dms_coordinates_to_dd_coordinates(image.get('gps_longitude', 'UNKNOWN'), image.get('gps_longitude_ref', 'UNKNOWN'))}")
    print(draw_map_for_location(image.gps_latitude, image.gps_latitude_ref, image.gps_longitude,image.gps_longitude_ref))
    decimal_latitude = dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)
    coordinates = (decimal_latitude, decimal_longitude)
    print(f"IMAGE DIRECTION: {degrees_to_direction(image.gps_img_direction)} ({image.gps_img_direction}°)")
    print(f"IMAGE DIRECTION REF: {format_direction_ref(image.gps_img_direction_ref)}")
    print(f"ALTITUDE: {format_altitude(image.gps_altitude, image.gps_altitude_ref)}")
    print(f"SPEED: {image.gps_speed} {format_speed_ref(image.gps_speed_ref)}\n")
