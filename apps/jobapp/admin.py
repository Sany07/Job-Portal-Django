from django.contrib import admin
from .models import *


admin.site.register(Category)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'status', 'created_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')

admin.site.register(Applicant, ApplicantAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_closed','created_at','updated_at')
    # Put soft-delete flags at the bottom in the admin form UI.
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'title',
                'description',
                'tags',
                'location',
                'job_type',
                'work_mode',
                'experience_level',
                'category',
                'salary',
                'views_count',
                'company_name',
                'company_description',
                'url',
                'last_date',
                'is_published',
                'is_closed',
            )
        }),
        ('Soft delete', {
            'fields': (
                'is_deleted',
                'deleted_at'
            )
        }),
    )

admin.site.register(Job,JobAdmin)

class BookmarkJobAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'created_at')

admin.site.register(BookmarkJob, BookmarkJobAdmin)


