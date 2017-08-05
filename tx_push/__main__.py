from sys import argv
from flask import Flask, jsonify
from peercoin_rpc import Client

app = Flask(__name__)


@app.route('/sendrawtransaction/<txid>')
def sendtx(txid):

    assert isinstance(txid, str), {'error': 'we only take strings around here.'}

    result = node.sendrawtransaction(txid)
    return jsonify(result)


if __name__ == '__main__':

    if argv[1] == "-testnet":
        node = Client(testnet=True)
        print("Running in testnet mode.")
        app.run(host='0.0.0.0', port=5555)

    else:
        node = Client(testnet=False)
        print("Running in mainnet mode.")
        app.run(host='0.0.0.0', port=5555)
