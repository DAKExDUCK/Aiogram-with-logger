import asyncio
from functools import wraps

from aiogram import types

from bot.handlers.logger import logger

admin_list = [626591599]


def is_admin(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        message: types.Message = args[0]
        if message.from_user.id in admin_list:
            return func(*args, **kwargs)
        else:
            logger.debug('User is not admin')
            return await if_not_admin(*args, **kwargs)
    return wrapper


async def if_not_admin(message: types.Message):
    msg_to_del = await message.reply('You are not Admin')
    await asyncio.sleep(3)
    try:
        await msg_to_del.delete()
        await message.delete()
    except:
        pass