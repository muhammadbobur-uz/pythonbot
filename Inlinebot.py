from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardMarkup,MessageEntity
from telegram import Update,KeyboardButton,ParseMode, InlineQueryResultArticle,InputTextMessageContent,InlineQueryResultPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext,InlineQueryHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.utils.helpers import escape_markdown
from uuid import uuid4


STATE_INLINE = 0
STATE_SEND = 1

btn = [[InlineKeyboardButton("🔎 Qidirish", switch_inline_query_current_chat='')]]


def start(update: Update, context: CallbackContext):
    first_name = update.effective_user.first_name
    update.message.reply_html(f"<b>Ассалому алайкум !</b>\n\n"
                              f"🟢 Ушбу бот орқали инлине қидиришингиз мумкин \n"
                              f"Унинг учун қидириш тугмасини босинг."
                              ,reply_markup=InlineKeyboardMarkup(btn))
    context.chat_data.update({
        'first_name': first_name
    })
    return STATE_INLINE

def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query
    print(query, uuid4())
    if query == "":
        return
    # query = update.inline_query
    # text = query.query
    # print(text)
    # query.from_user.send_message(text)

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Семена кукурузы сахарной ГЕНЕРАТОР",
            input_message_content=InputTextMessageContent(f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>", parse_mode="HTML"),
            url = "https://agrozamin.uz/uz/product/96",
            hide_url = True,
            description = "'Muhammadbobur Bobo' YaTT\n\nЦена: 3 500 UZS \nsoni: 3000\nToifa: Urug'lar\nPastki toifa: Donli urug'lar",
            thumb_url = 'https://agrozamin.uz/upload_files/product_photo/15616439ac45ff9.jpg',
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="КОСТЮМ СПЕЦ",
            input_message_content=InputTextMessageContent(
                f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>",
                parse_mode="HTML"),
            url="https://agrozamin.uz/uz/product/198",
            hide_url=True,
            description="Цена: 35 000 UZS \nsoni: 150 dona \nToifa: O'g'itlar\nPastki toifa: Bio o'g'itlar ",
            thumb_url='https://agrozamin.uz/upload_files/product_photo/1561644cd0c47ce.jpeg',
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Кормоуборочный комбайн RSM F 2650",
            input_message_content=InputTextMessageContent(
                f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>",
                parse_mode="HTML"),
            url="https://agrozamin.uz/uz/product/122",
            hide_url=True,
            description="Цена: 21 940 560 UZS \nsoni: 100 dona\nToifa: Qishloq xo'jaligi uskunalari\nPastki toifa: Chorvachilik uchun uskunalar",
            thumb_url='https://agrozamin.uz/upload_files/product_photo/1961643c9f762d6.jpeg',
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Айсидивит 100мл",
            input_message_content=InputTextMessageContent(
                f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>",
                parse_mode="HTML"),
            url="https://agrozamin.uz/uz/product/279",
            hide_url=True,
            description="Цена: 4 500 UZS \nsoni: 2000 dona \nToifa: Veterinariya\nPastki toifa: Immunostimulyatorlar",
            thumb_url='https://agrozamin.uz/upload_files/product_photo/156167d9f72083c.jpg',
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Помидор",
            input_message_content=InputTextMessageContent(
                f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>",
                parse_mode="HTML"),
            url="https://agrozamin.uz/uz/product/280",
            hide_url=True,
            description="Цена: 10 000 UZS \nsoni: 15 t\nToifa: Tayyor mahsulot\nPastki toifa: Sabzavotlar",
            thumb_url='https://agrozamin.uz/upload_files/product_photo/146166e4c55e15d.jpg',
        ),
    InlineQueryResultArticle(
            id=str(uuid4()),
            title="Помидор",
            input_message_content=InputTextMessageContent(
                f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>",
                parse_mode="HTML"),
            url="https://agrozamin.uz/uz/product/280",
            hide_url=True,
            description="Цена: 11 500 UZS \nsoni: 20 t\nToifa: Tayyor mahsulot\nPastki toifa: Sabzavotlar",
            thumb_url='https://agrozamin.uz/upload_files/news/616d643165aa9.jpg',
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Фелуцен брикет К1-2 энергетический для крупного рогатого скота",
            input_message_content=InputTextMessageContent(
                f"Yirtqich tigr sindiraman degan rasm\nsaytimiz: <a href='https://agrozamin.uz/uz/cart/index'>AgroZamin</a>",
                parse_mode="HTML"),
            url="https://agrozamin.uz/uz/product/228",
            hide_url=True,
            description="Цена: 1 000 UZS \nsoni: 1000 dona\nToifa: Ozuqa\nPastki toifa: Yem qo'shimchalari",
            thumb_url='https://agrozamin.uz/upload_files/product_photo/16616534298547d.jpg',
        ),
    ]
    update.inline_query.answer(results)
    print(query)


def send_card(update:Update,context:CallbackContext):
    t = update.message.text
    update.message.reply_html(f'{t}')

conv_handler = ConversationHandler(
    entry_points = [
        MessageHandler(Filters.all, start)
    ],
    states = {
        STATE_INLINE: [
            InlineQueryHandler(inline_query)
       ],
        STATE_SEND: [
            MessageHandler(Filters.all, send_card)
        ],
    },
    fallbacks= []
)

updater = Updater('5062910933:AAF5u_AZ419ftxh2-zyAGk_Ihc-Pc13fe5E', use_context = True)
updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(InlineQueryHandler(inline_query))

updater.start_polling()
updater.idle()