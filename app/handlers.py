from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.requests import BotDB

import app.keyboards as kb

router = Router()
BotDB = BotDB()


class AddPoints(StatesGroup):
    params = State()
    amount = State()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer("You're in main menu\nChoose Option", reply_markup=kb.main)


@router.message(F.text == 'Add Points')
async def cmd_add_points(message: Message):
    # Make sure the inline keyboard is being sent correctly
    await message.answer("Choose Parameter", reply_markup=kb.add_points)


@router.message(F.text == 'Reduce Point')
async def cmd_reduce_points(message: Message):
    # Implement the reduce point functionality
    await message.answer("This feature is coming soon!")


@router.message(F.text == 'Get Parameters')
async def cmd_get_parameters(message: Message):
    params_data = BotDB.get_params_data()
    params_level_data = BotDB.get_params_level_data()

    await message.answer(str(params_data), parse_mode=ParseMode.HTML)
    await message.answer(str(params_level_data), parse_mode=ParseMode.HTML)


@router.message(Command('get'))
async def cmd_get(message: Message):
    await message.answer(str(BotDB.get_params_data()), parse_mode=ParseMode.HTML)


# Make sure all callback handlers are properly registered
@router.callback_query(F.data.startswith('param-add'))
async def add_points_param(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    param = callback.data.split('-')[-1]  # Gets the parameter name from callback data.
    print(f"Parameter selected: {param}")
    await state.update_data(param=param)  # store the parameter into the state.
    await callback.message.answer(f"How many points do you want to add to {param}?")
    await state.set_state(AddPoints.amount)


@router.callback_query(F.data == 'main-menu')
async def return_to_main_menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("You're in main menu\nChoose Option", reply_markup=kb.main)


@router.message(AddPoints.amount)
async def add_points_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
        data = await state.get_data()
        param = data['param']
        BotDB.update_param(param, amount)  # Update database
        await message.answer(f"Added {amount} points to {param}!")
        # Return to main menu after completion
        await message.answer("Choose Option", reply_markup=kb.main)
    except ValueError:
        await message.answer("Please enter a valid number.")
    finally:
        await state.clear()