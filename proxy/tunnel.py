from pyngrok import ngrok
from pyngrok.ngrok import NgrokTunnel

from configuration import DAPS_URL, NGROK_AUTH_TOKEN

ngrok.set_auth_token(NGROK_AUTH_TOKEN)


def create_tunnel() -> NgrokTunnel:
    return ngrok.connect(DAPS_URL)


def list_tunnels() -> list[NgrokTunnel]:
    return ngrok.get_tunnels()


def get_public_url(tunnel: NgrokTunnel) -> str:
    return tunnel.public_url


def close_tunnel(tunnel: NgrokTunnel):
    ngrok.disconnect(tunnel.public_url)
