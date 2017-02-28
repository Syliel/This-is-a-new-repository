import requests

class KV(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.headers = {"Content-Type": "application/json"}
    def test(self):
        print(self.endpoint)
    def create(self, key, values):
        uri = endpoint + key
        try:
            r = requests.post(uri,
                              data=json.dumps(values),
                              headers+self.headers)
        except Exception as e:
            print("Failed to POST to %s, %s" % (uri, e))


