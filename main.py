import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
token = os.getenv(key='TOKEN_API')
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    # check_password = State()
    role = State()


async def on_startup(_):
    print("Я запустился!")


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message) -> None:
    reply_text = f'Добро пожаловать, {msg.from_user.first_name}!'
    await msg.answer(text=reply_text)
    await msg.delete()


@dp.message_handler(commands=['setadmin'])
async def enter_password(msg: types.Message) -> None:
    await msg.reply(text="Введите пароль:")
    await ProfileStatesGroup.role.set()


# @dp.message_handler(content_types=['text'], state=ProfileStatesGroup.check_password)
# async def cmd_change_status(msg: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['check_password'] = msg.text
#     await msg.reply('Ваш статус обновлен до Администратора!')
#     await state.next()


@dp.message_handler(content_types=['text'], state=ProfileStatesGroup.role)
async def load_role(msg: types.Message, state: FSMContext) -> None:
    if str(msg.text) == os.getenv(key='PASSWORD'):
        async with state.proxy() as data:
            data['role'] = 'admin'
        await msg.reply('Ваш статус повышен!') 
    else:
        await msg.reply(text='Неверный пароль')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
