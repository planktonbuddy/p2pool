from p2pool.bitcoin import networks

PARENT = networks.nets['krillcoin_testnet']
SHARE_PERIOD = 4 # seconds
CHAIN_LENGTH = 20*60//3 # shares
REAL_CHAIN_LENGTH = 20*60//3 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'adb1b3ddd3c52322'.decode('hex')
PREFIX = '5261c8dc0dc6b59f'.decode('hex')
P2P_PORT = 32223
MIN_TARGET = 16
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 32229
BOOTSTRAP_ADDRS = []
ANNOUNCE_CHANNEL = '#p2pool-krl-test'
VERSION_CHECK = lambda v: True
