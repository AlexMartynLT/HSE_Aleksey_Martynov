import sqlite3
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Импортируем токен из нашего файла config
from config import TOKEN

# Определяем "состояния" разговора.
# Это как главы в книге: AGE (спрашиваем возраст), GENRE (спрашиваем жанр), MOVIE (спрашиваем фильм).
AGE, GENRE, MOVIE = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начинает разговор и спрашивает возраст."""
    await update.message.reply_text(
        "Привет! Давай пройдем небольшой опрос о кино. "
        "Если захочешь прервать, просто отправь команду /cancel.\n\n"
        "Итак, первый вопрос: сколько тебе лет?"
    )
    # Возвращаем состояние AGE, чтобы ConversationHandler знал, какой шаг следующий
    return AGE


async def age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет возраст и спрашивает любимый жанр."""
    user_age = update.message.text
    # Проверяем, является ли введенный текст числом
    if not user_age.isdigit():
        await update.message.reply_text("Пожалуйста, введи возраст цифрами.")
        return AGE  # Остаемся в том же состоянии, ждем корректного ввода

    # Сохраняем возраст во временное хранилище
    context.user_data['age'] = int(user_age)

    await update.message.reply_text(
        f"Понял, тебе {user_age}. Теперь скажи, какой твой любимый жанр кино?"
    )
    # Переключаемся на следующее состояние - GENRE
    return GENRE


async def genre(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет жанр и спрашивает любимый фильм."""
    # Сохраняем ответ в user_data
    context.user_data['genre'] = update.message.text

    await update.message.reply_text(
        f"Отличный выбор! А какой твой самый любимый фильм?"
    )
    # Переключаемся на состояние MOVIE
    return MOVIE


async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет фильм и заканчивает разговор."""
    user_data = context.user_data
    user_data['movie'] = update.message.text

    # Подключаемся к базе данных
    conn = sqlite3.connect('anketa.db')
    cursor = conn.cursor()

    # Вставляем данные в таблицу
    try:
        cursor.execute(
            'INSERT INTO anketa (user_id, age, genre, movie) VALUES (?, ?, ?, ?)',
            (
                update.message.from_user.id,
                user_data['age'],
                user_data['genre'],
                user_data['movie']
            )
        )
        conn.commit()
        await update.message.reply_text(
            "Спасибо за твои ответы! Анкета завершена."
        )
    except sqlite3.IntegrityError:
        # Этот блок сработает, если user_id уже есть в базе (UNIQUE)
        await update.message.reply_text(
            "Похоже, ты уже проходил этот опрос. Спасибо!"
        )
    finally:
        # Обязательно закрываем соединение с базой данных
        conn.close()
        # Очищаем временные данные
        user_data.clear()

    # Завершаем разговор
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отменяет и завершает разговор."""
    user = update.message.from_user
    await update.message.reply_text(
        f"Анкетирование прервано. Спасибо, {user.first_name}!",
        reply_markup=ReplyKeyboardRemove()  # Убираем клавиатуру, если она была
    )
    # Завершаем разговор
    return ConversationHandler.END


def main() -> None:
    """Запускает бота."""
    application = Application.builder().token(TOKEN).build()

    # Создаем ConversationHandler с нашими состояниями
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, age)],
            GENRE: [MessageHandler(filters.TEXT & ~filters.COMMAND, genre)],
            MOVIE: [MessageHandler(filters.TEXT & ~filters.COMMAND, movie)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Добавляем обработчик разговоров в приложение
    application.add_handler(conv_handler)

    # Запускаем бота
    application.run_polling()


if __name__ == "__main__":
    main()