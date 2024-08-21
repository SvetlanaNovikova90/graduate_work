from users.models import Recording


def get_cached_subjects_for_recording(user_pk):
    recording_list = Recording.objects.filter(user_id=user_pk)
    return recording_list
