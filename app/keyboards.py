from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                                InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='♐️ Add Points'),
                                     KeyboardButton(text="〽️ Reduce Point")],
                                     [KeyboardButton(text='📊 Get Parameters')],
                                     [KeyboardButton(text='🔍 Others')]],
                           resize_keyboard=True)

others_tab = InlineKeyboardMarkup(inline_keyboard=
                                  [[InlineKeyboardButton(text='🗄 See History', callback_data='see-history')],
                                   [InlineKeyboardButton(text='📋 Description Of Parameters', callback_data='readme-description')]])

add_points = InlineKeyboardMarkup(inline_keyboard=
                               [[InlineKeyboardButton(text='❤️ Health', callback_data='param-add-health'),
                               InlineKeyboardButton(text='💪 Strength', callback_data='param-add-strength')],
                               [InlineKeyboardButton(text='🧠 Intelligence', callback_data='param-add-intelligence'),
                               InlineKeyboardButton(text='🦉 Wisdom', callback_data='param-add-wisdom')],
                               [InlineKeyboardButton(text='🤩 Charisma', callback_data='param-add-charisma'),
                               InlineKeyboardButton(text='😎 Confidence', callback_data='param-add-confidence')],
                               [InlineKeyboardButton(text='🧘 Self discipline', callback_data='param-add-self_discipline'),
                               InlineKeyboardButton(text='🛠️ Skills', callback_data='param-add-skills')],
                               [InlineKeyboardButton(text='😃 Happiness', callback_data='param-add-happiness'),
                               InlineKeyboardButton(text='🩹 Recovery', callback_data='param-add-recovery')],
                                [InlineKeyboardButton(text='⬅️ Back', callback_data='main-menu')]])

reduce_points = InlineKeyboardMarkup(inline_keyboard=
                               [[InlineKeyboardButton(text='❤️ Health', callback_data='param-reduce-health'),
                               InlineKeyboardButton(text='💪 Strength', callback_data='param-reduce-strength')],
                               [InlineKeyboardButton(text='🧠 Intelligence', callback_data='param-reduce-intelligence'),
                               InlineKeyboardButton(text='🦉 Wisdom', callback_data='param-reduce-wisdom')],
                               [InlineKeyboardButton(text='🤩 Charisma', callback_data='param-reduce-charisma'),
                               InlineKeyboardButton(text='😎 Confidence', callback_data='param-reduce-confidence')],
                               [InlineKeyboardButton(text='🧘 Self discipline', callback_data='param-reduce-self_discipline'),
                               InlineKeyboardButton(text='🛠️ Skills', callback_data='param-reduce-skills')],
                               [InlineKeyboardButton(text='😃 Happiness', callback_data='param-reduce-happiness'),
                               InlineKeyboardButton(text='🩹 Recovery', callback_data='param-reduce-recovery')],
                                [InlineKeyboardButton(text='⬅️ Back', callback_data='main-menu')]])