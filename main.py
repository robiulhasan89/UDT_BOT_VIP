import time
from signal_generator import generate_signal
from telegram_bot import send_signal, send_result
from utils import get_current_time_utc6

TRADE_DURATION = 60  # 1 minute trade
WAIT_AFTER_TRADE = 25  # 15–30 seconds

while True:
    now = get_current_time_utc6()
    if 10 <= now.hour < 22:
        signal = generate_signal()
        if signal:
            send_signal(signal)
            time.sleep(TRADE_DURATION)

            # Simulate result
            result = signal['result']  # 'win', 'martingale_win', 'loss'
            send_result(signal, result)
            time.sleep(WAIT_AFTER_TRADE)
        else:
            time.sleep(10)
    else:
        time.sleep(60)
