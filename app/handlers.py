from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.requests import BotDB

import app.keyboards as kb

router = Router()
BotDB = BotDB()


class AddPoints(StatesGroup):
    params = State()
    amount = State()
    description = State()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("You're in main menu\nChoose Option", reply_markup=kb.main)


@router.message(F.text == '♐️ Add Points')
async def cmd_add_points(message: Message):
    # Make sure the inline keyboard is being sent correctly
    await message.answer("Choose Parameter", reply_markup=kb.add_points)


@router.message(F.text == '〽️ Reduce Point')
async def cmd_reduce_points(message: Message):
    # Implement the reduce point functionality
    await message.answer("This feature is coming soon!")


@router.message(F.text == '📊 Get Parameters')
async def cmd_get_parameters(message: Message):
    params_data = BotDB.get_params_data()
    params_level_data = BotDB.get_params_level_data()

    await message.answer(str(params_data), parse_mode=ParseMode.HTML)
    await message.answer(str(params_level_data), parse_mode=ParseMode.HTML)

@router.message(F.text == '🔍 Others')
async def cmd_others(message : Message):
    await message.answer("Coming...", reply_markup=kb.others_tab)

@router.callback_query(F.data == 'see-history')
async def see_history(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(BotDB.get_history_data())


@router.callback_query(F.data == 'readme-description')
async def readme_description(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("https://github.com/yellowDeerrr/My-Life-Tracker-Telegram-Bot/blob/main/configREADME-PARAMS.md")

@router.callback_query(F.data == 'main-menu')
async def return_to_main_menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("You're in main menu\nChoose Option", reply_markup=kb.main)


# Make sure all callback handlers are properly registered
@router.callback_query(F.data.startswith('param-add'))
async def add_points_param(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    param = callback.data.split('-')[-1]  # Gets the parameter name from callback data.
    if param == 'self_discipline':
        param = 'Self Discipline';
    await state.update_data(param=param)  # store the parameter into the state.
    await callback.message.answer(f"How many points do you want to add to {param}?")
    await state.set_state(AddPoints.amount)


@router.message(AddPoints.amount)
async def add_points_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
        await state.update_data(amount=amount)

        await message.answer("Write a description of this action", reply_markup=kb.main)
        await state.set_state(AddPoints.description)
    except ValueError:
        await message.answer("Please enter a valid number.")
        await add_points_amount(message)


@router.message(AddPoints.description)
async def add_points_amount(message: Message, state: FSMContext):
        description = message.text
        data = await state.get_data()
        param = data['param']
        amount = data['amount']
        BotDB.add_points_param(param, amount, description)  # Update database
        await message.answer(f"Added {amount} points to {param}!")
        await cmd_add_points(message)

