from datetime import datetime
def date_formater(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    formated_date = date.strftime("%d/%m/%Y")
    return formated_date