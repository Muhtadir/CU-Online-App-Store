from django.urls import path
from first_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index,name="index"),
    path('create/',views.create,name='create'),
    path('dashboard/<email>',views.dashboard,name="dashboard"),
    # path('myprofile/',views.myprofile,name="myprofile"),
    path('myprofile/<email>',views.myprofile,name="myprofile"),
    path('upload/<email>',views.upload,name="upload"),
    path('delete/<email>/<app_name>',views.delete,name="delete"),
    path('wishlist/<email>',views.wishlist,name="wishlist"),
    path('addtowishlist/<email>/<app_name>',views.addtowishlist,name="addtowishlist"),
    path('auth/',views.auth,name='auth'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name="signup"),
    path('viewapp/<email>/<app_name>',views.viewapp,name="viewapp"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
