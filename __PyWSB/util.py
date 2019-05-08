def system():
    import sys
#sys,argv  sys.copyright
#sys.platform  >>

    print("platform: ", sys.platform)
    print("version intrpreter ", sys.version)

def python_version():   # w funkcji import
  from sys import version
  print("version ", version)


# requests

import requests

r=requests.get("https://google.com")