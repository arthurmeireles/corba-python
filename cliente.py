import CORBA, Fortune, sys
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
#pegar o argumento de entrada
ior = sys.argv[1]
#converte o objeto em string, algo assim.
o = orb.string_to_object(ior)
o = o._narrow(Fortune.CookieServer)
print o.get_cookie(  )






# import CORBA, Fortune
# orb = CORBA.ORB_init(  )
# o = orb.string_to_object("corbaloc::host.example.com/fortune")
# o = o._narrow(Fortune.CookieServer)
# print o.get_cookie(  )