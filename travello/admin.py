from django.contrib import admin
from .models import Destination
from .models import Movies
from .models import Trending
from .models import Top
# Register your models here.

admin.site.register(Destination)
admin.site.register(Movies)
admin.site.register(Trending)
admin.site.register(Top)