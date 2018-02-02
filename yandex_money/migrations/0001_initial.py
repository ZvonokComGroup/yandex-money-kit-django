# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 10:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import yandex_money.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('shop_id', models.PositiveIntegerField(default=456, verbose_name='ID магазина')),
                ('scid', models.PositiveIntegerField(default=123, verbose_name='Номер витрины')),
                ('customer_number', models.CharField(default=yandex_money.models.get_default_as_uuid, max_length=64, verbose_name='Идентификатор плательщика')),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Сумма заказа')),
                ('article_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Идентификатор товара')),
                ('payment_type', models.CharField(choices=[('PC', 'Кошелек Яндекс.Деньги'), ('AC', 'Банковская карта'), ('GP', 'Наличными через кассы и терминалы'), ('MC', 'Счет мобильного телефона'), ('WM', 'Кошелек WebMoney'), ('SB', 'Сбербанк: оплата по SMS или Сбербанк Онлайн'), ('AB', 'Альфа-Клик'), ('MA', 'MasterPass'), ('PB', 'Интернет-банк Промсвязьбанка'), ('QW', 'QIWI Wallet'), ('CR', 'Заплатить по частям')], default='PC', max_length=2, verbose_name='Способ платежа')),
                ('order_number', models.CharField(default=yandex_money.models.get_default_as_uuid, max_length=64, verbose_name='Номер заказа')),
                ('cps_email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email плательщика')),
                ('cps_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон плательщика')),
                ('success_url', models.URLField(default='http://example.com/success-payment/', verbose_name='URL успешной оплаты')),
                ('fail_url', models.URLField(default='http://example.com/fail-payment/', verbose_name='URL неуспешной оплаты')),
                ('status', models.CharField(choices=[('processed', 'Processed'), ('success', 'Success'), ('fail', 'Fail')], default='processed', max_length=16, verbose_name='Статус')),
                ('invoice_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер транзакции оператора')),
                ('shop_amount', models.DecimalField(blank=True, decimal_places=2, help_text='За вычетом процента оператора', max_digits=15, null=True, verbose_name='Сумма полученная на р/с')),
                ('order_currency', models.PositiveIntegerField(choices=[(643, 'Рубли'), (10643, 'Тестовая валюта')], default=643, verbose_name='Валюта')),
                ('shop_currency', models.PositiveIntegerField(blank=True, choices=[(643, 'Рубли'), (10643, 'Тестовая валюта')], default=643, null=True, verbose_name='Валюта полученная на р/с')),
                ('performed_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Время выполнение запроса')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'платежи',
                'verbose_name': 'платёж',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([('shop_id', 'order_number')]),
        ),
    ]
