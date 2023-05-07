from django.contrib import admin

from authors.models import Painter, Tag, Exhibition

@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    pass
