from django.contrib import admin
from management.models import *

class FacultyAdmin(admin.ModelAdmin):
    pass
class SubjectsAdmin(admin.ModelAdmin):
    pass
class TimingAdmin(admin.ModelAdmin):
    pass
class FacultyAllocationsAdmin(admin.ModelAdmin):
    pass




admin.site.register(FacultyOtherInfo, FacultyAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Timeing, TimingAdmin)
admin.site.register(FacultyAlocations, FacultyAllocationsAdmin)