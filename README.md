# Smart-Ethereum-Transaction
The gas mechanism on the Ethereum blockchain attempts to set charges for every smart contract operation in order to prevent infinite control of computational resources by executing transactions. To satisfy this requirement, users need to specify in their transactions how much gas fees (in terms of gas limit and gas price) they would like to pay for. In essence, these gas fees are paid to the miners in return for their computational services. Naturally, miners tend to maximize their profits by considering the transactions with higher gas fees, and as a result, the transactions with lower gas fees remain in the waiting pool for a long time. This implementation is for a machine learning model to predict the transaction waiting time on the based on various transaction parameters.
> Research paper for this work has been accepted in [IEEE Trustcom](https://trustcom2021.sau.edu.cn/) and is yet to be presented. Complete work will be made public after the presentation only subject to copyright laws of IEEE.
## User Interface
A scaled down version of the model can used by visiting [Ethereum Transaction Web Application](http://ethereum-transactions.herokuapp.com/).
>Please note that this web application is a highly scaled down version of the model and is based on previous gas prices.
Repository of the model can visited at [Smart-Ethereum-Transactions](https://github.com/subhasishgoswami/Smart-Ethereum-Transaction)

## Proposed Architecture
The proposed model is based on use of various machine learning algorithms with the dataset of transaction parameters.
<br>
<br>
<div align="center" class="row">
  <img src="https://i.imgur.com/bYNKO3h.png" width="500"/>
</div>
<br>
<br>
The proposed model is based on use of following transaction parameters to analyse the transaction waiting time-


* Gas Price <br>
`A amount of ETH paid per unit of gas incurred against the execution of the transaction`
* Gas Limit <br>
`Gas limit for the miners for execution of a transaction`
* Block Difficulty
<br> `It denotes difficulty level of the block containing the transaction.`
* Transaction Hour
<br>`It indicates the hour of the day between 0 to 23 when a particular transaction was created`
* Transaction Type
<br>`It indicates whether a transaction is for a contract adress or account address`
* Time To Mine Last Block
<br>`Time taken to mine the last block on the blockchain`
* Mining Rate
<br>`Number of blocks mined in last x seconds`

To try the various algorithms on a smaller version of the dataset-
* **Random Forest**
```
* cd Model
* pip install -r requirements.txt
* python randomforest.py
```
* **kNN**
```
* cd Model
* pip install -r requirements.txt
* python knn.py
```
* **MLP**
```
* cd Model
* pip install -r requirements.txt
* python MLP.py
```
## Collaborators
This work was done in collaboration with Indian Institute of Technology, Patna and all the copyright rules are subject to IEEE's directives on publications. For any query regarding the project please reach out at subhasishgoswami00@gmail.com email.

