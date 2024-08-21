from clinic.models import Service


def get_cached_subjects_for_service(department_pk):

    service_list = Service.objects.filter(department_id=department_pk)
    return service_list


