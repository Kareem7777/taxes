# Generated by Django 3.2 on 2021-06-06 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxesreceipt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('internal_id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('document_type', models.CharField(max_length=1)),
                ('date_time_issued', models.DateTimeField(auto_now_add=True)),
                ('currency', models.CharField(max_length=3)),
                ('currency_rate', models.DecimalField(decimal_places=12, max_digits=28)),
                ('extra_discount_amount', models.DecimalField(decimal_places=12, max_digits=28)),
                ('customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taxesreceipt.customer')),
            ],
        ),
        migrations.AddField(
            model_name='invoice_line',
            name='invoice_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taxesreceipt.invoice'),
        ),
        migrations.AddField(
            model_name='invoice_result',
            name='invoice_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taxesreceipt.invoice'),
        ),
    ]