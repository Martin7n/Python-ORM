# Generated by Django 5.0.4 on 2024-06-30 06:55

from django.db import migrations


def migrate_age_groups(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')
    people = person_model.objects.all()
    for person in people:
        if person.age <= 12:
            person.age_group = "Child"
        elif person.age <= 17:
            person.age_group = "Teen"
        else:
            person.age_group = "Adult"
    person_model.objects.bulk_update(people, ['age_group'])

def reset_age_group(apps, schema_editor):
    person_model = apps.get_model('main_app', "Person")

    for person in person_model.objects.all():
        person.age_group = "No age group"
        person.save()
        # person.age_group = person_model._meta.get_field('age_group').default


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [migrations.RunPython(migrate_age_groups, reset_age_group)
    ]
