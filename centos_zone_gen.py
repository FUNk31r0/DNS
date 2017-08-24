import sys
try:	
	ip_telas = sys.argv[1]
	lista_dominios = sys.argv[2]
	lista = open(lista_dominios, 'r')
	for line in lista:
			line = line.replace('\n', "")
		 	zona = '''$TTL 86400
@     IN     SOA    {}     {}. (
                    2001062501 ; serial
                    21600      ; refresh after 6 hours
                    3600       ; retry after 1 hour
                    604800     ; expire after 1 week
                    86400 )    ; minimum TTL of 1 day

      IN     NS     dns1.{}.
      IN     NS     dns2.{}.

      IN     MX     20     mail2.{}.com.br.

             IN     A       {}

server1      IN     A       {}
dns1         IN     A       {}
dns2         IN     A       {}
www2         IN     A       {}
www1         IN     A       {}

ftp          IN       CNAME   server1
www          IN       CNAME   server1
www3         IN       CNAME   server1
www4         IN       CNAME   server1
www5         IN       CNAME   server1
www6         IN       CNAME   server1
www7         IN       CNAME   server1
www8         IN       CNAME   server1
www9         IN       CNAME   server1
www10        IN       CNAME   server1
www11        IN       CNAME   server1
www12        IN       CNAME   server1
www13        IN       CNAME   server1
www13        IN       CNAME   server1
www14        IN       CNAME   server1
www15        IN       CNAME   server1
www16        IN       CNAME   server1
www17        IN       CNAME   server1
www18        IN       CNAME   server1
www19        IN       CNAME   server1
www20        IN       CNAME   server1
www21        IN       CNAME   server1
www22        IN       CNAME   server1
www23        IN       CNAME   server1
www24        IN       CNAME   server1
www25        IN       CNAME   server1
www26        IN       CNAME   server1
www27        IN       CNAME   server1
www28        IN       CNAME   server1
www29        IN       CNAME   server1
www30        IN       CNAME   server1
mail         IN       CNAME   server1
aapj         IN       CNAME   server1
dc           IN       CNAME   server1
www.dc       IN       CNAME   server1
hb           IN       CNAME   server1
'''.format(line, line, line, line, line, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas, ip_telas)
			arq = open("{}.zone".format(line), "wb")
			arq.write(zona)
			arq.close()
except:
	uso = """COMO USAR:
zone.gen.py <IP_TELAS> <LISTA_DOMINIOS.txt>"""
	print(uso)
