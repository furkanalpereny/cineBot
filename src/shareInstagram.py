from InstagramAPI import InstagramAPI
from PIL import Image

InstagramAPI = InstagramAPI("unsharedthings", "herhangibirsifre.1234")
InstagramAPI.login()  # login

photo_path = 'src/img/2019-11-23/19-06-13-12-39-1343139.jpg'
print(photo_path)
img = Image.open(open(photo_path, 'rb'))
img.save(photo_path)

caption = "Sample photo"

share = InstagramAPI.uploadPhoto(photo=photo_path, caption=caption)
print(share)