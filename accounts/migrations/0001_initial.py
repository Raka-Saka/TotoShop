# Generated by Django 4.0.1 on 2022-01-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('kanji_1name', models.CharField(max_length=24)),
                ('kanji_2name', models.CharField(max_length=24)),
                ('company_name', models.CharField(max_length=50)),
                ('company_phone_number', models.CharField(max_length=24)),
                ('company_general_email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('personal_phone_number', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_customer_enduser', models.BooleanField(default=False)),
                ('is_supplier', models.BooleanField(default=False)),
                ('is_vip', models.BooleanField(default=False)),
                ('is_customer_wineshop', models.BooleanField(default=False)),
                ('is_customer_restaurant', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
