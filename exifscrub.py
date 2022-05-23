# Written by open-jj | https://github.com/open-jj

from exif import Image
noExifData = False
files_passed = 0
finished_files = 0

loop = int(input("How many files are you going to scrub?: "))
for i in range(loop):
    imgs = input("List the file's location: ")
    with open(imgs, "rb") as image_file:
        image = Image(image_file)
        images = [image]
        for index, image in enumerate(images):
            try:
                image.delete(image.gps_latitude, image.gps_latitude_ref, image.gps_longitude, image.gps_longitude_ref, image.gps_altitude, image.gps_altitude_ref, image.datetime, image.datetime_digitized, image.datetime_original)
            except:
                print(f"Could not delete EXIF data for image {i}")
                noExifData = True
                files_passed += 1
            if noExifData == False:
                with open(f'image_{i}_scrubbed.jpg', 'wb') as updated_image:
                    updated_image.write(image.get_file())
                    print("Scrubbed File!")
                    print(f"Output File: image_{i}_scrubbed.jpg")
                    finished_files += 1
            else:
                pass
print(f"Scrubbed: {finished_files}\nFiles Skipped: {files_passed}")
input("Press Enter to Exit...")
            
