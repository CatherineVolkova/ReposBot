from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
import asyncio
import random

bot = Bot("5939327600:AAFTsZklP_U0cTidkdBvghTDMBjCv_1fWek")
dp = Dispatcher(bot)
#channel = message.chat.mention if message.chat.mention is not None else ""
#start_channel = "Канал"
#prefix = "*" + start_channel + " - " + channel + "*"



first = ["Nigerundayo!", "Yare Yare Daze", "Yes, I am!", "KONO DIO DA", "MUDA MUDA MUDA", "ORA ORA ORA", "ORA ORA ORA ORA ORAAAA", "WRYYYYY", "ORA", "Is this a Jojo reference??", "OH NO!!!", "OH MY GOD!!!", "Докажи", "Я переиграл твое переигрывание", "Die deutsche Wissenchaft ist die besye der Wert", "Тот, кто смеётся с закрытыми глазами, да ещё скрестив руки, точно знает, что выиграет - Джозеф Джостар", ]
second = ["Джонатан Джостар!!!!!", "Дио.....", "Джозеф Джостар :D", "Холли Куджо ^^", "Джотаро Куджо 0_0", "Джолин Куджо :)", "Джорно Джованна UwU", "Хигашиката Джоске *-*", "Джонни Джостар!"]
prob = 50

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Greetings, ! I am JojoBot.\n" +
        "I can chat with you about bizzare adventures any time of day and night.\n" +
        "To get help press /help.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши 'Привет' чтобы поздороваться со мной и активировать диалог!")


@dp.message_handler(commands=['whatjojoru'])
async def process_whatjojoru_command(message: types.Message):
    await message.reply("Ты " + random.choice(second))


@dp.message_handler(commands=['stand'])
async def process_stand_command(message: types.Message):
    await message.reply("Ты станешь обладателем станда с вероятностью " + str(random.randint(1, 100)) + "%")


@dp.message_handler(commands=['probability'])
async def process_stand_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="10%")
    keyboard.add(button_1)
    button_2 = "50%"
    keyboard.add(button_2)
    button_3 = "100%"
    keyboard.add(button_3)
    await message.answer("Выбери новую вероятность, с которой бот будет отвечать на сообщения", reply_markup=keyboard)

@dp.message_handler(Text(equals="10%"))
async def button_1(message: types.Message):
    global prob 
    prob = 10
    await message.reply("Новая вероятность равна 10%", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(equals="50%"))
async def button_2(message: types.Message):
    global prob 
    prob = 50
    await message.reply("Отлично! Новая вероятность равна 50%", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(equals="100%"))
async def button_3(message: types.Message):
    global prob
    prob  = 100
    await message.reply("Отлично!!! Новая вероятность равна 100%", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['owner'])
async def process_help_command(message: types.Message):
    await message.answer('Owner - @CatherineVv')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
    elif (random.randint(1, 100) <= prob):
        await msg.answer(random.choice(first))


if __name__ == '__main__':
    executor.start_polling(dp)