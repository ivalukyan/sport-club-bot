import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from env import TOKEN
from src.auth import login
from src.profile import profile
from src.schedules import training_session
from src.stats import top
from src.admin import adm
from src.srm.srm_bot import task, CRMain
from src.db.router import cursor,conn


router = Router()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router.message(CommandStart())
async def command_start(message: Message) -> None:

    await message.answer(
        f"Здравствуйте, <i>{message.from_user.first_name}</i>, вас приветствует бот спортивного клуба\n\n"
        f"Для того чтобы продолжить ввойдите в свой аккканут с помощью команды - <b>/login</b>\n"
        f"Для того чтобы узнать возможонсти бота - <b>/help</b>")


@router.message(Command('help'))
async def command_help(message: Message) -> None:
    await message.answer(f"‼️<b>КОМАНДЫ</b>‼️\n\n"
                         f"<i>/help</i> - возможность посмотреть все команды\n"
                         f"<i>/login</i> - команда для входа пользователя\n"
                         f"<i>/profile</i> - команда для вызова профиля\n"
                         f"<i>/schedule</i> - команда для записи на тренировку\n"
                         f"<i>/top</i> - команда для просмотра рейтингов")


@router.message(Command('update'))
async def command_update(message: Message) -> None:
    await CRMain(message)


@router.message(Command('delete'))
async def command_delete(message: Message) -> None:
    cursor.execute("""DELETE FROM public.bot_app_profile""")
    conn.commit()
    await message.answer("Пользователи удалены!")


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp = Dispatcher()
    dp.include_routers(login.router, training_session.router, top.router, adm.router, profile.router, router)
    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    asyncio.run(main())
