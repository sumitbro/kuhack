# Generated by Django 3.0.5 on 2021-02-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('website', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=1, null=True)),
                ('contact', models.CharField(max_length=15)),
                ('dob', models.DateField(null=True)),
                ('blood', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=200, null=True)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('ward', models.IntegerField(null=True)),
            ],
        ),
    ]
