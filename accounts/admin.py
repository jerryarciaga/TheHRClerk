from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    vebose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = (
        'email',
        'get_rank',
        'first_name',
        'last_name',
        'is_staff',
        'get_unit',
    )
    list_select_related = ('profile', )

    def get_rank(self, instance):
        return instance.profile.rank
    get_rank.short_description = 'Rank'

    def get_unit(self, instance):
        return instance.profile.unit
    get_unit.short_description = 'Unit'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
