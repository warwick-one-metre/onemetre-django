import demjson
import requests
import socket

class RoomAlertHelpers():
    def query_roomalert_json(ip, timeout):
        # The Room Alert omits the HTTP header when returning JSON.
        # This violates the HTTP spec and prevents us from using the
        # standard query libraries.  We instead speak HTTP ourselves over a socket.
        try:
            sock = socket.create_connection((ip, 80), timeout)
            sock.sendall(bytes('GET /getData.htm HTTP/1.0\n\n', 'ascii'))

            data = [sock.recv(4096)]
            while data[-1]:
                data.append(sock.recv(4096))

        except Exception as e:
            raise Exception('Socket error while querying %s: %s' % (ip, str(e)))

        # The first line will either be the JSON we want, or a raw HTTP header
        response = ''.join(b.decode('ascii') for b in data)
        if response[0] != '{':
            raise Exception('Unexpected response from %s:\n%s' % (ip, response))

        # The JSON returned by earlier firmwares omits quotes around the keys
        # This violates the JSON specification, and is not accepted by the
        # built-in JSON parser.  demjson accepts this invalid input.
        return demjson.decode(response)

    # Query json from a static url (hosted on a proper web server)
    def query_dummy_json(url, timeout):
        r = requests.get(url, timeout=timeout)
        if r.status_code != requests.codes.ok:
            message = 'Invalid http status: ' + str(r.status_code) + '. ' + \
                      'Query was: `' + self.roomalert_url + '`. ' + \
                      'Response header was: ' + str(r.headers) + '.'
            raise Exception(message)

        return r.json()

