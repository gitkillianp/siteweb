from django.contrib import admin
from formulaire.models import FormulaireModel


class FormulaireModelAdmin(admin.ModelAdmin):
    list_display = ("Email", "Type", "Description")


admin.site.register(FormulaireModel, FormulaireModelAdmin)
