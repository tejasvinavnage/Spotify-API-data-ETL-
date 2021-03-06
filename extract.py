# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlalchemy 
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = ""
USER_ID = ''
TOKEN = "BQDP1IqmMRnTh5d9JGsAfECBTySH-wyPZDJvLeFNP1G8rI6oCrKbvQyf1fJY7szIWWSfXGip1V8qGxnNmHZr-qS8vLje-PgI1T2hr72y_pGnyJ-WJsdSldVWarLeOKbpnXx5mbkwaYIEswrhRekjFjHoYH1hMsRVli2qxQQe"

if __name__ == "__main__":
    
    headers = {
            "Acccept" : "application/json",
            "Content-type" : "application/json",
            "Authorization" : "Bearer {token}".format(token = TOKEN)
            }
    
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp) , headers = headers)
    
    data = r.json()
    print(json.dumps(data, indent=4, sort_keys=True))
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    song_name = []
    artist_name = []
    played_at_list = []
    timestamps = []
    
    for song in data['items']:
        song_name.append(song['track']['name'])
        artist_name.append(song['track']['album']['artists'][0]['name'])
        played_at_list.append(song['played_at'])
        timestamps.append(song['played_at'][0:10])
    
    song_dict = {
            "song_name" : song_name,
            "artist_name" : artist_name,
            "played_at_list" : played_at_list,
            "timestamp" : timestamps
            }
    
    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"] )
    
    print(song_df)
        

    
    
    
    

