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
openssl req -x509 \
            -new \
            -nodes \
            -key ubntCA.key \
            -sha256 \
            -days 3650 \
            -subj "/C=US/ST=IS/L=TOTALLY/O=CONFUSED/OU=HERE/CN=THEKEYMASTER.COM" \
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
openssl req -new \
            -key server.key \
            -subj "/C=US/ST=IS/L=ALSOTOTALLY/O=CONFUSED/OU=HERE/CN=APPLE.COM" \
            -out server.csr

#
# Now generate the final certificate from the signing request.
#
openssl x509 -req \
             -in server.csr \
             -CA ubntCA.pem \
             -CAkey ubntCA.key \
             -CAcreateserial \
             -extfile <(printf "subjectAltName=DNS:APPLE.COM") \
             -out server.crt -days 3650 -sha256

}

function CreateServerPem {

cat server.crt  > server.pem
cat server.key >> server.pem

}

   CreateCertificateAuthority
   CreateServerCertificate
   CreateServerPem
