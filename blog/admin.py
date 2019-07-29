from django.contrib import admin
from .models import Blog
# 같은 폴더에 있는 models에서 Blog라는 모델을 가져와라

admin.site.register(Blog)
