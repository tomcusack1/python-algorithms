#!/usr/bin/env python

from python_ping import ping

# host = Host you want to ping
p = ping.Ping(host, timeout=3000, quiet=True, silent=True, ipv6=False)
stats = p.run(1)  # PingStats
