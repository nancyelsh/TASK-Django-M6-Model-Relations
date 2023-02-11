from django.contrib import admin

from classes import models

to_register = [
    models.Course,
    models.Lecture,
    models.Slide,
    models.Assignment,
    models.Tag,
]

admin.site.register(to_register)
