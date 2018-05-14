BinaryNinja CryptoScan
======================
Plugin for [Binary Ninja](https://binary.ninja/) platform

## General
This plugin scans binaries for common crypto constants and - in a future release - attempts to detect functions that appear to be cryptographic in nature.
The constants are largely a port of the findcrypt IDA plugin constants. 

## Features
### Overview
The plugin registers a single call that is accessible from the 'Tools' menu or by right-clicking in the main binary view window. 

Scan configurations are reloaded on _every_ call to the scan function. This means you can CRUD json config files and rescan immediately. 

The plugin supports the following types of scans:

 - Scanning for constants in data 
 - Scanning for constants in the IL 
 - Scanning for crypto signatures based on function behaviour (WIP) 

### Report
If any matches are identified a Markdown (for GUI) or text (for CLI) report will be shown, listing which scans were matched, what family they belong to as well as the address in the binary.
The aim of the report was to allow easy copy-pasting of the address for use with the 'Go to address...' function. 

### Configuration
Individual scan configurations are kept in the scans subfolder. The following fields are required in the JSON:

 - name: short name for the scan
 - description: long name or description, only for author's quality of life
 - type: static or signature (signatures are currently not implemented though)
 - flags: array of single byte strings, usually 4 bytes but no upper bound is set. You can now add null bytes. 
 - on_match: object with subfields
   - type: symbol is the only supported value right now, adds a symbol at the detected address
   - name: name to give to the symbol

## TODO
- [ ] Add more constants 
- [ ] Flesh out how signature detection will work
- [x] Make CryptoScan run in the background
- [x] Deal with null bytes in the flags better
- [ ] Detect cryptocurrencies
