from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.requests import BotDB

import app.keyboards as kb

router = Router()
BotDB = BotDB()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

@router.message(Command("get"))
async def get_users(message : Message):
    res = BotDB.get_params_data()
    await message.answer(str(res), parse_mode=ParseMode.HTML)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Choose option", reply_markup=kb.main)

@router.message(F.text == 'Add Points')
async def catalog(message : Message):
    await message.answer('Choose type of product', reply_markup=kb.catalog)
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("help")

@router.callback_query(F.data == 't-shirt')
async def t_shirts(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Chosen t shirts!")


@router.message(Command('register'))
async def register(message : Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Enter your name')


@router.message(Register.name)
async def register_name(message : Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Enter your age")


@router.message(Register.age)
async def register_age(message : Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer("Enter you number", reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message : Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Your name: {data["name"]}\nYour age: {data["age"]}\nYour number: {data["number"]}')
    await state.clear()
