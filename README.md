# wappalyzer-docker-reporter

A python wrapper for wappalyzer's docker container to scan a list of endpoints and produce a human-readable HTML report

## Requires:

* Docker
* wappalyzer-clie docker image - available [here](https://hub.docker.com/r/wappalyzer/cli/)

## Usage:

```
./python wappalyzer-docker-reporter.py <list_of_urls> <output.html>
```
