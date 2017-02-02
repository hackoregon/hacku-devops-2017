# you'll need to add the include import
from django.conf.urls import url, include
from django.contrib import admin

# here we import the router from our views.py
# the router handles all url mapping for our app
from user.views import router

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # This includes all our registered ViewSets
    url(r'^', include(router.urls)),

    # This provides the ability to login to the app
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

## Setting up static files for development:
if settings.DEBUG == True:
  urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
