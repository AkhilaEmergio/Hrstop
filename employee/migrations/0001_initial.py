# Generated by Django 5.1.4 on 2024-12-23 08:47

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_logo', models.FileField(upload_to='logos/')),
                ('website_url', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('employee_code', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Integrity_control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan', models.BooleanField(default=False, null=True)),
                ('aadhar', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('employee_code', models.CharField(max_length=100)),
                ('profile', models.FileField(null=True, upload_to='profiles/')),
                ('reporting_manager', models.CharField(max_length=100, null=True)),
                ('business_unit', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('date_of_joining', models.CharField(max_length=100, null=True)),
                ('employment_type', models.CharField(max_length=100, null=True)),
                ('service_status', models.CharField(max_length=100, null=True)),
                ('workmode', models.CharField(max_length=100, null=True)),
                ('probation', models.CharField(max_length=100, null=True)),
                ('extension', models.CharField(max_length=100, null=True)),
                ('notice_period', models.CharField(max_length=100, null=True)),
                ('enrollment_no', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('trigger_onboarding', models.BooleanField(default=False, null=True)),
                ('send_mail', models.BooleanField(default=True, null=True)),
                ('weekly_offs', models.JSONField(null=True)),
                ('total_hr_spend', models.FloatField(default=0.0)),
                ('active_from', models.DateTimeField(blank=True, null=True)),
                ('inactive_from', models.DateTimeField(blank=True, null=True)),
                ('deactivate', models.BooleanField(default=False)),
                ('deactivated_on', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='userprofile_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='userprofile_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('year_of_passing', models.CharField(max_length=100)),
                ('gpa', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='education/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100, null=True)),
                ('occupation', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.JSONField()),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('bloodgroup', models.CharField(max_length=100)),
                ('domicile', models.CharField(max_length=100)),
                ('citizenship', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=100)),
                ('marriage_date', models.DateField(null=True)),
                ('mobile', models.CharField(max_length=20)),
                ('workphone', models.CharField(max_length=20, null=True)),
                ('personal_email', models.CharField(max_length=100, null=True)),
                ('linkedin', models.CharField(max_length=100, null=True)),
                ('slackuser', models.CharField(max_length=100, null=True)),
                ('permanent_address', models.TextField()),
                ('present_address', models.TextField()),
                ('drivinglicense', models.CharField(max_length=100, null=True)),
                ('passport', models.CharField(max_length=100, null=True)),
                ('Aadhar_number', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100, null=True)),
                ('UAN', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('previous_exp', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
