# Generated by Django 4.1.4 on 2022-12-20 14:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart_1', '0004_user_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_1',
            fields=[
                ('hos_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hos_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hos_address', models.CharField(max_length=100)),
                ('hos_city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_diagnosis', models.CharField(blank=True, max_length=100, null=True)),
                ('p_address', models.CharField(blank=True, max_length=100, null=True)),
                ('hos_p', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quickstart_1.hospital_1')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_examination', models.DateTimeField(auto_now_add=True)),
                ('patient_problem', models.CharField(blank=True, max_length=100, null=True)),
                ('med_p', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quickstart_1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_salary', models.IntegerField()),
                ('hos_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quickstart_1.hospital_1')),
            ],
        ),
    ]
