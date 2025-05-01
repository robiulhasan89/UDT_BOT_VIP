import requests

BOT_TOKEN = '7898377652:AAFjQectG_42F1LRKRosFPfeRNDv-rmNv8c'
CHANNEL_ID = '@UDT_LOSS_RECOVERY_VIP'

def send_signal(signal):
    message = f"""─── UDT LOSS RECOVERY ───

PAIR: {signal['pair']}
TIME: {signal['time']}
DIRECTION: {signal['direction']}"""
    send_telegram_message(message)

def send_result(signal, result):
    if result == 'win':
        result_text = "✅ WIN"
    elif result == 'martingale_win':
        result_text = "✅ WIN (M1)"
    else:
        result_text = "❌ LOSS"

    message = f"""─── UDT LOSS RECOVERY ───

PAIR: {signal['pair']}
TIME: {signal['time']}
DIRECTION: {signal['direction']}
RESULT: {result_text}"""

    send_telegram_message(message)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL_ID, "text": message}
    requests.post(url, data=data)
