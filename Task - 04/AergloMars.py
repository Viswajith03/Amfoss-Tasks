import requests
import os
from PIL import Image
import urllib.request

Api_Key = "Ns3b2MuqXDvoXOpVPsY9I08I4I1xnhzhOjYB3HlS"

name = input("Enter the name of the rover (in lower case):")

date = input("Enter the data in YYYY-MM-DD format : ")

Api_ = str(Api_Key)

url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_Key}"

r = requests.get(url)

Data = r.json()

no_photos = int(input("Enter the number of photos : "))

Photos = Data['photos'][:no_photos]

for index , photo in enumerate(Photos):
    img_url = photo['img_src']

    image_dir = f"./Rover_Images/{date} {name}"
    dir_res = os.path.exists(image_dir)
    title = f'{index}.jpg'

    if (dir_res ==  False):
        os.makedirs(image_dir)
    else:
        print(f"Saving {title} to {image_dir}")

    urllib.request.urlretrieve(url = img_url , filename = os.path.join(image_dir,title))
print("DONE")

