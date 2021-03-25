from django.shortcuts import render


def index(req, *args, **kwargs):
    return render(req, 'index')


def robots(req, *args, **kwargs):
    return render(req, 'robots.txt', content_type='text/plain')


def manifestJSON(req, *args, **kwargs):
    return render(req, 'manifest.json', content_type='application/json')


def asset_manifest(req, *args, **kwargs):
    return render(req, 'asset-manifest.json', content_type='application/json')


def service_worker(req, *args, **kwargs):
    return render(req, 'service-worker.js', content_type="application/x-javascript")


def service_worker_map(req, *args, **kwargs):
    return render(req, 'service-worker.js.map', content_type="application/x-javascript")
