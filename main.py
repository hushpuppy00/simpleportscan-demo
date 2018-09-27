# !usr/bin/dev python3.5
# authror = "hushpuppy"
# time = "2107/6/23"

from simpoleportscan import simpleportscan

if __name__ == "__main__":
    ip = input("please input the ip:")
    port = [input("please input the scan port:").split(',')]
    res = simpleportscan(ip,*port)
    res.scan()