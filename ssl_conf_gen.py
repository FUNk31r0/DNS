import sys
arq = open(sys.argv[1])

for line in arq:
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        line = line.lower()
        print("""
<VirtualHost *:443>
    DocumentRoot "/var/www/html/{}"
    ServerName {}:443
        SSLEngine on
        SSLCertificateFile /etc/ssl/certs/{}.pem
        SSLCertificateKeyFile /etc/ssl/private/{}.key
        BrowserMatch "MSIE [2-5]" \\
         nokeepalive ssl-unclean-shutdown \\
         downgrade-1.0 force-response-1.0
</VirtualHost>
""".format(line, line, line, line))

