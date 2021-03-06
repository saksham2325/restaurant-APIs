from django.db import migrations

def split_names(apps,schema_editor):
    User = apps.get_model('accounts','User')
    for person in User.objects.all():
        splitted_name = person.name.split(" ",1)
        person.first_name=splitted_name[0]
        if len(splitted_name)>1:
            person.last_name = splitted_name[1]
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211016_0659'),
    ]

    operations = [
        migrations.RunPython(split_names,migrations.RunPython.noop),
    ]
