from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("saltstickerco", "herhangibirsifre.1234")
InstagramAPI.login()  # login

photo_path = 'src/img/2019-11-23/19-06-13-12-39-1343139.jpg'
print(photo_path)
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
