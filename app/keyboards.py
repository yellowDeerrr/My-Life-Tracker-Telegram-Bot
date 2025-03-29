from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                                InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Add Points'),
                                     KeyboardButton(text="Reduce Point")],
                                     [KeyboardButton(text='Get Parameters')]],
                           resize_keyboard=True)

add_points = InlineKeyboardMarkup(inline_keyboard=
                               [[InlineKeyboardButton(text='Health', callback_data='param-add-health'),
                               InlineKeyboardButton(text='Strength', callback_data='param-add-strength')],
                               [InlineKeyboardButton(text='Intelligence', callback_data='param-add-intelligence'),
                               InlineKeyboardButton(text='Wisdom', callback_data='param-add-wisdom')],
                               [InlineKeyboardButton(text='Charisma', callback_data='param-add-charisma'),
                               InlineKeyboardButton(text='Confidence', callback_data='param-add-confidence')],
                               [InlineKeyboardButton(text='Self discipline', callback_data='param-add-self_discipline'),
                               InlineKeyboardButton(text='Skills', callback_data='param-add-skills')],
                               [InlineKeyboardButton(text='Happiness', callback_data='param-add-happiness'),
                               InlineKeyboardButton(text='Recovery', callback_data='param-add-recovery')],
                                [InlineKeyboardButton(text='Back', callback_data='main-menu')]])

catalog = InlineKeyboardMarkup(inline_keyboard=
                               [[InlineKeyboardButton(text='T-shirts', callback_data='t-shirt')],
                               [InlineKeyboardButton(text='pants', callback_data='pants'),
                                InlineKeyboardButton(text="Кепки", callback_data='cap')]])

get_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Send number', request_contact=True)]],
    resize_keyboard=True)