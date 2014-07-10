import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fe0cf2db'.decode('hex')
P2P_PORT = 32124
ADDRESS_VERSION = 48
RPC_PORT = 32123
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'krillcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 100000000 if height < 100 else 100*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('skeinhash').getPoWHash(data))
BLOCK_PERIOD = 120 # s
SYMBOL = 'KRL'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Krillcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Krillcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.krillcoin'), 'krillcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = ''
ADDRESS_EXPLORER_URL_PREFIX = ''
TX_EXPLORER_URL_PREFIX = ''
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
