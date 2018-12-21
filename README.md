# binconverter.tk

## Summary

Fast and simple converter from binaries to integers/unsigned integers/floats (IEEE-754).

I needed such service for a long time, just to be able to stop infinitely using different calculators and be able to convert binaries transparently in many programmming languages from VBA and PHP to JS and GoLang. Now the time has come.

## Usage (and live demo)

Just a few links.

http://binconverter.tk/?bin=11111111111111111111111111001000&type=int

http://binconverter.tk/?bin=01000000111000110011110011010000&type=float

http://binconverter.tk/?bin=00100110&type=int

Supported types (for now): float, init, uint.

## Installation

Python 2 needed. Here are instructions to get bitstring module work on Ubuntu:

```
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install bitstring
```

To make it work on the same machine with Apache:

```
<VirtualHost *:80>
    ServerName binconverter.tk
    ServerAlias www.binconverter.tk
    ProxyPass / http://localhost:8080
    ProxyPassReverse / http ://localhost:8080
</VirtualHost>
```

Note that proxy_http mod must be enabled. If not, try do it with `sudo a2enmod proxy_http`.

Just clone this repo and run `python server.py`. You'll get your web-server on 8080 port (by default).

## TODO

Make port readable from config. Fix some errors. Change how-to-use message. Write unit tests. 

Commits are welcome!
