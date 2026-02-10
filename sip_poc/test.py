#!/usr/bin/env python3

import pjsua2 as pj
import time

AUTH_NAME='101'
DISPLAY_NAME='jaredlovell'
PASSWORD='v6Ige2f45SSTgM4oAE5c'


# Subclass to extend the Account and get notifications etc.
class Account(pj.Account):
  def onRegState(self, prm):
      print("***OnRegState: " + prm.reason)

# pjsua2 test function
def pjsua2_test():
  # Create and initialize the library
  ep_cfg = pj.EpConfig()
  ep = pj.Endpoint()
  ep.libCreate()
  ep.libInit(ep_cfg)

  # Create SIP transport. Error handling sample is shown
  sipTpConfig = pj.TransportConfig();
  sipTpConfig.port = 5060;
  sipTpConfig.public_address = '192.168.1.51';
  ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig);
  # Start the library
  ep.libStart();

  acfg = pj.AccountConfig();
  acfg.idUri = "sip:101@192.168.1.51"
  acfg.idUri = "sip:101@192.168.1.24"
  acfg.regConfig.registrarUri = "sip:192.168.1.24";
  cred = pj.AuthCredInfo("digest", "192.168.1.24", AUTH_NAME, 0, PASSWORD);
  acfg.sipConfig.authCreds.append( cred );
  # Create the account
  acc = Account();
  acc.create(acfg);
  # Here we don't have anything else to do..
  time.sleep(120);

  # Destroy the library
  ep.libDestroy()

#
# main()
#
if __name__ == "__main__":
  pjsua2_test()
