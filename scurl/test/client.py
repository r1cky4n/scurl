# Copyright (C) Jean-Paul Calderone
# See LICENSE for details.

from sys import argv, stdout
import socket

from OpenSSL.SSL import TLSv1_METHOD, SSLv3_METHOD, Context, Connection


def main():

    try:
        #create an AF_INET, STREAM socket (TCP)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit();
     
    print 'Socket Created'
     
    host = 'www.google.com'
    port = 80
     
    try:
        remote_ip = socket.gethostbyname( host )
     
    except socket.gaierror:
        #could not resolve
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
         
    client.connect((remote_ip, port))
    print 'connected', client.getpeername()

    client_ssl = Connection(Context(SSLv3_METHOD), client)
    client_ssl.set_connect_state()
    #client_ssl.set_tlsext_host_name(argv[1])
    client_ssl.do_handshake()
    print 'Server subject is', client_ssl.get_peer_certificate().get_subject()
    client_ssl.close()


if __name__ == '__main__':
    import client
    raise SystemExit(client.main())
