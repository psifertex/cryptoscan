import binaryninja as bn
from CryptoScan import CryptoScan

def run_plugin(bv):
    # For now this will reload configs on every run, might be desirable.
    static_scan = bn.ChoiceField('Scan for constants', ['Yes', 'No'])
    signature_scan = bn.ChoiceField('Scan IL signatures', ['Yes', 'No'])
    bn.get_form_input([None, static_scan, None, signature_scan], 'Scanning options')
    options = {'static' : static_scan.result == 0, 'signature' : signature_scan.result == 0}
    if any(option for option in options.values()):
        cs = CryptoScan(bv, options)
        cs.start()
