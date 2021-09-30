# Generated by Django 3.2.7 on 2021-09-30 06:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('seats', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.DecimalField(decimal_places=2, editable=False, max_digits=100)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.show')),
            ],
        ),
    ]
