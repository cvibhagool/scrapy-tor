# scrapy-tor
This is a scrapy project skeleton with Tor integration

# How to get started
Beacuse scrapy does not work with SOCKS proxy, you'll need to set up a web proxy server that relays requests to Tor. 
You can install [Polipo](http://www.pps.univ-paris-diderot.fr/~jch/software/polipo/), a lightweight web proxy. Then point Polipo to Tor's listening port, which is 9050 by default.

Uncomment or add the following lines to Polipo's config file `etc/polipo/config` to set up Polipo.
```
socksParentProxy = localhost:9050
disableLocalInterface=true
diskCacheRoot = ""
```
The function `ProxyMiddleware` defined in `middlewares.py` will relay all scrapy's requests to Polipo's default port of 8123

Don't forget to start Polipo and Tor before scraping!
