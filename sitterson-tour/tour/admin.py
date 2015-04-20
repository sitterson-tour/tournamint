from django.contrib import admin
from tour.models import TourStop


class TourAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	fields = ('published', 'title', 'slug', 'content')
	list_display = ['published', 'title', 'updated']
	list_display_links = ['title']
	list_editable  = ['published']
	list_filter = ['published', 'updated']
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ['title', 'content']


admin.site.register(TourStop, TourAdmin)


