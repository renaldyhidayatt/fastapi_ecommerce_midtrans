from midtransclient import Snap
from .config import Settings

snap = Snap(
    is_production=False,
    server_key=Settings.MIDTRANS_SERVER_KEY,
    client_key=Settings.MIDTRANS_CLIENT_KEY,
)
