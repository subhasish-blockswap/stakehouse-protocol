
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
            i= request.form['id']
            l= {'CIP_DECRYPTION_REQUESTED': 'Number of Decryptions Requested', 
            'DEPOSIT_REGISTERED': 'Number of ETH Deposits Registered',
       'DETH_REWARDS_MINTED': 'Number of dETH Rewards Minted', 'DETH_REWARDS_MINTED_IN_OPEN_INDEX': 'Number of dETH Rewards Minted Events',
       'DETH_WITHDRAWN_INTO_OPEN_MARKET': 'Number of dETH Rewards Withdrawn Into Open Market Events', 'INDEX_CREATED': 'Number of Index Created Events',
       'INITIALS_REGISTERED': 'Number Of Intitials Registed Events', 'KNOT_INSERTED_INTO_INDEX': 'Number of Knots Into Index',
       'KNOT_TRANSFERRED_FROM_INDEX': 'Number Of Knot Transferred From Index Events', 'NEW_HOUSE_MEMBER': 'Number of House Members',
       'NEW_STAKEHOUSE_REGISTRY_DEPLOYED': 'Number of StakeHouse Registries', 'RAGE_QUIT': 'Number of Rage Quits',
       'SIGNING_KEY_RE_ENCRYPTION': 'Number of Signing Key Encryptions', 'SLOT_SLASHED': 'Number of Slots Slashed', 'SLOT_TOPPED_UP': 'Number of Slots Topped Up'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            json_data = json.loads(r.text)
            df_data = json_data['data']['events']
            df = pd.DataFrame(df_data)
            df['Timestamp']= df['blockTimestamp']
            df['Timestamp']= df['Timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d'))
            df['last']= df['Timestamp'].str.slice(0,7)
            df_july= df[df['last']== '2022-07']
            df_july_deposit= df[df['key']== str(i)]
            df2= df_july_deposit.groupby(['Timestamp']).size().reset_index(name='count')
            plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees

            plt.plot(df2['Timestamp'], df2['count'])
            plt.xlabel("Date", labelpad=20)
            plt.legend()
            plt.title(l[i])
            plt.ylabel(l[i], labelpad=20)
            plt.savefig("./static/squares.png", bbox_inches='tight')
            plt.close()
            return render_template('ethereum.html')
            
            


if __name__ == '__main__':
        app.run(threaded = False)
