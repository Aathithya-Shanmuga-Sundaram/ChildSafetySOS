# ChildSafetySOS

ChildSafetySOS is a Python terminal-based chat application that monitors messages for toxic or harmful content in real-time. It uses a pre-trained BERT model to classify messages and sends SOS alerts via Telegram when risky messages are detected. Ideal for monitoring child chats or sensitive communications.

## Features

- **Toxicity detection**: Detects messages that are toxic, obscene, threatening, or sexually explicit.
- **Real-time Telegram alerts**: Sends SOS notifications to a parent/admin chat when flagged messages occur.
- **Terminal-based chat**: Simple and easy-to-use interface for sending and receiving messages.
- **Predefined bot responses**: Automatically responds with safe predefined replies.
- **Customizable thresholds**: Adjust sensitivity for flagged messages (default: score ≥ 0.8).

## Requirements

- Python 3.9+
- `transformers` library
- `requests` library
  
Install dependencies with:

```bash
pip install transformers requests
