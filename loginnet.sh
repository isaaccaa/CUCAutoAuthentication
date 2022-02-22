#!/bin/bash
PING=`ping www.baidu.com -c 3 | grep 'Request timeout' | wc -l`
echo $PING
if [ $PING != '0' ]; then
    echo "Net Bad"
    python3 login.py
    exit 1;
fi