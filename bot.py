import requests


def send_msg(text):
    token = "6378712734:AAH0iqRVvi83eeQ0QmWrkmzBHAD862HDE3M"
    chat_id = "1383629352"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)