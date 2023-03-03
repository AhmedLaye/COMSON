
from django.contrib import admin
from.models import Demandeur
# Register your models here.
class Adminhome(admin.ModelAdmin):
    list_display=('nom','prenom', 'age')
    search_fields = ('nom',) 
    # list_editable = ('price',)
admin.site.register(Demandeur, Adminhome)