import logging
from enum import Enum, auto

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ====== ЛОГИ ======
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ====== СОСТОЯНИЯ КОНЕЧНОГО АВТОМАТА ======
class State(Enum):
    S0_WAIT_NAME = auto()
    S1_WAIT_AGE = auto()
    S2_SHOW_RESULT = auto()

DEFAULT_STATE = State.S0_WAIT_NAME

# Храним состояние и данные пользователя в user_data (встроенное хранилище PTB)
# context.user_data["state"] -> State
# context.user_data["name"]  -> str
# context.user_data["age"]   -> int


def get_state(context: ContextTypes.DEFAULT_TYPE) -> State:
    return context.user_data.get("state", DEFAULT_STATE)


def set_state(context: ContextTypes.DEFAULT_TYPE, state: State) -> None:
    context.user_data["state"] = state


# ====== ОБРАБОТЧИКИ ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    set_state(context, State.S0_WAIT_NAME)
    context.user_data.pop("name", None)
    context.user_data.pop("age", None)
    await update.message.reply_text(
        "Привет! Я бот с конечным автоматом из 3 состояний.\n"
        "Состояние S0: введи своё имя."
    )


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Доп. команда, чтобы вручную сбросить
    await start(update, context)


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    state = get_state(context)

    # ====== S0: ждём имя ======
    if state == State.S0_WAIT_NAME:
        if not text:
            await update.message.reply_text("Имя не может быть пустым. Введи имя ещё раз:")
            return

        context.user_data["name"] = text
        set_state(context, State.S1_WAIT_AGE)
        await update.message.reply_text(
            f"Отлично, {text}!\n"
            "Состояние S1: теперь введи свой возраст (числом)."
        )
        return

    # ====== S1: ждём возраст ======
    if state == State.S1_WAIT_AGE:
        if not text.isdigit():
            await update.message.reply_text("Возраст нужно ввести числом. Попробуй ещё раз:")
            return

        age = int(text)
        if age <= 0 or age > 120:
            await update.message.reply_text("Введи реальный возраст (1..120):")
            return

        context.user_data["age"] = age
        set_state(context, State.S2_SHOW_RESULT)

        name = context.user_data.get("name", "Неизвестно")
        await update.message.reply_text(
            "Состояние S2: итог.\n"
            f"Тебя зовут: {name}\n"
            f"Твой возраст: {age}\n\n"
            "Напиши любое сообщение — и мы вернёмся в S0 (ввод имени)."
        )
        return

    # ====== S2: показываем итог и возвращаемся в S0 ======
    if state == State.S2_SHOW_RESULT:
        set_state(context, State.S0_WAIT_NAME)
        context.user_data.pop("name", None)
        context.user_data.pop("age", None)
        await update.message.reply_text(
            "Снова S0: введи своё имя."
        )
        return

    # На всякий случай, если состояние сломалось
    set_state(context, DEFAULT_STATE)
    await update.message.reply_text("Состояние сброшено. Введи имя:")


def main() -> None:
    # Вставь сюда токен от @BotFather
    TOKEN = "8240592654:AAHvujEjt9hZajXvaH2O69VyklBGHNZs-Ew"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.run_polling()


if __name__ == "__main__":
    main()
