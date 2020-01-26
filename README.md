# filtercheck-exploring

explores data from https://map.internetintel.oracle.com/ixp/#/ixp/list

## requires

* python3
  * requests 

## basic usage

```
virtualenv -p python3 venv
. venv/bin/activate
pip3 install requests
# edit .py file to use particular data source you're interested in, this has MBIX by default
./spamhaus_prefix.py | less
```
