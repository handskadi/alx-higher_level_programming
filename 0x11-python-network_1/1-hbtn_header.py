#!/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as res:
        x_req_id = dict(res.headers).get("X-Request-Id")
        print(x_req_id)
        
