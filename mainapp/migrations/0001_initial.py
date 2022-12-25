# Generated by Django 4.0.1 on 2022-04-23 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Bid_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_bid_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bid_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Businessman_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=15)),
                ('user_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('pan_card', models.CharField(max_length=15)),
                ('gst_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('bank_account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=20)),
                ('account_holder_name', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Farmers_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('pan_card', models.IntegerField(null=True)),
                ('adhar_card', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('bank_account_no', models.IntegerField(null=True)),
                ('account_holder_name', models.CharField(max_length=30, null=True)),
                ('ifsc_code', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Market_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_sale_price', models.IntegerField()),
                ('picking_address', models.CharField(max_length=30)),
                ('delivery_address', models.CharField(max_length=30)),
                ('delivery_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=30)),
                ('subtype', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('district_name', models.CharField(max_length=30)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.CharField(max_length=300)),
                ('product_image1', models.FileField(upload_to='images')),
                ('product_image2', models.FileField(upload_to='images')),
                ('product_video', models.FileField(upload_to='videos')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.farmers_detail')),
            ],
        ),
    ]