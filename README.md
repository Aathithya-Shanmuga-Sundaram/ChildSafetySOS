# ChildSafetySOS

ChildSafetySOS is a Python terminal-based chat application that monitors messages for toxic or harmful content in real-time. It uses a pre-trained BERT model to classify messages and sends SOS alerts via Telegram when risky messages are detected. Ideal for monitoring child chats or sensitive communications.

## Features

* **Toxicity detection**: Detects messages that are toxic, obscene, threatening, or sexually explicit.
* **Real-time Telegram alerts**: Sends SOS notifications to a parent/admin chat when flagged messages occur.
* **Terminal-based chat**: Simple and easy-to-use interface for sending and receiving messages.
* **Predefined bot responses**: Automatically responds with safe predefined replies.
* **Customizable thresholds**: Adjust sensitivity for flagged messages (default: score ≥ 0.8).

## Requirements

* Python 3.9+
* `transformers` library
* `requests` library

Install dependencies with:

```bash
pip install transformers requests
```

## Setup

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/ChildSafetySOS.git
cd ChildSafetySOS
```

2. **Configure your Telegram Bot**:

   * Create a Telegram bot via [BotFather](https://t.me/BotFather) and get the **Bot Token**.
   * Find your **chat ID** (parent/admin chat) by sending a message to your bot and checking updates:

   ```bash
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```

3. **Include BOT\_TOKEN and PARENT\_TOKEN** in `app.py`:

```python
Bot_token = "YOUR_BOT_TOKEN"          # Replace with your Telegram bot token
Parent_token = "YOUR_PARENT_CHAT_ID"  # Replace with the parent/admin chat ID
```

### ⚠️ Optional: Use `.env` for Safer Storage

1. Create a `.env` file in the project root:

```
BOT_TOKEN=your_bot_token_here
PARENT_TOKEN=your_parent_chat_id_here
```

2. Install `python-dotenv`:

```bash
pip install python-dotenv
```

3. **Run the chat application**:

```bash
python app.py
```

4. **Start chatting** in the terminal.

   * Toxic messages (score ≥ 0.8) trigger **SOS alerts** via Telegram.
   * Predefined bot replies are displayed automatically.

## Example

```
Child: I hate everyone
Friend: Stay calm and think before sending messages!
```

* Toxic message triggers Telegram alert:

```
SOS ALERT 🚨
From: Child
Message: I hate everyone
Type: toxic
Risk: 0.92
```

## Contributing

Feel free to fork, open issues, and submit pull requests.
Enhancements like GUI/web integration or advanced alerting are welcome.
