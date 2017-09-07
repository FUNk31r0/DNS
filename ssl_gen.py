import time
import sys
import os
arq = open(sys.argv[1])
for line in arq:
#	print line
	line = line.replace("\n", "")
	line = line.replace("\n", "")
	string = """
#!/bin/bash

function CreateCertificateAuthority {

if [ -f ./ubntCA.key ]; then rm ./ubntCA.key; fi
if [ -f ./ubntCA.pem ]; then rm ./ubntCA.pem; fi

#
# Create the Root Key
#
openssl genrsa -out ubntCA.key 2048

#
# Now self-sign this certificate using the root key.
#
# CN: CommonName
# OU: OrganizationalUnit
# O: Organization
# L: Locality
# S: StateOrProvinceName
# C: CountryName
#
openssl req -x509 \\
            -new \\
            -nodes \\
            -key ubntCA.key \\
            -sha256 \\
            -days 3650 \\
            -subj "/C=US/ST=IS/L=TOTALLY/O=CONFUSED/OU=HERE/CN=%s" \\
            -out ubntCA.pem

print ""
print "Now install this cert (ubntCA.pem) in your workstations Trusted Root Authority."
print ""

}

function CreateServerCertificate {

if [ -f ./server.key ]; then rm ./server.key; fi
if [ -f ./server.csr ]; then rm ./server.csr; fi
if [ -f ./server.crt ]; then rm ./server.crt; fi

#
# Create A Certificate
#
openssl genrsa -out server.key 2048

#
# Now generate the certificate signing request.
#
openssl req -new \\
            -key server.key \\
            -subj "/C=US/ST=IS/L=ALSOTOTALLY/O=CONFUSED/OU=HERE/CN=%s" \\
            -out server.csr

#
# Now generate the final certificate from the signing request.
#
openssl x509 -req \\
             -in server.csr \\
             -CA ubntCA.pem \\
             -CAkey ubntCA.key \\
             -CAcreateserial \\
             -extfile <(printf "subjectAltName=DNS:%s") \\
             -out server.crt -days 3650 -sha256

}

function CreateServerPem {

cat server.crt  > server.pem
cat server.key >> server.pem

}

   CreateCertificateAuthority
   CreateServerCertificate
   CreateServerPem

chown ro0t *

""" % (line, line, line)
	print string
	file = open(line+".sh", "w")
	file.writelines(string)
	file.close()
	time.sleep(1)
	os.system('chmod 777 %s.sh' %line)
	os.system('bash %s.sh' %line)
	os.system('rm %s.sh' %line)
	line = line.lower()
	os.system('mv server.pem certs/%s.pem' %line)
        os.system('mv server.key private/%s.key' %line)
	os.system('mv ubntCA.pem clientes/%s.pem' %line)
	os.system('rm ubntCA* && rm server*')
