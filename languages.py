"""
All UI strings for each supported language.
"""

STRINGS = {
    "pt": {
        "flag": "🇧🇷",
        "name": "Português",
        "welcome": (
            "👋 Olá, *{name}*!\n\n"
            "Bem-vindo ao *{bot_name}*.\n\n"
            "⚠️ _Estou aqui para ajudá-lo com suas perguntas sobre a Carteira._\n\n"
            "Selecione a categoria que melhor descreve o seu problema:"
        ),
        "choose_sub": "Você selecionou: *{category}*\n\nEscolha o problema específico:",
        "type_other": "Você selecionou: *{category}*\n\n📝 Por favor, descreva brevemente o seu problema:",
        "report_summary": "📋 *Resumo do Relatório*\n\n*Categoria:* {category}\n*Problema:* {issue}\n\nConfirme ou altere sua seleção:",
        "report_summary_other": "📋 *Resumo do Relatório*\n\n*Categoria:* ✏️ Outro Problema\n*Descrição:* {issue}\n\nConfirme ou edite:",
        "submitted": "✅ *Relatório Enviado!*\n_Registrado em: {timestamp}_\n\n📋 Todos os relatórios foram registrados e enviados ao nosso administrador para acompanhamento.\n\n━━━━━━━━━━━━━━━━━━━━\n📌 *O que aconteceu e o que isso significa:*\n\n{advice}\n━━━━━━━━━━━━━━━━━━━━\n\nO que você gostaria de fazer agora?",
        "rectify_title": "{steps}",
        "back_to_start": "Selecione a categoria que melhor descreve o seu problema:",
        "cancelled": "❌ Cancelado. Digite /start para iniciar um novo relatório.",
        "restarting": "Claro! Selecione a categoria do novo problema:",
        "help": (
            "ℹ️ *Reportador de Problemas Cripto — Ajuda*\n\n"
            "*Comandos:*\n• /start — Reportar um novo problema\n• /ajuda — Exibir esta mensagem\n• /cancelar — Cancelar relatório\n\n"
            "⚠️ _Nunca pediremos suas chaves privadas ou frase semente._"
        ),
        "btn_confirm": "✅ Enviar Relatório",
        "btn_edit": "🔙 Alterar",
        "btn_cancel": "❌ Cancelar",
        "btn_rectify": "🔧 Tentar Resolver o Problema",
        "btn_support": "🧑‍💼 Falar com o Suporte",
        "btn_support_still": "🧑‍💼 Ainda precisa de ajuda? Falar com Suporte",
        "btn_restart": "🔄 Reportar Outro Problema",
        "btn_back": "🔙 Voltar",
        "categories": {
            "scam":        "🚨 Golpe / Fraude",
            "transaction": "💸 Problema com Transação",
            "wallet":      "👛 Problema na Carteira",
            "exchange":    "🏦 Problema na Exchange",
            "other":       "✏️ Outro Problema",
            "buy_pixel":   "🛒 Comprar Pixel para DePix",
            "depix_lbtc":  "🔄 Trocar DePix por LBTC",
        },
        "sub_options": {
            "scam": [
                {"key": "scam_phishing",      "label": "🎣 Phishing / Site Falso"},
                {"key": "scam_rugpull",       "label": "🪤 Rug Pull / Golpe de Saída"},
                {"key": "scam_romance",       "label": "💔 Golpe Romântico / Pig Butchering"},
                {"key": "scam_impersonation", "label": "🎭 Falso Suporte / Impersonação"},
                {"key": "scam_pump",          "label": "📈 Pump & Dump"},
            ],
            "transaction": [
                {"key": "tx_stuck",         "label": "⏳ Transação Presa / Pendente"},
                {"key": "tx_failed",        "label": "❌ Transação Falhou"},
                {"key": "tx_wrong_address", "label": "📍 Enviado para Endereço Errado"},
                {"key": "tx_missing",       "label": "🔍 Fundos Não Recebidos"},
                {"key": "tx_double",        "label": "🔁 Cobrado em Duplicidade"},
            ],
            "wallet": [
                {"key": "wallet_locked", "label": "🔒 Bloqueada / Sem Acesso"},
                {"key": "wallet_hacked", "label": "🛑 Carteira Hackeada / Comprometida"},
                {"key": "wallet_sync",   "label": "🔄 Problema de Sincronização"},
                {"key": "wallet_seed",   "label": "📄 Perdi a Frase Semente"},
                {"key": "wallet_hw",     "label": "🔌 Problema na Carteira Hardware"},
            ],
            "exchange": [
                {"key": "ex_withdrawal", "label": "💰 Saque Bloqueado / Atrasado"},
                {"key": "ex_frozen",     "label": "🧊 Conta Congelada / Suspensa"},
                {"key": "ex_kyc",        "label": "📋 Problema de KYC / Verificação"},
                {"key": "ex_funds",      "label": "💸 Fundos Faltando na Exchange"},
                {"key": "ex_login",      "label": "🔑 Não Consigo Fazer Login"},
                {"key": "ex_buy_pixel",  "label": "🛒 Comprar Pixel para DePix"},
                {"key": "ex_depix_lbtc", "label": "🔄 Trocar DePix por LBTC"},
            ],
            "buy_pixel": [
                {"key": "buy_pixel_issue",  "label": "❓ Problema com minha compra"},
                {"key": "buy_pixel_pending","label": "⏳ Pagamento pendente / não confirmado"},
                {"key": "buy_pixel_wrong",  "label": "📍 Valor errado recebido"},
            ],
            "depix_lbtc": [
                {"key": "depix_lbtc_issue",  "label": "❓ Problema com minha troca"},
                {"key": "depix_lbtc_rate",   "label": "📉 Taxa ruim / valor inesperado"},
                {"key": "depix_lbtc_stuck",  "label": "⏳ Troca parada / pendente"},
            ],
        },
    },

    "en": {
        "flag": "🇬🇧",
        "name": "English",
        "welcome": (
            "👋 Hello, *{name}*!\n\n"
            "Welcome to *{bot_name}*.\n\n"
            "⚠️ I'm here to help you with your questions about Wallet.\n\n"
            "Please select the category that best describes your problem:"
        ),
        "choose_sub": "You selected: *{category}*\n\nChoose the specific issue you're experiencing:",
        "type_other": "You selected: *{category}*\n\n📝 Please briefly describe your issue:",
        "report_summary": "📋 *Report Summary*\n\n*Category:* {category}\n*Issue:* {issue}\n\nPlease confirm or change your selection:",
        "report_summary_other": "📋 *Report Summary*\n\n*Category:* ✏️ Other Issue\n*Description:* {issue}\n\nConfirm or edit:",
        "submitted": "✅ *Report Submitted!*\n_Logged at: {timestamp}_\n\n📋 All reports have been logged and sent to our admin for follow up.\n\n━━━━━━━━━━━━━━━━━━━━\n📌 *What happened and what it means:*\n\n{advice}\n━━━━━━━━━━━━━━━━━━━━\n\nWhat would you like to do next?",
        "rectify_title": "{steps}",
        "back_to_start": "Please select the category that best describes your problem:",
        "cancelled": "❌ Cancelled. Type /start to begin a new report.",
        "restarting": "Sure! Select the category for your new issue:",
        "help": (
            "ℹ️ *{bot_name} — Help*\n\n"
            "*Commands:*\n• /start — Report a new issue\n• /help — Show this message\n• /cancel — Cancel report\n\n"
            "⚠️ _We will NEVER ask for your private keys or seed phrase._"
        ),
        "btn_confirm": "✅ Submit Report",
        "btn_edit": "🔙 Change",
        "btn_cancel": "❌ Cancel",
        "btn_rectify": "🔧 Try to Rectify My Issue",
        "btn_support": "🧑‍💼 Contact Support",
        "btn_support_still": "🧑‍💼 Still need help? Contact Support",
        "btn_restart": "🔄 Report Another Issue",
        "btn_back": "🔙 Back",
        "categories": {
            "scam":        "🚨 Scam / Fraud",
            "transaction": "💸 Transaction Problem",
            "wallet":      "👛 Wallet Issue",
            "exchange":    "🏦 Exchange Problem",
            "other":       "✏️ Other Issue",
            "buy_pixel":   "🛒 Buy Pixel to DePix",
            "depix_lbtc":  "🔄 Exchange DePix to LBTC",
        },
        "sub_options": {
            "scam": [
                {"key": "scam_phishing",      "label": "🎣 Phishing / Fake Website"},
                {"key": "scam_rugpull",       "label": "🪤 Rug Pull / Exit Scam"},
                {"key": "scam_romance",       "label": "💔 Romance / Pig Butchering Scam"},
                {"key": "scam_impersonation", "label": "🎭 Fake Support / Impersonation"},
                {"key": "scam_pump",          "label": "📈 Pump & Dump Scheme"},
            ],
            "transaction": [
                {"key": "tx_stuck",         "label": "⏳ Transaction Stuck / Pending"},
                {"key": "tx_failed",        "label": "❌ Transaction Failed"},
                {"key": "tx_wrong_address", "label": "📍 Sent to Wrong Address"},
                {"key": "tx_missing",       "label": "🔍 Funds Not Received"},
                {"key": "tx_double",        "label": "🔁 Double Charged / Duplicate TX"},
            ],
            "wallet": [
                {"key": "wallet_locked", "label": "🔒 Locked / Lost Access"},
                {"key": "wallet_hacked", "label": "🛑 Wallet Hacked / Compromised"},
                {"key": "wallet_sync",   "label": "🔄 Sync / Balance Not Showing"},
                {"key": "wallet_seed",   "label": "📄 Lost Seed Phrase"},
                {"key": "wallet_hw",     "label": "🔌 Hardware Wallet Issue"},
            ],
            "exchange": [
                {"key": "ex_withdrawal", "label": "💰 Withdrawal Blocked / Delayed"},
                {"key": "ex_frozen",     "label": "🧊 Account Frozen / Suspended"},
                {"key": "ex_kyc",        "label": "📋 KYC / Verification Problem"},
                {"key": "ex_funds",      "label": "💸 Missing Funds on Exchange"},
                {"key": "ex_login",      "label": "🔑 Cannot Log In"},
                {"key": "ex_buy_pixel",  "label": "🛒 Buy Pixel to DePix"},
                {"key": "ex_depix_lbtc", "label": "🔄 Exchange DePix to LBTC"},
            ],
            "buy_pixel": [
                {"key": "buy_pixel_issue",  "label": "❓ Problem with my purchase"},
                {"key": "buy_pixel_pending","label": "⏳ Payment pending / not confirmed"},
                {"key": "buy_pixel_wrong",  "label": "📍 Wrong amount received"},
            ],
            "depix_lbtc": [
                {"key": "depix_lbtc_issue",  "label": "❓ Problem with my exchange"},
                {"key": "depix_lbtc_rate",   "label": "📉 Bad rate / unexpected amount"},
                {"key": "depix_lbtc_stuck",  "label": "⏳ Exchange stuck / pending"},
            ],
        },
    },

    "es": {
        "flag": "🇪🇸",
        "name": "Español",
        "welcome": (
            "👋 ¡Hola, *{name}*!\n\n"
            "Bienvenido a *{bot_name}*.\n\n"
            "⚠️ _Estoy aquí para ayudarte con tus preguntas sobre la Billetera._\n\n"
            "Por favor, selecciona la categoría que mejor describe tu problema:"
        ),
        "choose_sub": "Seleccionaste: *{category}*\n\nElige el problema específico que estás experimentando:",
        "type_other": "Seleccionaste: *{category}*\n\n📝 Por favor, describe brevemente tu problema:",
        "report_summary": "📋 *Resumen del Reporte*\n\n*Categoría:* {category}\n*Problema:* {issue}\n\nConfirma o cambia tu selección:",
        "report_summary_other": "📋 *Resumen del Reporte*\n\n*Categoría:* ✏️ Otro Problema\n*Descripción:* {issue}\n\nConfirma o edita:",
        "submitted": "✅ *¡Reporte Enviado!*\n_Registrado el: {timestamp}_\n\n📋 Todos los reportes han sido registrados y enviados a nuestro administrador para seguimiento.\n\n━━━━━━━━━━━━━━━━━━━━\n📌 *Qué ocurrió y qué significa:*\n\n{advice}\n━━━━━━━━━━━━━━━━━━━━\n\n¿Qué te gustaría hacer ahora?",
        "rectify_title": "{steps}",
        "back_to_start": "Por favor, selecciona la categoría que mejor describe tu problema:",
        "cancelled": "❌ Cancelado. Escribe /start para iniciar un nuevo reporte.",
        "restarting": "¡Claro! Selecciona la categoría del nuevo problema:",
        "help": (
            "ℹ️ *Reportador de Problemas Cripto — Ayuda*\n\n"
            "*Comandos:*\n• /start — Reportar un nuevo problema\n• /ayuda — Ver este mensaje\n• /cancelar — Cancelar reporte\n\n"
            "⚠️ _Nunca pediremos tus claves privadas ni frase semilla._"
        ),
        "btn_confirm": "✅ Enviar Reporte",
        "btn_edit": "🔙 Cambiar",
        "btn_cancel": "❌ Cancelar",
        "btn_rectify": "🔧 Intentar Resolver el Problema",
        "btn_support": "🧑‍💼 Contactar Soporte",
        "btn_support_still": "🧑‍💼 ¿Aún necesitas ayuda? Contactar Soporte",
        "btn_restart": "🔄 Reportar Otro Problema",
        "btn_back": "🔙 Volver",
        "categories": {
            "scam":        "🚨 Estafa / Fraude",
            "transaction": "💸 Problema con Transacción",
            "wallet":      "👛 Problema con Billetera",
            "exchange":    "🏦 Problema con Exchange",
            "other":       "✏️ Otro Problema",
            "buy_pixel":   "🛒 Comprar Pixel a DePix",
            "depix_lbtc":  "🔄 Intercambiar DePix a LBTC",
        },
        "sub_options": {
            "scam": [
                {"key": "scam_phishing",      "label": "🎣 Phishing / Sitio Falso"},
                {"key": "scam_rugpull",       "label": "🪤 Rug Pull / Estafa de Salida"},
                {"key": "scam_romance",       "label": "💔 Estafa Romántica / Pig Butchering"},
                {"key": "scam_impersonation", "label": "🎭 Falso Soporte / Suplantación"},
                {"key": "scam_pump",          "label": "📈 Pump & Dump"},
            ],
            "transaction": [
                {"key": "tx_stuck",         "label": "⏳ Transacción Atascada / Pendiente"},
                {"key": "tx_failed",        "label": "❌ Transacción Fallida"},
                {"key": "tx_wrong_address", "label": "📍 Enviado a Dirección Incorrecta"},
                {"key": "tx_missing",       "label": "🔍 Fondos No Recibidos"},
                {"key": "tx_double",        "label": "🔁 Cobro Duplicado"},
            ],
            "wallet": [
                {"key": "wallet_locked", "label": "🔒 Bloqueada / Sin Acceso"},
                {"key": "wallet_hacked", "label": "🛑 Billetera Hackeada / Comprometida"},
                {"key": "wallet_sync",   "label": "🔄 Problema de Sincronización"},
                {"key": "wallet_seed",   "label": "📄 Perdí la Frase Semilla"},
                {"key": "wallet_hw",     "label": "🔌 Billetera Hardware"},
            ],
            "exchange": [
                {"key": "ex_withdrawal", "label": "💰 Retiro Bloqueado / Atrasado"},
                {"key": "ex_frozen",     "label": "🧊 Cuenta Congelada / Suspendida"},
                {"key": "ex_kyc",        "label": "📋 Problema de KYC / Verificación"},
                {"key": "ex_funds",      "label": "💸 Fondos Faltantes en Exchange"},
                {"key": "ex_login",      "label": "🔑 No Puedo Iniciar Sesión"},
                {"key": "ex_buy_pixel",  "label": "🛒 Comprar Pixel a DePix"},
                {"key": "ex_depix_lbtc", "label": "🔄 Intercambiar DePix a LBTC"},
            ],
            "buy_pixel": [
                {"key": "buy_pixel_issue",  "label": "❓ Problema con mi compra"},
                {"key": "buy_pixel_pending","label": "⏳ Pago pendiente / no confirmado"},
                {"key": "buy_pixel_wrong",  "label": "📍 Monto incorrecto recibido"},
            ],
            "depix_lbtc": [
                {"key": "depix_lbtc_issue",  "label": "❓ Problema con mi intercambio"},
                {"key": "depix_lbtc_rate",   "label": "📉 Mala tasa / monto inesperado"},
                {"key": "depix_lbtc_stuck",  "label": "⏳ Intercambio pendiente / atascado"},
            ],
        },
    },

    "fr": {
        "flag": "🇫🇷",
        "name": "Français",
        "welcome": (
            "👋 Bonjour, *{name}*!\n\n"
            "Bienvenue sur *{bot_name}*.\n\n"
            "⚠️ _Je suis là pour vous aider avec vos questions sur le Portefeuille._\n\n"
            "Veuillez sélectionner la catégorie qui décrit le mieux votre problème:"
        ),
        "choose_sub": "Vous avez sélectionné: *{category}*\n\nChoisissez le problème spécifique:",
        "type_other": "Vous avez sélectionné: *{category}*\n\n📝 Veuillez décrire brièvement votre problème:",
        "report_summary": "📋 *Résumé du Rapport*\n\n*Catégorie:* {category}\n*Problème:* {issue}\n\nConfirmez ou modifiez votre sélection:",
        "report_summary_other": "📋 *Résumé du Rapport*\n\n*Catégorie:* ✏️ Autre Problème\n*Description:* {issue}\n\nConfirmez ou modifiez:",
        "submitted": "✅ *Rapport Envoyé!*\n_Enregistré le: {timestamp}_\n\n📋 Tous les rapports ont été enregistrés et envoyés à notre administrateur pour suivi.\n\n━━━━━━━━━━━━━━━━━━━━\n📌 *Ce qui s'est passé et ce que cela signifie:*\n\n{advice}\n━━━━━━━━━━━━━━━━━━━━\n\nQue souhaitez-vous faire maintenant?",
        "rectify_title": "{steps}",
        "back_to_start": "Veuillez sélectionner la catégorie qui décrit le mieux votre problème:",
        "cancelled": "❌ Annulé. Tapez /start pour commencer un nouveau rapport.",
        "restarting": "Bien sûr! Sélectionnez la catégorie du nouveau problème:",
        "help": (
            "ℹ️ *Reporteur de Problèmes Crypto — Aide*\n\n"
            "*Commandes:*\n• /start — Signaler un nouveau problème\n• /aide — Afficher ce message\n• /annuler — Annuler le rapport\n\n"
            "⚠️ _Nous ne demanderons JAMAIS vos clés privées ou phrase de récupération._"
        ),
        "btn_confirm": "✅ Envoyer le Rapport",
        "btn_edit": "🔙 Modifier",
        "btn_cancel": "❌ Annuler",
        "btn_rectify": "🔧 Essayer de Résoudre",
        "btn_support": "🧑‍💼 Contacter le Support",
        "btn_support_still": "🧑‍💼 Besoin d'aide? Contacter le Support",
        "btn_restart": "🔄 Signaler un Autre Problème",
        "btn_back": "🔙 Retour",
        "categories": {
            "scam":        "🚨 Arnaque / Fraude",
            "transaction": "💸 Problème de Transaction",
            "wallet":      "👛 Problème de Portefeuille",
            "exchange":    "🏦 Problème d'Exchange",
            "other":       "✏️ Autre Problème",
            "buy_pixel":   "🛒 Acheter Pixel vers DePix",
            "depix_lbtc":  "🔄 Échanger DePix contre LBTC",
        },
        "sub_options": {
            "scam": [
                {"key": "scam_phishing",      "label": "🎣 Phishing / Faux Site Web"},
                {"key": "scam_rugpull",       "label": "🪤 Rug Pull / Arnaque de Sortie"},
                {"key": "scam_romance",       "label": "💔 Arnaque Romantique / Pig Butchering"},
                {"key": "scam_impersonation", "label": "🎭 Faux Support / Usurpation"},
                {"key": "scam_pump",          "label": "📈 Pump & Dump"},
            ],
            "transaction": [
                {"key": "tx_stuck",         "label": "⏳ Transaction Bloquée / En Attente"},
                {"key": "tx_failed",        "label": "❌ Transaction Échouée"},
                {"key": "tx_wrong_address", "label": "📍 Envoyé à la Mauvaise Adresse"},
                {"key": "tx_missing",       "label": "🔍 Fonds Non Reçus"},
                {"key": "tx_double",        "label": "🔁 Double Facturation"},
            ],
            "wallet": [
                {"key": "wallet_locked", "label": "🔒 Verrouillé / Accès Perdu"},
                {"key": "wallet_hacked", "label": "🛑 Portefeuille Piraté / Compromis"},
                {"key": "wallet_sync",   "label": "🔄 Problème de Synchronisation"},
                {"key": "wallet_seed",   "label": "📄 Phrase de Récupération Perdue"},
                {"key": "wallet_hw",     "label": "🔌 Portefeuille Matériel"},
            ],
            "exchange": [
                {"key": "ex_withdrawal", "label": "💰 Retrait Bloqué / Retardé"},
                {"key": "ex_frozen",     "label": "🧊 Compte Gelé / Suspendu"},
                {"key": "ex_kyc",        "label": "📋 Problème de KYC / Vérification"},
                {"key": "ex_funds",      "label": "💸 Fonds Manquants sur l'Exchange"},
                {"key": "ex_login",      "label": "🔑 Impossible de Se Connecter"},
                {"key": "ex_buy_pixel",  "label": "🛒 Acheter Pixel vers DePix"},
                {"key": "ex_depix_lbtc", "label": "🔄 Échanger DePix contre LBTC"},
            ],
            "buy_pixel": [
                {"key": "buy_pixel_issue",  "label": "❓ Problème avec mon achat"},
                {"key": "buy_pixel_pending","label": "⏳ Paiement en attente / non confirmé"},
                {"key": "buy_pixel_wrong",  "label": "📍 Montant incorrect reçu"},
            ],
            "depix_lbtc": [
                {"key": "depix_lbtc_issue",  "label": "❓ Problème avec mon échange"},
                {"key": "depix_lbtc_rate",   "label": "📉 Mauvais taux / montant inattendu"},
                {"key": "depix_lbtc_stuck",  "label": "⏳ Échange bloqué / en attente"},
            ],
        },
    },
}


def get_strings(lang: str) -> dict:
    return STRINGS.get(lang, STRINGS["en"])
