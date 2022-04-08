# Generated by Django 4.0.2 on 2022-03-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile_num', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_amount', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.BigIntegerField()),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.card')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customer')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.category')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.item')),
            ],
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_number', models.IntegerField()),
                ('profit', models.BigIntegerField()),
                ('sold_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product'),
        ),
        migrations.AddField(
            model_name='card',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customer'),
        ),
    ]
