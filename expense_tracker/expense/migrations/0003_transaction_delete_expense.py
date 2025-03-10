# Generated by Django 5.1.7 on 2025-03-08 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_expense_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Shopping', 'Shopping'), ('Bills', 'Bills'), ('Other', 'Other'), ('Salary', 'Salary'), ('Freelance', 'Freelance'), ('Investments', 'Investments')], max_length=50)),
                ('transaction_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
