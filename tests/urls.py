# -*- coding: utf-8 -*-
from django.conf.urls import include, url


urlpatterns = [
    url(r'^cms/', include('cms.urls')),
]
