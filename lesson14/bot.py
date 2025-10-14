# Импортируем нужные компоненты из библиотеки
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Импортируем наш токен из файла config
from config import TOKEN


# --- Функции-обработчики ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с меню, когда пользователь вводит команду /start."""
    # Создаем список кнопок. Каждый вложенный список - это один ряд кнопок.
    keyboard = [
        [KeyboardButton("Выбор формы (ИП/ООО)")],
        [KeyboardButton("Система налогообложения")],
        [KeyboardButton("Пошаговая инструкция"), KeyboardButton("Полезные ссылки")]
    ]

    # Создаем объект клавиатуры
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Я бот-помощник по регистрации бизнеса. "
        f"Чтобы начать, выбери один из пунктов меню.",
        reply_markup=reply_markup  # Добавляем нашу клавиатуру к сообщению
    )


async def choice_form(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отвечает на нажатие кнопки 'Выбор формы (ИП/ООО)'."""
    # Текст-заглушка для этого раздела
    text = (
        "Выбор между ИП и ООО зависит от ваших целей. \n\n"
        "<b>ИП (Индивидуальный предприниматель)</b> — проще зарегистрировать и вести отчетность, "
        "все заработанные деньги — ваши личные. Но вы отвечаете по обязательствам всем своим имуществом. \n\n"
        "<b>ООО (Общество с ограниченной ответственностью)</b> — более сложная регистрация и отчетность. "
        "Вы рискуете только в пределах уставного капитала. Подходит для бизнеса с партнерами."
    )
    # Используем parse_mode='HTML' для поддержки тегов <b>
    await update.message.reply_text(text, parse_mode='HTML')


async def tax_system(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отвечает на нажатие кнопки 'Система налогообложения'."""
    text = "Здесь будет подробная информация о различных системах налогообложения (УСН, ОСНО, Патент и т.д.)."
    await update.message.reply_text(text)


async def instructions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отвечает на нажатие кнопки 'Пошаговая инструкция'."""
    text = "Здесь будет пошаговая инструкция по регистрации бизнеса: сбор документов, подача заявления, открытие счета."
    await update.message.reply_text(text)


async def useful_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отвечает на нажатие кнопки 'Полезные ссылки'."""
    text = "Здесь будут полезные ссылки: сайт ФНС, портал Госуслуг, конструкторы документов."
    await update.message.reply_text(text)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Завершает диалог и убирает клавиатуру."""
    await update.message.reply_text(
        "Рад был помочь! Если снова понадобится информация, просто отправьте /start.",
        # Передаем инструкцию для удаления клавиатуры
        reply_markup=ReplyKeyboardRemove()
    )


# --- Основная часть ---

def main() -> None:
    """Основная функция, которая запускает и останавливает бота."""
    # Создаем "мозг" нашего бота - объект Application, в который передаем токен
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))

    # Регистрируем обработчики кнопок (текстовых сообщений)
    application.add_handler(MessageHandler(filters.Regex(r"^Выбор формы \(ИП/ООО\)$"), choice_form))
    application.add_handler(MessageHandler(filters.Regex("^Система налогообложения$"), tax_system))
    application.add_handler(MessageHandler(filters.Regex("^Пошаговая инструкция$"), instructions))
    application.add_handler(MessageHandler(filters.Regex("^Полезные ссылки$"), useful_links))

    # Запускаем бота. Он будет работать, пока мы его не остановим (например, нажав Ctrl+C в терминале)
    application.run_polling()


# Эта стандартная конструкция в Python.
# Она проверяет, был ли этот файл запущен напрямую (а не импортирован в другой файл).
# Если да, то вызывается функция main().
if __name__ == "__main__":
    main()
