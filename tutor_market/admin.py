from django.contrib import admin

from tutor_market.models import Rating, Subject, Tutor, Value


admin.site.site_header = 'Gipfel Tutor Administration'
admin.site.site_title = 'Gipfel Tutor Admin'
admin.site.index_title = 'Gipfel Tutor Administration'

admin.site.register(Tutor)
admin.site.register(Rating)
admin.site.register(Subject)
admin.site.register(Value)