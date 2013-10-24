from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from re import search
from members.models import *
from members.forms import *

class MemberAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'rin')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'rin', 'password1', 'password2')}
        ),
    )
    form = MemberChangeForm
    add_form = MemberCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_active',)
    list_filter = ()
    search_fields = ['first_name', 'last_name',]

class MeetingAttendanceAdmin(admin.ModelAdmin):

    def valid(self, obj):
        return obj.valid

    valid.boolean = True

    search_fields = ['member__first_name', 'member__last_name',]
    list_display = ('member', 'type', 'date', 'valid',)
    raw_id_fields = ('member',)

class WorkHourAdmin(admin.ModelAdmin):

    def valid(self, obj):
        return obj.valid

    search_fields = ['member__first_name', 'member__last_name',]
    list_display = ('member', 'hours', 'date', 'approved', 'valid',)
    raw_id_fields = ('member',)

class ClassAttendanceAdmin(admin.ModelAdmin):

    search_fields = ['member__first_name', 'member__last_name',]
    list_display = ('member', 'type', 'date',)
    raw_id_fields = ('member',)

class ExamAdmin(admin.ModelAdmin):

    def valid(self, obj):
        return obj.valid

    valid.boolean = True

    search_fields = ['member__first_name', 'member__last_name',]
    list_display = ('member', 'type', 'date', 'passed', 'valid',)
    raw_id_fields = ('member',)

class ShadowAdmin(admin.ModelAdmin):

    search_fields = ['member__first_name', 'member__last_name',]
    list_display = ('member', 'show', 'date', 'approved',)
    raw_id_fields = ('member', 'show',)

class ShowAdmin(admin.ModelAdmin):

    search_fields = ['member__first_name', 'member__last_name',]
    list_display = ('member', 'name', 'submitted', 'approved', 'scheduled', 'shadowable',)
    raw_id_fields = ('member',)

admin.site.register(Member, MemberAdmin)
admin.site.register(MeetingAttendance, MeetingAttendanceAdmin)
admin.site.register(WorkHour, WorkHourAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Shadow, ShadowAdmin)
admin.site.register(Show, ShowAdmin)
