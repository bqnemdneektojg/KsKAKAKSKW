# ---- Импорт Модулей ---- #
import asyncio
import smtplib
from sendinblue import SendinBlue
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aiogram.dispatcher import FSMContext
from aiocryptopay.const import InvoiceStatus
from aiogram.utils.exceptions import Throttled
from aiocryptopay import AioCryptoPay, Networks
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# --- Импорт Конфигов --- #
from config import *
from states import *
from bomber import *
from database import *
from keyboards import *
# --- Соединяем платежки --- #

crypto = AioCryptoPay(token=CRYPTOPAY_TOKEN, network=Networks.MAIN_NET)
storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=storage)
# --- SendinBlue --- #
sendinblue = SendinBlue(api_key='YOUR_SENDINBLUE_API_KEY'
# --- Создаем старт --- #
@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=1)
async def start(message: types.Message):
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEJjSlkoEihmAAB4-w84tUzDBjiLWxsvewAAmQ6AALgo4IH_LAjcdV4gS0vBA')
    if not Users.user_exists(message.from_user.id):

# --- Разбор admin --- #
await message.answer(f'''<b>🕷️ Приветствую в BuddiesMailer!
<i>Используй кнопки ниже, чтобы управлять ботом:</i></b>''', reply_markup=start_keyboard(message.from_user.id))

@dp.message_handler(text='🥷 Админка')
@dp.throttled(anti_flood, rate=1)
async def admin(message: types.Message):
    if message.from_user.id in aids:
        await message.answer(f'''<b>🥷 Админ-панель

👥 Пользователей в боте:</b> <code>{Users.get_users_count()}</code>
<b>🤵🏼‍♂️ С доступом:</b> <code>{Users.get_subs_count()}</code>


@dp.message_handler(text='🕸️ Открыть меню')
async def open_menu(message: types.Message):
    await message.answer('<b>🔯 Меню:</b>', reply_markup=menu_keyboard(message.from_user.id))

dp.callback_query_handler(text='🐦‍⬛ Отправить письмо')
@dp.throttled(anti_flood, rate=1)
async def bomber(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

    if not Users.have_sub(callback_query.from_user.id):
        await callback_query.message.answer(f'<b>✖️ Для продолжения оплатите доступ!</b>', reply_markup=menu_keyboard(callback_query.from_user.id))
    else:
        if
async def sendm(query: CallbackQuery, state: FSMContext):
    await query.message.answer('🕸️ Введите почту отправителя')
    await state.set_state(BotState.sender)

@dp.message(BotState.sender)
async def san(message: Message, state: FSMContext):
    await state.update_data(send=message.text)
    await message.answer('🕷️ Введите почту получателя')
    await state.set_state(BotState.recp)

@dp.message(BotState.recp)
async def rec(message: Message, state: FSMContext):
    await state.update_data(recp=message.text)
    await message.answer('✖️ Введите тему сообщения')
    await state.set_state(BotState.subject)

@dp.message(BotState.subject)
async def sub(message: Message, state: FSMContext):
    await state.update_data(subj=message.text)
    await message.answer('🐦‍⬛ Введите текст сообщения')
    await state.set_state(BotState.text)

@dp.message(BotState.text)
async def txt(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
   try:
      mail.send_mail(sendermail=data['send'], recpmail=data['recp'], mailsubject=data['subj'], text=data['text'])
    except Exception as exc:
        await message.answer(f"✖️ Письмо не отправлено. {exc}")
        return
    await state.clear()
    await message.answer('🥷 Письмо отправлено!')


          # --- Профиль --- #
@dp.callback_query_handler(text='profile')
@dp.throttled(anti_flood, rate=1)
async def profile(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

    if not Users.have_sub(callback_query.from_user.id):
        await callback_query.message.answer(f'''<b>🕸️ ID:</b> <code>{callback_query.from_user.id}</code>

<b>🕷️ Доступ:</b> <code>отсутствует</code>''', reply_markup=menu_keyboard(callback_query.from_user.id))
    else:
        await callback_query.message.answer(f'''<b>🕸️ ID:</b> <code>{callback_query.from_user.id}</code>

<b>🕷️ Доступ заканчивается в:</b> <code>{Users.sub_until(callback_query.from_user.id)}</code>''', reply_markup=menu_keyboard(callback_query.from_user.id))

        # --- Информация --- #
@dp.callback_query_handler(text='information')
@dp.throttled(anti_flood, rate=1)
async def information(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

    await callback_query.message.answer(f'''<b>🥷 Администратор: @MDMA_NUXACH
🕸️ Канал с новостями: @BuddiesMailer</b>''', reply_markup=menu_keyboard(callback_query.from_user.id))

@dp.callback_query_handler(text='back')
@dp.throttled(anti_flood, rate=1)
async def back(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

# --- Проверка почт на валидность --- #
dp.callback_query_handler(text='takesub')
@dp.throttled(anti_flood, rate=1)
async def takesub(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in aids:
        await callback_query.message.answer('<b>


    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEJjSlkoEihmAAB4-w84tUzDBjiLWxsvewAAmQ6AALgo4IH_LAjcdV4gS0vBA')
    await callback_query.message.answer(f'''<b>🕷️ Приветствую в BuddiesMailer!
<i>Используй кнопки ниже, чтобы управлять ботом:</i></b>''', reply_markup=start_keyboard(message.from_user.id))


@dp.callback_query_handler(text_startswith='check_cryptobot:')
@dp.throttled(anti_flood, rate=1)
async def check_cryptobot(callback_query: types.CallbackQuery):
    if not Users.have_sub(callback_query.from_user.id):
        invoices = await crypto.get_invoices(invoice_ids=callback_query.data.split(':')[1])
        if invoices[0].status == InvoiceStatus.PAID:
            await callback_query.message.delete()
            Users.give_sub(callback_query.from_user.id, int(callback_query.data.split(':')[2]))


            await callback_query.message.answer(f'<b>💣 Доступ оплачен. Приятных писем!</b>', reply_markup=menu_keyboard(callback_query.from_user.id))
        elif invoices[0].status == InvoiceStatus.ACTIVE:
            await callback_query.answer(f'✖️  Доступ не оплачен!')
        else:
            await callback_query.message.delete()
            await callback_query.message.answer(f'<b>🕸️ Платёж больше не активен!</b>', reply_markup=menu_keyboard(callback_query.from_user.id))
    else:
        await callback_query.message.answer(f'<b>🐦‍⬛ У вас уже имеется доступ, используйте кнопки:</b>', reply_markup=menu_keyboard(callback_query.from_user.id))



@dp.callback_query_handler(text='dump')
@dp.throttled(anti_flood, rate=1)
async def dump(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in aids:
        await bot.send_document(callback_query.from_user.id, open('bot.db', 'rb'))

@dp.callback_query_handler(text='mail')
@dp.throttled(anti_flood, rate=1)
async def mail(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in aids:
        await Mail.photo.set()
        await callback_query.message.answer('''<b>🎩 Загрузите фото рассылки

<i>Для пропуска напишите "-"</i></b>''')

@dp.message_handler(content_types=['photo'], state=Mail.photo)
async def mail2(message: types.Message, state: FSMContext):
    if message.from_user.id in aids:
        async with state.proxy() as data:
            try:
                data['photo'] = message.photo[0].file_id
            except:
                data['photo'] = None
        
        await Mail.next()
        await message.answer('''<b>🥷 Теперь введите текст рассылки

<i>Поддержка разметки "HTML"</i></b>''')

@dp.message_handler(state=Mail.photo)
async def mail2(message: types.Message, state: FSMContext):
    if message.from_user.id in aids:
        async with state.proxy() as data:
            try:
                data['photo'] = message.photo[0].file_id
            except:
                data['photo'] = None
        
        await Mail.next()
        await message.answer('''<b>🕸️ Теперь введите текст рассылки

<i>Поддержка разметки "HTML"</i></b>''')

@dp.message_handler(state=Mail.description)
async def mail3(message: types.Message, state: FSMContext):
    if message.from_user.id in aids:
        async with state.proxy() as data:
            data['description'] = message.text 

            g, e = 0, 0
            for user in Users.get_users():
                try:
                    await bot.send_photo(user.UID, data['photo'], data['description'], parse_mode='html')
                    g += 1
                except:
                    try:
                        await bot.send_message(user.UID, data['description'], parse_mode='html')
                        g += 1
                    except:
                        e += 1

        await state.finish()
        await message.answer(f'''<b>⏱ Рассылка окончена!

🕷️ Получили сообщение:</b> <code>{g}</code>
<b>🕷️ Не получили:</b> <code>{e}</code>''', reply_markup=admin_keyboard())

@dp.callback_query_handler(text='givesub')
@dp.throttled(anti_flood, rate=1)
async def givesub(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in aids:
        await callback_query.message.answer('<b>🕸️ Введите ID пользователя которому хотите выдать доступ:</b>', reply_markup=cancel_keyboard())
        await GiveSub.id.set()

@dp.callback_query_handler(text='takesub')
@dp.throttled(anti_flood, rate=1)
async def takesub(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in aids:
        await callback_query.message.answer('<b>🕸️ Введите ID пользователя которому хотите забрать доступ:</b>', reply_markup=cancel_keyboard())
        await TakeSub.id.set()

@dp.message_handler(state=GiveSub.id)
async def givesub2(message: types.Message, state: FSMContext):
    if message.from_user.id in aids:
        async with state.proxy() as data:
            data['id'] = int(message.text)
        
        await message.answer('<b>🐦‍⬛ Введите количество дней доступа:</b>', reply_markup=cancel_keyboard())
        await GiveSub.next()

@dp.message_handler(state=GiveSub.days)
async def givesub3(message: types.Message, state: FSMContext):
    if message.from_user.id in aids:
        async with state.proxy() as data:
            data['days'] = int(message.text)
            id = data['id']
            days = data['days']
        
        Users.give_sub(id, days)
        await bot.send_message(id, f'<b>🕷️ Вам выдан доступ на</b> <code>{days}</code> <b>дней!</b>', reply_markup=start_keyboard(message.from_user.id))
        await state.finish()
        await message.answer('<b>🕷️ Пользователю выдан доступ!</b>', reply_markup=admin_keyboard())

@dp.message_handler(state=TakeSub.id)
async def takesub2(message: types.Message, state: FSMContext):
    if message.from_user.id in aids:
        async with state.proxy() as data:
            data['id'] = int(message.text)
            id = data['id']
        
        Users.take_sub(id)
        await bot.send_message(id, f'<b>✖️ У вас забрали доступ!</b>', reply_markup=start_keyboard(message.from_user.id))
        await state.finish()
        await message.answer('<b>🕷️ Пользователю забрали доступ!</b>', reply_markup=admin_keyboard())

@dp.message_handler(text='✖️ Отмена', state='*')
@dp.throttled(anti_flood, rate=1)
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEJjSlkoEihmAAB4-w84tUzDBjiLWxsvewAAmQ6AALgo4IH_LAjcdV4gS0vBA')
    await message.answer(f'''<b>🕷️ Приветствую в BuddiesMailer!
<i>Используй кнопки, чтобы управлять ботом</i></b>''', reply_markup=start_keyboard(message.from_user.id))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
