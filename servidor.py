import sys, os
import Fortune, Fortune__POA
import CORBA


FORTUNE_PATH = "/usr/games/fortune"

class CookieServer_i(Fortune__POA.CookieServer):
    def get_cookie(self):
        pipe   = os.popen(FORTUNE_PATH)
        cookie = pipe.read()
        if pipe.close():
            # An error occurred with the pipe
            cookie = "Deu certo, finalmente!!! \n"
        return cookie

sys.argv.extend(("-ORBInitRef", "NameService=corbaname::localhost:1050"))
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
poa.activate_object(servant)

ref = poa.id_to_reference(servant)
cookie = CookieServer_i()
servantId = poa.activate_object(cookie);

# Publish the hello object reference to the Naming Service
ref = poa.id_to_reference(servantId)

# Get the Naming Service's root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
	print("Failed to narrow the root naming context")
	sys.exit(1)

text = "cookie"
path = [CosNaming.NameComponent("cookie", "")]

try:
    # context.bind(path, ref)
    rootContext.bind(path, ref)
    print("Bound the hello object to the naming service")

except CosNaming.NamingContext.AlreadyBound as ex:
    print("Cookie object already bound, rebinding new object")
    # context.rebind(path, ref)
    rootContext.rebind(path, ref)

# Activate the POA Manager and run
poa._get_the_POAManager().activate()
print("Python Server active and waiting...")
orb.run()
