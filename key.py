import rsa
(pubkey,privkey)=rsa.newKeys(512)
pub=pubkey.save_pkcs1()
print 'pub',pub
#pubfile=open('public.pem','w+')
#pubfile.write(pub)
#pubfile.close()
pri=privkey.save_pkcs1()
print 'proi',pri
