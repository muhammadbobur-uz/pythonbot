from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardMarkup,MessageEntity
from telegram import Update,KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
import mysql.connector
from backend import analiz

data = analiz()

b1, b2, b3 = ("πΊπΏ ΠΠ·Π±Π΅ΠΊΡΠ°","π·πΊ Π ΡΡΠΊΠΈΠΉ","πΊπΏ O\'zbekcha")
def b_button():
    return ReplyKeyboardMarkup([[b1], [b2], [b3]], resize_keyboard=True, one_time_keyboard=True)

t1,t2 = ("π± Raqam yuborish", "πΊπΏ Tilni o'zagrtirish π·πΊ")
def t_button():
    return ReplyKeyboardMarkup([[KeyboardButton(t1, request_contact=True)],
                                [t2]], resize_keyboard=True, one_time_keyboard=True)

bck = [[InlineKeyboardButton("π Orqaga", callback_data='back')]]

faq1, faq2, faq3, faq4, faq5 = ("Saytdagi xatolik","Texnik savol", "Taklif", "Boshqa turdagi savol", "π Orqaga")
faq = [[InlineKeyboardButton(faq1, callback_data='sayt_xato')],[InlineKeyboardButton(faq2, callback_data='tex_sav')],
                                [InlineKeyboardButton(faq3, callback_data='tak')],[InlineKeyboardButton(faq4, callback_data='boshqa')],
                                [InlineKeyboardButton(faq5, callback_data='back')]]

k1, k2, k3, k4, k5 = ("β Maxsulot qo'shish","ππ»ββοΈ Shaxsiy kabinet","π¬ E'lonlar","π² Biz bilan bog'lanish", "πΊπΏ Tilni o'zagrtirish π·πΊ")
def k_button():
    return ReplyKeyboardMarkup([[k1,k2],[k3,k4],[k5]], resize_keyboard=True, one_time_keyboard=True)

sh1,sh2, sh3, sh4, sh5, sh6, sh7 = ("β Maxsulot qo'shish", "π¬ Mening maxsulotlarim", "π° Balansni to'ldirish", "π Referal Havola", "π§ Sozlamalar", "π Asosiy menu", "π Shaxsiy kabinetdan chiqish")
def sh_button():
    return ReplyKeyboardMarkup([[sh1],[sh2,sh3],[sh4,sh5], [sh6, sh7]], resize_keyboard=True, one_time_keyboard=True)

s1, s2, s3, s4, s5, s6, s7 = ("π± Telefon raqamni tahrirlash","π€ FIO ni o'zgartirish", "π₯ E-mailni o'zgartirish", "π§ Avatarni yangilash", "π Manzilni o'zgartirish", "π Ortga qaytish", "π Asosiy menu")
def s_button():
    return ReplyKeyboardMarkup([[s1],[s2,s3],[s4,s5], [s6, s7]], resize_keyboard=True, one_time_keyboard=True)

STATE_BEGIN = 0
STATE_PHONE = 1
STATE_CHECK = 2
STATE_KOBINET = 3
STATE_BIZ_BILAN = 4
STATE_SHAXSIY_KABINET = 5
STATE_SOZLAMALAR = 6

def start(update: Update, context: CallbackContext):
    data.__init__()
    global name
    name = update.effective_user.first_name
    id = update.effective_user.id
    update.message.reply_html(f'ΠΡΡΠ°Π»ΠΎΠΌΡ Π°Π»Π°ΠΉΠΊΡΠΌ! ΠΠ΅Π»ΠΈΠ½Π³, Π°Π²Π²Π°Π» ΡΠΈΠ·ΠΌΠ°Ρ ΠΊΡΡΡΠ°ΡΠΈΡ ΡΠΈΠ»ΠΈΠ½ΠΈ ΡΠ°Π½Π»Π°Π± ΠΎΠ»Π°ΠΉΠ»ΠΈΠΊ.'
                              f'\n\nAssalomu alaykum ! Keling, avval xizmat ko\'rsatish tilini tanlab olaylik.'
                              f'\n\nΠΠ΄ΡΠ°ΡΡΠ²ΡΠΉΡΠ΅! ΠΠ°Π²Π°ΠΉΡΠ΅ Π΄Π»Ρ Π½Π°ΡΠ°Π»Π° Π²ΡΠ±Π΅ΡΠ°Π΅ΠΌ ΡΠ·ΡΠΊ ΠΎΠ±ΡΠ»ΡΠΆΠΈΠ²Π°Π½ΠΈΠΈΡ.  ',
                              reply_markup=b_button())
    context.chat_data.update({
        'id': id,
        'name': name
    })
    return STATE_BEGIN

def f_b(update: Update, context: CallbackContext):
    data.__init__()
    b_name = update.message.text
    if b_name == b1:
        update.message.reply_html(f'Π’Π΅Π»Π΅ΡΠΎΠ½ ΡΠ°?Π°ΠΌΠΈΠ½Π³ΠΈΠ·Π½ΠΈ +9989** *** ** **\nΡΠ°ΠΊΠ»Π΄Π° ΡΠ±ΠΎΡΠΈΠ½Π³, '
                                  f'ΡΠΊΠΈ "π± Π Π°?Π°ΠΌ ΡΠ±ΠΎΡΠΈΡ"\nΡΡΠ³ΠΌΠ°ΡΠΈΠ½ΠΈ Π±ΠΎΡΠΈΠ½Π³:',
                                  reply_markup=t_button())
    elif b_name == b2:
        update.message.reply_html(f'Π’Π΅Π»Π΅ΡΠΎΠ½ ΡΠ°?Π°ΠΌΠΈΠ½Π³ΠΈΠ·Π½ΠΈ +9989** *** ** **\nΡΠ°ΠΊΠ»Π΄Π° ΡΠ±ΠΎΡΠΈΠ½Π³, '
                                  f'ΡΠΊΠΈ "π± Π Π°?Π°ΠΌ ΡΠ±ΠΎΡΠΈΡ"\nΡΡΠ³ΠΌΠ°ΡΠΈΠ½ΠΈ Π±ΠΎΡΠΈΠ½Π³:',
                                  reply_markup=t_button())
    elif b_name == b3:
        update.message.reply_html(f'Telefon raqamingizni +9989** *** ** **\nshaklda yuboring, '
                                  f'yoki "π± Raqam yuborish"\ntugmasini bosing: ',
                                  reply_markup=t_button())

    return STATE_PHONE

def f_back(update:Update, context: CallbackContext):
    data.__init__()
    update.message.reply_html("<b>Π’ΠΈΠ»Π½ΠΈ ΡΠ°Π½Π»Π°Π½Π³..\n\nΠΡΠ±Π΅ΡΠΈΡΠ΅ ΡΠ·ΡΠΊ..\n\nTilni tanlang..</b>", reply_markup=b_button())
    return STATE_BEGIN

def f_sms(update:Update, context: CallbackContext):
    data.__init__()
    query = update.callback_query
    query.message.reply_html("<b>β»οΈQaytadan ...</b>", reply_markup=t_button())
    return STATE_PHONE

def phone_entity_handler(update: Update, context: CallbackContext):
    data.__init__()
    pne = list(filter(lambda e: e.type == 'phone_number', update.message.entities))[0]
    phone_number = update.message.text[pne.offset : pne.offset + pne.length]
    print(update.message.text, update.message.entities[0], phone_number)
    #update.message.reply_html(f"Hurmatli mijoz Operatorlarimiz sizning <b>{phone_number}</b> nomeringizga qo\'ng\'iroq qilishadi so'rovnomada qatnashganingiz uchun raxmat.")
    context.chat_data.update({
        'phone_number': phone_number
    })
    if phone_number:
        data.mb_select(number=f'{phone_number}')
        if data.b:
            update.message.reply_html("<b>π Juda soz ! \nHurmatli mijoz siz bizning bazada bor ekansiz β \nAgroZamin botiga xush kelibsiz. π€ </b>", reply_markup = k_button())
            return STATE_KOBINET
        else:
            update.message.reply_html(f"<b>Sizning raqamingiz <b>{phone_number}</b> ga yuborilgan kodni kiriting: "
                                      f" \n\n\nsaytimiz: πππ\nhttps://dev.agrozamin.uz/</b>", reply_markup=InlineKeyboardMarkup(bck))
            data.send_sms(num=context.chat_data['phone_number'][1:], kod=context.chat_data['id'])
            data.send_sms(num=context.chat_data['phone_number'], kod=context.chat_data['id'])
            return STATE_CHECK
    print(context.chat_data)

def phone_contact_handler(update: Update, context: CallbackContext):
    data.__init__()
    phone_number = update.message.contact
    context.chat_data.update({
        'phone_number': phone_number['phone_number']
    })
    #update.message.reply_html(f"Hurmatli mijoz Operatorlarimiz sizning <b>{phone_number['phone_number']}</b> nomeringizga telefon qilishadi so\'rovnomada qatnashganingiz uchun raxmat.")
    if phone_number:
        data.mb_select(number=f"{phone_number['phone_number']}")
        if data.b:
            update.message.reply_html("<b>π Juda soz ! \nHurmatli mijoz siz bizning bazada bor ekansiz β \nAgroZamin botiga xush kelibsiz. π€ </b>",
                                      reply_markup = k_button())
            return STATE_KOBINET
        else:
            update.message.reply_html(f"Sizning raqamingiz <b>{phone_number['phone_number']}</b> ga yuborilgan kodni kiriting: ", reply_markup=InlineKeyboardMarkup(bck))
            data.send_sms(num = context.chat_data['phone_number'][1:], kod = context.chat_data['id'])
            data.send_sms(num=context.chat_data['phone_number'], kod=context.chat_data['id'])
            return STATE_CHECK


def phone_resent_handler(update: Update, context: CallbackContext):
    data.__init__()
    update.message.reply_html(f'<b>{name}</b> edi siz bilan mutaxassislarimiz bog\'lanishi uchun telefon nomeringizni '
                              f'kiriting: ')

def check_sms(update:Update, context: CallbackContext):
    data.__init__()
    if int(update.message.text) == int(context.chat_data['id']):
        update.message.reply_html("βββ AgroZamin botiga xush kelibsiz", reply_markup = k_button())
        data.mb_insert(d1=context.chat_data['id'], d2=f"{context.chat_data['name']}", d3=f"{context.chat_data['phone_number']}")
        return STATE_KOBINET
    else:
        update.message.reply_html(f"<b>{update.message.text}</b> β Kod kiritishda xatolik β\nTekshirib qaytadan kiriting:\n\n\n<b>Ma\'lumot uchun saytimiz: πππ\nhttps://dev.agrozamin.uz/</b>")

def mbdelete(update:Update,context:CallbackContext):
    data.__init__()
    data.mb_delete()

def f_kabinet(update:Update, context:CallbackContext):
    data.__init__()
    k_name = update.message.text
    if k_name == k1:
        update.message.reply_html(f"{k1} tanlandi")
    if k_name == k2:
        update.message.reply_html(f"{k2} tanlandi", reply_markup = sh_button())
        return STATE_SHAXSIY_KABINET
    if k_name == k3:
        update.message.reply_html(f"{k3} tanlandi")
    if k_name == k4:
        update.message.reply_html("<b>Biz bilan bog'lanish uchun kontaktlar :\n\nπ² +998 90 996 83 95 \nπ +998 71 232 88 88 \nβ +998 71 265 80 60"
                                  "\n\nMa'lumot uchun saytimiz:\nπ https://dev.agrozamin.uz/"
                                  "\n\nπ Bizga xabar qoldirmoqchi bo'lsangiz? Quyidagilardan birini tanlangππ» :</b>",  reply_markup=InlineKeyboardMarkup(faq))
        return STATE_BIZ_BILAN
    if k_name == k5:
        update.message.reply_html(f"{k5} tanlandi")

def f_biz_bilan(update:Update, context:CallbackContext):
    data.__init__()
    query = update.callback_query
    if query.data == 'sayt_xato':
        query.message.reply_html(f'<b>{faq1}</b> tanlandi')
    if query.data == 'tex_sav':
        query.message.reply_html(f'<b>{faq2}</b> tanlandi')
    if query.data == 'tak':
        query.message.reply_html(f'<b>{faq3}</b> tanlandi')
    if query.data == 'boshqa':
        query.message.reply_html(f'<b>{faq4}</b> tanlandi')
    if query.data == 'back':
        query.message.reply_html(f'<b>{faq5}</b> tanlandi', reply_markup = k_button())
        return STATE_KOBINET

def f_sh_kabinet(update:Update,context:CallbackContext):
    data.__init__()
    sh_kabinet = update.message.text
    if sh_kabinet == sh5:
        update.message.reply_html(f"{sh5} tanlandi", reply_markup = s_button())
        return STATE_SOZLAMALAR
    if sh_kabinet == sh6:
        update.message.reply_html(f"{sh6} tanlandi", reply_markup = k_button())
        return STATE_KOBINET

def f_sozlamalar(update:Update,context:CallbackContext):
    data.__init__()
    s_soz = update.message.text
    if s_soz == s6:
        update.message.reply_html(f"{s6} tanlandi", reply_markup = sh_button())
        return STATE_SHAXSIY_KABINET


updater = Updater('TOKEN', use_context=True)

conv_handler = ConversationHandler(
    entry_points = [
        CommandHandler('start', start),
        #CommandHandler('delete', mbdelete)
        ],
    states = {
        STATE_BEGIN: [
            MessageHandler(Filters.text, f_b),
            MessageHandler(Filters.all, start)
        ],
        STATE_PHONE: [
            MessageHandler(Filters.regex('^('+t2+')$'), f_back),
            MessageHandler(Filters.text & Filters.entity(MessageEntity.PHONE_NUMBER), phone_entity_handler),
            MessageHandler(Filters.contact, phone_contact_handler),
            MessageHandler(Filters.all, phone_resent_handler)
        ],
        STATE_CHECK: [
            CallbackQueryHandler(f_sms),
            MessageHandler(Filters.all, check_sms)
        ],
        STATE_KOBINET: [
            MessageHandler(Filters.text, f_kabinet)
        ],
        STATE_BIZ_BILAN: [
            CallbackQueryHandler(f_biz_bilan)
        ],
        STATE_SHAXSIY_KABINET: [
            MessageHandler(Filters.all, f_sh_kabinet)
        ],
        STATE_SOZLAMALAR: [
            MessageHandler(Filters.all, f_sozlamalar)
        ],
    },
    fallbacks= []
)
updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
