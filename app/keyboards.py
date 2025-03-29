from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                                InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Add Points'),
                                     KeyboardButton(text="Reduce Point")],
                                     [KeyboardButton(text='Get Parameters')]],
                           resize_keyboard=True)


catalog = InlineKeyboardMarkup(inline_keyboard=
                               [[InlineKeyboardButton(text='T-shirts', callback_data='t-shirt')],
                               [InlineKeyboardButton(text='pants', callback_data='pants'),
                                InlineKeyboardButton(text="Кепки", callback_data='cap')]])

get_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Send number', request_contact=True)]],
    resize_keyboard=True)