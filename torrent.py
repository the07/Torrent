from hashlib import md5, sha1
from random import choice
import socket
from struct import pack, unpack
from threading import Thread
from time import sleep, time
import types
from urllib import urlencode, urlopen
from utility import collapse, slice

from bencode import decode, encode

CLIENT_NAME = "GTorrent"
CLIENT_ID = "GTPY"
CLIENT_VERSION = "1.0.0"
