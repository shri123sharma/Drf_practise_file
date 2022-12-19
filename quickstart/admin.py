from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Snippet)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(User_1)

@admin.register(Collage)
class CollageaAdmin(admin.ModelAdmin):
    list_display=['name','type_collage','location','pin_code']
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['collage_department','floor','fields']
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display=['dep_section','classes']
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=('album_name','album_song','publish_date','update_date')
