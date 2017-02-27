"""django_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django_quiz import settings
from login.views import LoginView,RegisterView,LogoutView,Authenticate,UserInfo,ProfileDetails,UpdateProfileDetails
from views import IndexView
from rest_framework.authtoken import views
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/qna/', include('qna.urls')),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/user/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/auth/register/$', RegisterView.as_view(), name='register'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/v1/auth/authenticate/$', Authenticate.as_view(),name='authenticate'),
    url(r'^api/v1/user/info/$', UserInfo.as_view(),name='info'),
    url(r'^api/v1/user/(?P<profile_id>[0-9]+)/profile_details/$', ProfileDetails.as_view(),name='profile'),
    url(r'^api/v1/user/update_profile/$', UpdateProfileDetails.as_view(),name='update_profile'),


    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT,
    # }),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
