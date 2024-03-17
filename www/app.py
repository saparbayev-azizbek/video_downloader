from aiogram import executor

from aiogram import types
from instaapi import insta
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("assalomu alaykum")

@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
    await message.answer("assalomu alaykum yordam")

@dp.message_handler(Text(startswith='https://www.instagram.com'))
async def image(message: types.Message):
    msg = message.text
    res = insta(msg)
    try:
        if res['Type'] == 'Post-Video':
            await message.answer_video(video=res['media'])
        if res['Type'] == 'Post-Image':
            await message.answer_photo(photo=res['media'])
        if res['Type'] == 'Carousel':
            media_group = []
            for i in range(len(res['media'])):
                if res['media_with_thumb'][i]['Type'] == 'Image':
                    media_group.append(types.InputMediaPhoto(res['media'][i]))
                elif res['media'][i]['Type'] == 'Video':
                    media_group.append(types.InputMediaVideo(res['media'][i]['media']))

            await bot.send_media_group(chat_id=message.chat.id, media=media_group)
            media_group = []
    except:
        await message.answer("Fayl topilmadi")



async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
