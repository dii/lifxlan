from .device import *
from .group import Group
from .lifxlan import LifxLAN
from .light import *
from .message import *
from .msgtypes import *
from .multizonelight import *
from .switch import *
from .tilechain import Tile, TileChain
from .unpack import unpack_lifx_message
from .utils import *

__version__ = "1.2.8"
__description__ = "API for local communication with LIFX devices over a LAN."
__url__ = "http://github.com/mclarkk/lifxlan"
__author__ = "Meghan Clark"
__authoremail__ = "mclarkk@berkeley.edu"
__license__ = "MIT"
