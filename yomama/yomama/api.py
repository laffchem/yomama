from ninja import NinjaAPI
from v1.api import router as jokes_router
from v1.private_api import private_router as internal_router
from django.contrib.admin.views.decorators import staff_member_required

api = NinjaAPI(urls_namespace='public_api')
api.add_router("/v1/", jokes_router)

api_private = NinjaAPI(csrf=True, urls_namespace='private_api.py')
api_private.add_router("/internal/", internal_router)
