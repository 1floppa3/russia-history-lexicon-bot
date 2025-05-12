# Lexicon XVIII: A Telegram Bot for Archaic Russian Vocabulary

**Course:** History of Russia, HSE  

---

## 📝 Overview
"Lexicon XVIII" is a Telegram bot designed to help users discover, learn, and quiz themselves on archaic Russian words and expressions from the 18th century. Built with Python and Aiogram 3.20, this project demonstrates:
- Telegram Bot API integration
- Asynchronous scheduling (daily word)
- State management (FSM)
- JSON-based persistence

---

## 🚀 Features
- **/start** — welcome message & auto-registration
- **/word** `**<word>**` — lookup definitions
- **/random** — random word
- **/books** — supported sources
- **/quiz** — multiple-choice test
- **⭐ Add to Favorites** — save for later
- **/favorites** — view saved words
- **/word_of_day 1/0** — toggle daily word at 09:00 Europe/Berlin

---

## 🏗 Architecture
```
project_root/
├─ bot/
│   ├─ services/       # LexiconService, UserDataService
│   ├─ handlers/       # command & callback handlers
│   ├─ keyboards/      # InlineKeyboard builders
│   ├─ middlewares/    # EnsureUserMiddleware
│   └─ utils/          # daily_scheduler
├─ data/
│   ├─ words.json
│   └─ users.json
├─ .env                # BOT_TOKEN, settings
├─ requirements.txt
└─ main.py             # app entrypoint
```

---

## ⚙️ Installation
```
git clone <repo_url>
cd russia-history-lexicon-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# edit BOT_TOKEN in .env
python main.py
```

---

## 📜 License

MIT License