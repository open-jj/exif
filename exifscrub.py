# MADE BY OSC
# delete bad exif data

from exif import Image
print("""
 $$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ /  \__|$$ /  \__|
$$ |  $$ |\$$$$$$\  $$ |      
$$ |  $$ | \____$$\ $$ |      
$$ |  $$ |$$\   $$ |$$ |  $$\ 
 $$$$$$  |\$$$$$$  |\$$$$$$  |
 \______/  \______/  \______/ 
                              
                              
                              
""")
print("Images contain metadata/exif that give data on the photo's place where it has been tooken, the time, and the settings used to make the photo look good. This application written in python is suppose to delete the metadata/exif that shows this.\n")
print("!! MAKE SURE IMAGE FILE FORMAT IS JPG !!\n")
loop = int(input("How many files are you going to scrub?: "))
for i in range(loop):
    imgs = input("List the file's directory: ")
    with open(imgs, "rb") as image_file:
        image = Image(image_file)
        images = [image]
        for index, image in enumerate(images):
            try:
                image.delete(image.gps_latitude, image.gps_latitude_ref, image.gps_longitude, image.gps_longitude_ref, image.gps_altitude, image.gps_altitude_ref, image.datetime, image.datetime_digitized, image.datetime_original)
            except:
                pass
            with open(f'./images/image{str(i)}_updated.jpg', 'wb') as updated_image:
                updated_image.write(image.get_file())
            print("Scrubbed File!")


