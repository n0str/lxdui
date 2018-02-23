import os

from pylxd import Client


class Connect:

    def __init__(self, password=''):
        path = os.path.abspath(os.path.dirname(__file__))
        self.certfile = os.path.join(path, "../conf/client.crt")
        self.keyfile = os.path.join(path, "../conf/client.key")
        self.password = password

    def remote(self):
        try:
            conn = Client(
                endpoint='https://45.76.43.148:8443',
                cert=(self.certfile, self.keyfile),
                verify=False
            )
            conn.authenticate(self.password)

            return {"error": False, "conn": conn}

        except Exception as e:
            return {"error": True,
                    "message": "We have trouble connecting to the LXD daemon. LXC/LXD might not be installed or either daemon not initialised up properly !\n{}".format(e)}

    def local(self):
        try:
            conn = Client()
            return {"error": False, "conn": conn}
        except Exception as e:
            return {"error": True,
                    "message": "We have trouble connecting to the LXD daemon. LXC/LXD might not be installed or either daemon not initialised up properly !\n{}".format(
                        e)}
