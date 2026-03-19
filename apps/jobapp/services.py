from django.shortcuts import get_object_or_404
from jobapp.models import Job, Applicant, BookmarkJob
from account.models import User

def toggle_job_status(user_id: int, job_id: int) -> bool:
    """Marks a job as closed."""
    job = get_object_or_404(Job, id=job_id, user=user_id)
    job.is_closed = True
    job.save()
    return True

def delete_user_job(user_id: int, job_id: int) -> bool:
    """Deletes a job created by an employer."""
    job = get_object_or_404(Job, id=job_id, user=user_id)
    job.delete()
    return True

def remove_bookmark(user_id: int, bookmark_id: int) -> bool:
    """Deletes a saved bookmark."""
    bookmark = get_object_or_404(BookmarkJob, id=bookmark_id, user=user_id)
    bookmark.delete()
    return True
