# bitcoin-explorer - Bitcoin Blockchain Local Maltego Transform Pack

Author : @bostonlink

## About

Maltego local transform pack that parses the Bitcoin Blockchain (blockexplorer.com) and creates Maltego graphs based on bitcoin wallet addresses and transactions.  Will allow analysts to look up specific addresses and identify relationships between transactions and holding patterns visually.  Further, it will allow analysts to quickly follow specific Bitcoin transactions in the case of following stolen bitcoins easily and percisely with the data returned from blockexplorer.com.  In addition if an owner of a specifc bitcoin address discloses the address publicly in a way that reveals their online persona or identify then it is possible to relate a bitcoin wallet address to a specific persona or identity in this way.  

Directory Structure:

* `src/bitcoin-explorer` directory is where all the magic stuff goes and happens.
* `src/bitcoin-explorer/transforms` directory is where all the transform modules are located.
* `src/bitcoin-explorer/transforms/common` directory is where common code for all transforms are stored.
* `src/bitcoin-explorer/transforms/common/entities.py` is where custom entities are defined.
* `maltego/` is where the Maltego entity exports are stored.
* `src/bitcoin-explorer/resources/maltego` directory is where the `entities.mtz` and `*.machine` files are stored for auto install and uninstall.

## 2.0 - Installation

### 2.1 - Supported Platforms
bitcoin-explorer has currently been tested on Mac OS X and Linux.
Further testing will be done on Windows in the near future.

### 2.2 - Requirements
bitcoin-explorer is supported and tested on Python 2.7.x

The canari framework must be installed to use this package
See: https://github.com/allfro/canari

This package depends on the python requests package, the package will be installed when you run setup.py automatically if you do not already have the 'requests' package installed.

### 2.3 - How to install
Once you have the Canari framework installed and working, follow the directions below to install bitcoin-explorer

Install the package:

```bash
$ cd bitcoin-explorer
$ python setup.py install
```
Then install the canari package by issuing the following:

```bash
$ canari create-profile bitcoin-explorer
```

 INSTRUCTIONS:
 -------------
 1. Open Maltego.
 2. Click on the home button (Maltego icon, top-left corner).
 3. Click on 'Import'.
 4. Click on 'Import Configuration'.
 5. Follow prompts.
 6. Enjoy!

Once installed you must edit the bitcoin-explorer.conf file with local environment settings. Note currently there are no configuration options in the bitcoin-explorer package.

```bash
$ vim ~/.canari/bitcoin-explorer.conf
```
All Done!!  Have fun!

## Special Thanks!

The entire Bitcoin and crypto currency community
Paterva (@Paterva)<br/>
Nadeem Douba (@ndouba)<br/>
MassHackers (@MassHackers)<br/>
GuidePoint Security LLC. (@GuidePointSec)<br/>