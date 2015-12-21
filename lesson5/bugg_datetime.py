
import datetime

def get_midnight_datetime(dt=None):
    if dt is None:
        dt = datetime.datetime.now()
    return datetime.datetime(dt.year, dt.month, dt.day)

if __name__ == "__main__":
    print(get_midnight_datetime())
