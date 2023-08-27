from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from database import *
from config import *

def start_keyboard(UID):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)

	b1 = KeyboardButton('🕸️ Открыть меню')
	b2 = KeyboardButton('🥷 Админка')

	markup.add(b1)

	if UID in aids:
		markup.add(b2)

	return markup

def menu_keyboard(UID):
	markup = InlineKeyboardMarkup(resize_keyboard=True)

	b = InlineKeyboardButton('🕷️ Купить доступ', callback_data='buy_access')
	b1 = InlineKeyboardButton('🐦‍⬛ Отправить письмо', callback_data='send_mail')
	b2 = InlineKeyboardButton('✖️ Мой профиль', callback_data='profile')
	b3 = InlineKeyboardButton('📓 Справочник', callback_data='helper')
	b4 = InlineKeyboardButton('💣 Проверка почт', callback_data='validator_mail')
	b5 = InlineKeyboardButton('🕸️ Временная почта, callback_data='tempmail')
	b6 = InlineKeyboardButton('🕷️ Информация', callback_data='information')

	if Users.have_sub(UID):
		markup.add(b1)
		markup.add(b2, b3)
		markup.add(b4)
		markup.add(b5, b6)
	else:
		markup.add(b)
		markup.add(b2, b3)
		markup.add(b4)
		markup.add(b5, b6)

	return markup

def methods_pay_keyboard(price):
	markup = InlineKeyboardMarkup(resize_keyboard=True)


	b2 = InlineKeyboardButton('🕸️ Cryptobot', callback_data=f'buy_access:cryptobot:{price}')
	b3 = InlineKeyboardButton('🕷️ Вернуться в меню', callback_data='back')

	markup.add(b1)
	markup.add(b2)
	markup.add(b3)

	return markup

def time_sub_keyboard():
	markup = InlineKeyboardMarkup(resize_keyboard=True)

	b1 = InlineKeyboardButton('✖️ Месяц', callback_data=f'buy_access_time:30')
 b2 = InlineKeyboardButton('✖️ Два месяца',
callback_data=f'buy_access_time:60')
	b3 = InlineKeyboardButton('🕷️ Вернуться в меню', callback_data='back')

	markup.add(b1, b2)
	markup.add(b3)

	return markup

def admin_keyboard():
	markup = InlineKeyboardMarkup(resize_keyboard=True)

	b1 = InlineKeyboardButton('🕷️ Рассылка', callback_data='mail')
	b2 = InlineKeyboardButton('🕸️ Выгрузка БД', callback_data='dump')
	b3 = InlineKeyboardButton('🐦‍⬛ Выдать доступ', callback_data='givesub')
	b4 = InlineKeyboardButton('✖️ Забрать доступ', callback_data='takesub')

	markup.add(b1)
	markup.add(b2)
	markup.add(b3)
	markup.add(b4)

	return markup

def stop_bomber_keyboard(BID):
	markup = InlineKeyboardMarkup(resize_keyboard=True)


def cancel_keyboard():
	markup = ReplyKeyboardMarkup(resize_keyboard=True)

	b1 = KeyboardButton('✖️ Отмена')

	markup.add(b1)
	return markup

def check_payment_keyboard(invoice_id, pay, days):
	markup = InlineKeyboardMarkup(resize_keyboard=True)

	b1 = InlineKeyboardButton('🕷️ Проверить оплату', callback_data=f'check_{pay}:{invoice_id}:{days}')
	markup.add(b1)
	return markup


