import Fortune, sys
from omniORB import CORBA

orb = CORBA.ORB_init()

obj = orb.string_to_object("corbaname::localhost:1050/NameService#cookie")
cokie = obj._narrow(Fortune.CookieServer)

if cokie is None:
    print("Can't narrow reference")
    sys.exit(1)

print(cokie.get_cookie())

