from sightengine.client import SightengineClient
client = SightengineClient('426576713', 'QCxr9vX5AZQP7nTnqxFm')
output = client.check('face-attributes').set_file('1.jpg')