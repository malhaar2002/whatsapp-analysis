import pandas as pd

def fetch_no_messages(selected_user, df):
    if selected_user == 'Overall':
        return df.shape[0]
    else:
        return df[df['user'] == selected_user].shape[0]

def fetch_gaali(selected_user, df):
    gaalis = {
        'mdrchd': 0,
        'maadarchod': 0,
        'bhosdike': 0,
        'bhonsdike': 0,
        'bsdke': 0,
        'bsdk': 0,
        'bhenchod': 0,
        'behenchod': 0,
        'chutiya': 0,
        'gaandu': 0
    }
    if selected_user == 'Overall':
        new_df = df
    else:
        new_df = df.query("user == @selected_user")
    for message in new_df['message']:
        for gaali in gaalis:
            if gaali in message.lower():
                gaalis[gaali] += 1
    gaali_df = pd.DataFrame(gaalis.items(), columns=['gaali', 'count'])
    return gaali_df