import re
import pandas as pd

def preprocess(data):
    # for 12h pattern
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\D{2}\s-\s'
    # for 24h pattern
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\-\s'

    messages = re.split(pattern, data)
    messages = messages[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'date': dates})

    # convert date column to datetime
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p - ')

    users = []
    messages = []

    for message in df['user_message']:
        pattern = '([\w\W]+?):\s'
        split_message = re.split(pattern, message)
        if len(split_message) == 3:
            users.append(split_message[1])
            messages.append(split_message[2])
        else:
            users.append('notification')
            messages.append(split_message[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns = ['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df