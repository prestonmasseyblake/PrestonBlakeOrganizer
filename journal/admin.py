from django.contrib import admin
from journal.models import JournalCategory, JournalEntry

# Register your models here.
admin.site.register(JournalCategory)
admin.site.register(JournalEntry)
