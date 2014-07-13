from p2pool.bitcoin import networks

PARENT = networks.nets['krillcoin']
SHARE_PERIOD = 12 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 24 # blocks
IDENTIFIER = 'd3d427d41c2aea82'.decode('hex')
PREFIX = '5f819604be744ac0'.decode('hex')
P2P_PORT = 31235
MIN_TARGET = 16
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 31237
BOOTSTRAP_ADDRS = ['162.243.213.204']
ANNOUNCE_CHANNEL = '#p2pool-krl'
VERSION_CHECK = lambda v: True
