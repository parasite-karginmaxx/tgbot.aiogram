from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Узнать статус', callback_data='status_now')
        #  InlineKeyboardButton(text='Расписание',
        #                       url='https://drive.google.com/drive/folders/1Z8V1jh0OZuW-e3m-O05D0n88_OdDPyTV',
        #                       callback_data='cb_btn_3_main')],
        # [InlineKeyboardButton(text='Отправить уведомление', callback_data='cb_ikb_groups')
        ]
    ])
    return ikb

def cancel_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отмена',
                              callback_data='cancel')]
    ])
    return ikb
    

def status_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Повысить статус',
                             callback_data='set_admin'),
         InlineKeyboardButton(text='Отмена',
                              callback_data='cancel')]
    ])
    return ikb

def get_main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Помощь')],
        [KeyboardButton(text='/description')]
        [KeyboardButton(text='Мой статус')]
    ], resize_keyboard=True)
    return kb
