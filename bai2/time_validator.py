import datetime

def parse_and_inspect_date(date_str):
    try:
        date = datetime.datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )
        return date
    except:
        return False
