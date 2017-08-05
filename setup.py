from setuptools import setup

setup(name='tx_push',
      version='0.1',
      description='Simple Flask based sendrawtransaction push API.',
      keywords=['peerassets', 'blockchain', 'assets', 'api'],
      url='https://github.com/peerassets/tx_push',
      author=['Peerchemist', 'Saeveritt'],
      license='BSD2',
      packages=['tx_push'],
      install_requires=['peercoin_rpc', 'flask']
      )
