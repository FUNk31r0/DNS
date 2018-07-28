import sys
arq = open(sys.argv[1], 'r')

for line in arq:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        print("""
<VirtualHost {}:80>
    DocumentRoot "/var/www/html/{}"
    ServerName {}
    Redirect / https://{}
</VirtualHost>
""".format(line, line, line, line))
