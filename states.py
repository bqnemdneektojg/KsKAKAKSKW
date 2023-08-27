rom aiogram.dispatcher.filters.state import State, StatesGroup

class Mail(StatesGroup):
    photo = State()
    description = State()

class sendmail(StatesGroup):
    sender = State()
    recp = State()
    subject = State()
    text = State()

class GiveSub(StatesGroup):
    id = State()
    days = State()

class TakeSub(StatesGroup):
    id = State()