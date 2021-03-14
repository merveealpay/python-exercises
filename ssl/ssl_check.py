import socket
import ssl
import datetime
import requests

def ssl_expiry_datetime(hostname, port=443):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    #Create a SSLContext object with default settings.
    context = ssl.create_default_context()
    #objenin property ve valuesunu
    #print(context.__dict__)


    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # AF_INET = Address Family Internet = IPv4 tipinde adres
    # 3 saniye timeout
    conn.settimeout(3.0)

    conn.connect((hostname, port))
    ssl_info = conn.getpeercert()
    # Python datetime objesine sertifikadan bir string parse ediyor.
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)


# Kac gun kaldi sonlanmasina

def ssl_valid_time_remaining(hostname, port=443):
    expires = ssl_expiry_datetime(hostname, port)
    return expires - datetime.datetime.utcnow()


def check_ssl_expiry(hostname, port=443, warning_buffer=30, critical_buffer=7):
    days = ssl_valid_time_remaining(hostname, port).days
    if days < 0:
        print("FAILED:  {0} icin sertifikanin suresi doldu.".format(hostname))
    elif days < critical_buffer:
        print("CRITICAL: {0} icin sertifikanin suresinin expire olmasi cok yakin ({1} gun kaldi)".format(
            hostname, days
        ))
    elif days < warning_buffer:
        print("WARNING: {0} icin expire olma zamani yaklasiyor. ({1} gun kaldi.)".format(
            hostname, days
        ))
    #return olarak gondermen gerek print yapma
    else:
        print("OK: {0} icin sertifika suresi gayet iyi. ({1} gun kaldi.)".format(
            hostname, days
        ))


with open("hosts.txt") as file:
    for line in file:
        if line.strip().startswith("#"):
            continue
        #  bos satirlari gec
        if line.strip() is "":
            continue
        line = line.replace("\n", "")
        port = 443
        # www.example.com:8443
        if ":" in line:
            split_host = line.split(":")
            port = int(split_host[1])
            hostname = split_host[0]
        else:
            hostname = line
        try:
            check_ssl_expiry(hostname, port)
        except Exception as err:
            print("WARNING: Baglanamadi. {0}: {1}".format(
                hostname,
                err
            ))

