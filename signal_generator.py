import random
from utils import get_current_time_utc6

def generate_signal():
    markets = ['EURUSD-OTC', 'GBPUSD-OTC', 'USDJPY-OTC', 'AUDUSD-OTC']
    selected_market = random.choice(markets)
    direction = random.choice(['CALL', 'PUT'])

    indicators_agree = random.random() < 0.25  # 25% chance indicators agree

    if not indicators_agree:
        return None

    time_now = get_current_time_utc6()
    signal = {
        'pair': selected_market,
        'time': time_now.strftime('%H:%M'),
        'direction': direction,
        'result': random.choice(['win', 'martingale_win', 'loss'])
    }
    return signal
