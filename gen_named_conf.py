import sys
try:
        lista = open(sys.argv[1])
        for line in lista:
                line = line.replace("\n", "") 
                print("""
zone "%s" IN {
        type master;
        file "/etc/%s.zone";
        allow-update { none; };
}; 

""" % (line, line))
except:
  print("""
  USO
 python gen_zones_conf.py <LISTA_DE_DOMINIOS.txt> >> <named.conf OR named.conf.local>
  """)

