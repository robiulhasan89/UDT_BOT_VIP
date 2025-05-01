from datetime import datetime, timedelta

def get_current_time_utc6():
    utc_now = datetime.utcnow()
    return utc_now + timedelta(hours=6)
