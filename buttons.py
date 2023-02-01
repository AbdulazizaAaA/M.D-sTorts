from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuMain = ReplyKeyboardMarkup(
    keyboard = [
        [
             KeyboardButton(text="Buyurtma berish"),
             KeyboardButton(text="Menu")
        ],
        [
             KeyboardButton(text="Lokatsiya"),
        ]
    ]
)