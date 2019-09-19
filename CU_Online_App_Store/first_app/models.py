from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=264)
    email = models.CharField(max_length=264,unique=True)
    catagory = models.CharField(max_length=264)
    department = models.CharField(max_length=264)
    dept_id = models.CharField(max_length=264)
    password = models.CharField(max_length=264)
    confirm_password = models.CharField(max_length=264)
    phone_no = models.CharField(max_length=264)
    about = models.CharField(max_length=264)

    def __str__(self):
        return self.email
class MyWishList(models.Model):
    email = models.CharField(max_length=264)
    app_name = models.CharField(max_length=264)


class App_Profile(models.Model):
    app_name = models.CharField(max_length=100,unique=True)
    developer = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    apklocation = models.CharField(max_length=100)
    imagelocation = models.CharField(max_length=100)
    # apk = models.FileField(upload_to='upload/apk')

    def __str__(self):
        return self.app_name

# class AppProfile(models.Model):
#     Foreien_Key_From_SignUP = models.ForeignKey(Profile,on_delete=models.CASCADE)
#     appname = models.CharField(max_length=264,unique=True)
#     developername = models.CharField(max_length=264)
#     date = models.CharField(max_length=264)
#     version = models.CharField(max_length=264)
#     size = models.CharField(max_length=264)
#     description = models.CharField(max_length=264)
#     # photoLink = models.CharField(max_length=264)
#
#     def __str__(self):
#         return self.appname

# class WebPage(models.Model):
#     topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
#     name = models.CharField(max_length=264,unique=True)
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         return self.name



# class AccessRecord(models.Model):
#     name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
#     date = models.DateField()
#
#     def __str__(self):
#         return str(self.date)


# Create your models here.
# class Topic(models.Model):
#     top_name = models.CharField(max_length=264,unique=True)
#
#     def __str__(self):
#         return self.top_name
