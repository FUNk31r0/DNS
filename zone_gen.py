import sys
try:	
	ip_telas = sys.argv[1]
	lista_dominios = sys.argv[2]
	lista = open(lista_dominios, 'r')
	for line in lista:
			line = line.replace('\n', "")
		 	zona = '''
$TTL 604800
@       IN      SOA     {}.      {} (
                2007031001
                28800
                3600
                604800
                38400
)
{}      IN      NS      {}
{}      IN      MX      10 mail.{}
{}      IN      A       {}
{}      IN      AAAA    0:0:0:0:0:ffff:b946:b8cf

www        IN       A            {}
www2       IN       A            {}
www3       IN       A            {}
www4       IN       A            {}
www5       IN       A            {}
www6       IN       A            {}
www7       IN       A            {}
www8       IN       A            {}
www9       IN       A            {}
www10      IN       A            {}
www11      IN       A            {}
www12      IN       A            {}
www13      IN       A            {}
www14      IN       A            {}
www15      IN       A            {}
www16      IN       A            {}
www17      IN       A            {}
www18      IN       A            {}
www19      IN       A            {}
www20      IN       A            {}
www21      IN       A            {}
www22      IN       A            {}
www23      IN       A            {}
www24      IN       A            {}
www25      IN       A            {}
www26      IN       A            {}
www27      IN       A            {}
www28      IN       A            {}
www29      IN       A            {}
www30      IN       A            {}
mail       IN       A            {}
aapj       IN       A            {}
dc  	   IN       A            {}
www.dc	   IN       A            {}
hb  	   IN       A            {}
*          IN       AAAA         0:0:0:0:0:ffff:b946:b8cf
'''.format(line, line, line, line, line, line, line, ip_telas, line, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas)
			arq = open("{}.zone".format(line), "wb")
			arq.write(zona)
			arq.close()
except:
	uso = """COMO USAR:
zone.gen.py <IP_TELAS> <LISTA_DOMINIOS.txt>"""
	print(uso)
