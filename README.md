# 🤖 Crypto Issue Reporter — Telegram Bot

A Telegram bot that guides crypto users through reporting issues using inline buttons (no typing required), then provides tailored advice and action options.

---

## ✨ Flow Overview

```
/start
  └─▶ Choose Category (button)
        └─▶ Choose Specific Issue (button)
              └─▶ Confirm Report (button)
                    └─▶ What to do next (advice)
                          ├─▶ 🔧 Rectify My Issue  → Step-by-step fix guide
                          └─▶ 🧑‍💼 Contact Support  → Opens your support link
```

---

## 🚀 Deploy on Railway (Recommended)

### 1. Create your Telegram bot
- Message [@BotFather](https://t.me/BotFather) → `/newbot` → copy your token

### 2. Push to GitHub
```bash
git init
git add .
git commit -m "Initial bot"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 3. Deploy on Railway
1. Go to https://railway.app and sign in
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your repository
4. Go to **Variables** tab and add:
   - `TELEGRAM_BOT_TOKEN` = your bot token
   - `SUPPORT_LINK` = your Telegram support group/admin link (e.g. `https://t.me/your_username`)
5. Railway auto-detects `railway.toml` and deploys — your bot runs 24/7!

---

## 🗂️ Project Structure

```
crypto_report_bot/
├── bot.py              # Main bot logic & conversation states
├── responses.py        # Sub-options, advice text, rectify steps
├── requirements.txt    # Dependencies
├── Procfile            # Process definition
├── runtime.txt         # Python version
├── railway.toml        # Railway deployment config
├── .env.example        # Environment variable template
└── README.md           # This file
```

---

## 🔧 Customization

### Change support link
Set `SUPPORT_LINK` environment variable on Railway to your Telegram group/admin link.

### Add a new issue sub-type
In `responses.py`:
1. Add to `SUB_OPTIONS["category"]`: `{"key": "my_key", "label": "🔑 My Issue"}`
2. Add to `_ADVICE`: `"my_key": "Explanation text..."`
3. Add to `_RECTIFY`: `"my_key": "1️⃣ Step one\n\n2️⃣ Step two..."`

### Forward reports to a Telegram group
In `bot.py`, inside `save_report()`, add:
```python
await context.bot.send_message(chat_id=YOUR_GROUP_ID, text=f"New report from @{user.username}:\n{sub_label}")
```

---

## ⚠️ Disclaimer
This bot provides general guidance only. For significant financial losses, always consult legal professionals and report to the appropriate authorities.
