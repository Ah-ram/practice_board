# Generated by Django 5.0.7 on 2024-07-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("boardId", models.AutoField(primary_key=True, serialize=False)),
                ("boardName", models.CharField(max_length=32)),
                ("boardContext", models.TextField()),
                ("boardWriter", models.CharField(max_length=32)),
                ("regDate", models.DateTimeField(auto_now_add=True)),
                ("updDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "board",
            },
        ),
    ]
