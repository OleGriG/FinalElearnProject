from django.contrib import admin
from . import models


class RelevanceElement(admin.StackedInline):
    model = models.Element

    fk_name = 'relevance_id'
    exclude = [f.name for f in models.Element._meta.get_fields() if '_id' in f.name and f.name != 'relevance_id']
    extra = 1


class GeoElement(admin.StackedInline):
    model = models.Element

    fk_name = 'geo_id'
    exclude = [f.name for f in models.Element._meta.get_fields() if '_id' in f.name and f.name != 'geo_id']
    extra = 1


class SkillElement(admin.StackedInline):
    model = models.Element

    fk_name = 'skill_id'
    exclude = [f.name for f in models.Element._meta.get_fields() if '_id' in f.name and f.name != 'skill_id']
    extra = 1


@admin.register(models.RelevancePage)
class RelevanceAdmin(admin.ModelAdmin):
    inlines = [RelevanceElement, ]


@admin.register(models.GeoPage)
class GeoAdmin(admin.ModelAdmin):
    inlines = [GeoElement, ]


@admin.register(models.SkillPage)
class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillElement, ]


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass
