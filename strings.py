"""
All UI strings for the bot, organized by language code.
Supported: pt, en, es, fr
"""

STRINGS = {
    "pt": {
        "lang_name": "🇧🇷 Português",
        "welcome": (
            "👋 Olá, *{name}*!\n\n"
            "Bem-vindo ao *{bot_name}*.\n\n"
            "⚠️ _Estou aqui para ajudá-lo com suas perguntas sobre a Carteira.\n\n"
            "Por favor, selecione a categoria que melhor descreve o seu problema:"
        ),
        "choose_category": "Por favor, selecione a categoria que melhor descreve o seu problema:",
        "you_selected": "Você selecionou: *{label}*\n\nEscolha o problema específico que está enfrentando:",
        "type_other_prompt": "Você selecionou: *✏️ Outro Problema*\n\n📝 Por favor, descreva brevemente o seu problema:",
        "report_summary": "📋 *Resumo do Relatório*\n\n*Categoria:* {category}\n*Problema:* {sub}\n\nConfirme ou altere sua seleção:",
        "report_confirmed": (
            "✅ *Relatório Enviado!*\n"
            "_Registrado em: {timestamp}_\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *O que aconteceu e o que isso significa:*\n\n"
            "{advice}\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "O que você gostaria de fazer agora?"
        ),
        "rectify_title": "{steps}",
        "cancelled": "❌ Cancelado. Digite /start para iniciar um novo relatório.",
        "restart_prompt": "Por favor, selecione a categoria que melhor descreve o seu problema:",
        "help_text": (
            "ℹ️ *{bot_name} — Ajuda*\n\n"
            "*Comandos:*\n"
            "• /start — Reportar um novo problema\n"
            "• /ajuda — Exibir esta mensagem\n"
            "• /cancelar — Cancelar relatório atual\n\n"
            "⚠️ _Nunca pediremos suas chaves privadas ou frase semente._"
        ),
        "btn_confirm": "✅ Enviar Relatório",
        "btn_edit": "🔙 Alterar",
        "btn_cancel": "❌ Cancelar",
        "btn_rectify": "🔧 Tentar Resolver o Problema",
        "btn_support": "🧑‍💼 Falar com o Suporte",
        "btn_still_support": "🧑‍💼 Ainda precisa de ajuda? Falar com Suporte",
        "btn_restart": "🔄 Reportar Outro Problema",
        "btn_back": "🔙 Voltar",
        "categories": {
            "scam":        "🚨 Golpe / Fraude",
            "transaction": "💸 Problema com Transação",
            "wallet":      "👛 Problema na Carteira",
            "exchange":    "🏦 Problema na Exchange",
            "other":       "✏️ Outro Problema",
        },
        "log_timestamp": "Data/Hora",
        "log_category": "Categoria",
        "log_issue": "Problema",
        "log_name": "Nome",
    },

    "en": {
        "lang_name": "🇬🇧 English",
        "welcome": (
            "👋 Hello, *{name}*!\n\n"
            "Welcome to *{bot_name}*.\n\n"
            "⚠️ _I'm here to help you with your questions about Wallet.\n\n"
            "Please select the category that best describes your problem:"
        ),
        "choose_category": "Please select the category that best describes your problem:",
        "you_selected": "You selected: *{label}*\n\nPlease choose the specific issue you're experiencing:",
        "type_other_prompt": "You selected: *✏️ Other Issue*\n\n📝 Please briefly describe your problem:",
        "report_summary": "📋 *Report Summary*\n\n*Category:* {category}\n*Issue:* {sub}\n\nPlease confirm or change your selection:",
        "report_confirmed": (
            "✅ *Report Submitted!*\n"
            "_Logged at: {timestamp}_\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *What happened and what it means:*\n\n"
            "{advice}\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "What would you like to do next?"
        ),
        "rectify_title": "{steps}",
        "cancelled": "❌ Cancelled. Type /start to begin a new report.",
        "restart_prompt": "Please select the category that best describes your problem:",
        "help_text": (
            "ℹ️ *{bot_name} — Help*\n\n"
            "*Commands:*\n"
            "• /start — Report a new issue\n"
            "• /help — Show this message\n"
            "• /cancel — Cancel current report\n\n"
            "⚠️ _We will NEVER ask for your private keys or seed phrase._"
        ),
        "btn_confirm": "✅ Submit Report",
        "btn_edit": "🔙 Change",
        "btn_cancel": "❌ Cancel",
        "btn_rectify": "🔧 Try to Rectify My Issue",
        "btn_support": "🧑‍💼 Contact Support",
        "btn_still_support": "🧑‍💼 Still need help? Contact Support",
        "btn_restart": "🔄 Report Another Issue",
        "btn_back": "🔙 Back",
        "categories": {
            "scam":        "🚨 Scam / Fraud",
            "transaction": "💸 Transaction Problem",
            "wallet":      "👛 Wallet Issue",
            "exchange":    "🏦 Exchange Problem",
            "other":       "✏️ Other Issue",
        },
        "log_timestamp": "Timestamp",
        "log_category": "Category",
        "log_issue": "Issue",
        "log_name": "Name",
    },

    "es": {
        "lang_name": "🇪🇸 Español",
        "welcome": (
            "👋 ¡Hola, *{name}*!\n\n"
            "Bienvenido a *{bot_name}*.\n\n"
            "⚠️ _Estoy aquí para ayudarte con tus preguntas sobre la Billetera.\n\n"
            "Por favor, selecciona la categoría que mejor describe tu problema:"
        ),
        "choose_category": "Por favor, selecciona la categoría que mejor describe tu problema:",
        "you_selected": "Seleccionaste: *{label}*\n\nElige el problema específico que estás experimentando:",
        "type_other_prompt": "Seleccionaste: *✏️ Otro Problema*\n\n📝 Por favor, describe brevemente tu problema:",
        "report_summary": "📋 *Resumen del Reporte*\n\n*Categoría:* {category}\n*Problema:* {sub}\n\nConfirma o cambia tu selección:",
        "report_confirmed": (
            "✅ *¡Reporte Enviado!*\n"
            "_Registrado a las: {timestamp}_\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *Qué ocurrió y qué significa:*\n\n"
            "{advice}\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "¿Qué te gustaría hacer ahora?"
        ),
        "rectify_title": "{steps}",
        "cancelled": "❌ Cancelado. Escribe /start para iniciar un nuevo reporte.",
        "restart_prompt": "Por favor, selecciona la categoría que mejor describe tu problema:",
        "help_text": (
            "ℹ️ *{bot_name} — Ayuda*\n\n"
            "*Comandos:*\n"
            "• /start — Reportar un nuevo problema\n"
            "• /ayuda — Mostrar este mensaje\n"
            "• /cancelar — Cancelar reporte actual\n\n"
            "⚠️ _Nunca pediremos tus claves privadas o frase semilla._"
        ),
        "btn_confirm": "✅ Enviar Reporte",
        "btn_edit": "🔙 Cambiar",
        "btn_cancel": "❌ Cancelar",
        "btn_rectify": "🔧 Intentar Resolver el Problema",
        "btn_support": "🧑‍💼 Contactar Soporte",
        "btn_still_support": "🧑‍💼 ¿Aún necesitas ayuda? Contactar Soporte",
        "btn_restart": "🔄 Reportar Otro Problema",
        "btn_back": "🔙 Volver",
        "categories": {
            "scam":        "🚨 Estafa / Fraude",
            "transaction": "💸 Problema con Transacción",
            "wallet":      "👛 Problema con Billetera",
            "exchange":    "🏦 Problema con Exchange",
            "other":       "✏️ Otro Problema",
        },
        "log_timestamp": "Fecha/Hora",
        "log_category": "Categoría",
        "log_issue": "Problema",
        "log_name": "Nombre",
    },

    "fr": {
        "lang_name": "🇫🇷 Français",
        "welcome": (
            "👋 Bonjour, *{name}*!\n\n"
            "Bienvenue sur *{bot_name}*.\n\n"
            "⚠️ _Je suis là pour vous aider avec vos questions sur le Portefeuille.\n\n"
            "Veuillez sélectionner la catégorie qui décrit le mieux votre problème :"
        ),
        "choose_category": "Veuillez sélectionner la catégorie qui décrit le mieux votre problème :",
        "you_selected": "Vous avez sélectionné : *{label}*\n\nChoisissez le problème spécifique que vous rencontrez :",
        "type_other_prompt": "Vous avez sélectionné : *✏️ Autre Problème*\n\n📝 Veuillez décrire brièvement votre problème :",
        "report_summary": "📋 *Résumé du Rapport*\n\n*Catégorie :* {category}\n*Problème :* {sub}\n\nConfirmez ou modifiez votre sélection :",
        "report_confirmed": (
            "✅ *Rapport Envoyé !*\n"
            "_Enregistré à : {timestamp}_\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *Ce qui s'est passé et ce que cela signifie :*\n\n"
            "{advice}\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Que souhaitez-vous faire maintenant ?"
        ),
        "rectify_title": "{steps}",
        "cancelled": "❌ Annulé. Tapez /start pour commencer un nouveau rapport.",
        "restart_prompt": "Veuillez sélectionner la catégorie qui décrit le mieux votre problème :",
        "help_text": (
            "ℹ️ *{bot_name} — Aide*\n\n"
            "*Commandes :*\n"
            "• /start — Signaler un nouveau problème\n"
            "• /aide — Afficher ce message\n"
            "• /annuler — Annuler le rapport en cours\n\n"
            "⚠️ _Nous ne demanderons JAMAIS vos clés privées ou votre phrase de récupération._"
        ),
        "btn_confirm": "✅ Envoyer le Rapport",
        "btn_edit": "🔙 Modifier",
        "btn_cancel": "❌ Annuler",
        "btn_rectify": "🔧 Essayer de Résoudre le Problème",
        "btn_support": "🧑‍💼 Contacter le Support",
        "btn_still_support": "🧑‍💼 Besoin d'aide ? Contacter le Support",
        "btn_restart": "🔄 Signaler un Autre Problème",
        "btn_back": "🔙 Retour",
        "categories": {
            "scam":        "🚨 Arnaque / Fraude",
            "transaction": "💸 Problème de Transaction",
            "wallet":      "👛 Problème de Portefeuille",
            "exchange":    "🏦 Problème d'Exchange",
            "other":       "✏️ Autre Problème",
        },
        "log_timestamp": "Horodatage",
        "log_category": "Catégorie",
        "log_issue": "Problème",
        "log_name": "Nom",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    """Get a translated string, falling back to English."""
    s = STRINGS.get(lang, STRINGS["en"]).get(key, STRINGS["en"].get(key, key))
    return s.format(**kwargs) if kwargs else s


def get_category_label(lang: str, cat_key: str) -> str:
    return STRINGS.get(lang, STRINGS["en"])["categories"].get(cat_key, cat_key)
