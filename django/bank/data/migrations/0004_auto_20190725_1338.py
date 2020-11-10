# Generated by Django 2.2 on 2019-07-25 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20190708_2044'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bnaker',
            new_name='Banker',
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transfer_amount', models.IntegerField()),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Banker')),
                ('Transfer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Account_holder')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_amount', models.IntegerField()),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Banker')),
                ('Loan_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Account_holder')),
            ],
        ),
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deposite_amount', models.IntegerField()),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Banker')),
                ('Deposite_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Account_holder')),
            ],
        ),
    ]