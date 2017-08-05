from flask import Flask, jsonify
from peercoin_rpc import Client

node = Client(testnet=True)

app = Flask(__name__)


@app.route('/sendrawtransaction/<txid>')
def sendtx(txid):
    result = node.sendrawtransaction(txid)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
