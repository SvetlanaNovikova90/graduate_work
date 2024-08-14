from django.core.cache import cache


from clinic.models import Service
from config import settings


def get_cached_subjects_for_service(department_pk):
    # if settings.CACHE_ENABLED:
    #     key = f'service_list_{department_pk}'
    #     service_list = cache.get(key)
    #     if service_list is None:
    #         service_list = Service.objects.filter(department_id=department_pk)
    #         cache.set(key, service_list)
    # else:
    service_list = Service.objects.filter(department_id=department_pk)
    return service_list
