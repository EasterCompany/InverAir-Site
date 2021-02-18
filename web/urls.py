# Essential
from django.urls import path

# Application Views
from core.views import *

# URL Endpoints
urlpatterns = [

    # Core App
    path('', index),
    path('index.html', index),
    path('robots.txt', robots),
    path('manifest.json', manifestJSON),
    path('asset-manifest.json', asset_manifest),

    # Service Worker
    path('service-worker.js', service_worker),
    path('service-worker.js.map', service_worker_map),

]
