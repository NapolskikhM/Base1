from django.contrib import admin
from .models import Table1, Table2, Table3, Table4


@admin.register(Table1)
class Table1Admin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description',)
    search_fields = ('name',)


@admin.register(Table2)
class Table2Admin(admin.ModelAdmin):
    list_display = ('range', 'age', 'qualification',)
    search_fields = ('range',)

@admin.register(Table3)
class Table3Admin(admin.ModelAdmin):
    list_display = ('name', 'exp',)
    search_fields = ('name',)

@admin.register(Table4)
class Table4Admin(admin.ModelAdmin):
    list_display = ('name', 'salary',)
    search_fields = ('name',)