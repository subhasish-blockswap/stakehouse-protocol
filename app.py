
# Flask utils
import json
import requests
import pandas as pd
import itertools
import threading
import time
import sys
import numpy as np
import datetime
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

from flask import Flask, redirect, url_for, request, render_template,g
from werkzeug.utils import secure_filename

#For Heroku Server Web App
from gevent.pywsgi import WSGIServer

from web3 import Web3, HTTPProvider

# Define a flask app
app = Flask(__name__)

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/6d3134d1d86843d59e639249171d1948'))
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
#Load your trained model

url = 'https://api.thegraph.com/subgraphs/name/bswap-eng/stakehouse-protocol'

value = '''
{
  events(
    orderBy: blockNumber, 
    orderDirection: desc,
    where:{
      key_not: "CIP_DECRYPTION_PIECE_RECEIVED"
    },
    first:1000
  ) {
    key
    value
    blockNumber
    blockTimestamp
  }
}
'''
payload = { 'query': value }

headers = { 'Content-Type': 'application/json'}





@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
            temp= request.form['id']
            print(temp)
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            json_data = json.loads(r.text)
            df_data = json_data['data']['events']
            df = pd.DataFrame(df_data)
            df['Timestamp']= df['blockTimestamp']
            df['Timestamp']= df['Timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d'))
            df['last']= df['Timestamp'].str.slice(0,7)
            df_july= df[df['last']== '2022-07']
            df_july_deposit= df[df['key']== str(temp)]
            df2= df_july_deposit.groupby(['Timestamp']).size().reset_index(name='count')
            plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees

            plt.plot(df2['Timestamp'], df2['count'])
            plt.xlabel("Date", labelpad=20)
            plt.legend()
            plt.title("Number Of Events Registered")
            plt.ylabel("Cumulative ETH Deposited", labelpad=20)
            plt.savefig("./static/squares.png", bbox_inches='tight')
            plt.close()
            return render_template('ethereum.html')
            


if __name__ == '__main__':
        app.run(threaded = False)
