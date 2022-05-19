import json
import requests
import hashlib

CASE_URL = "https://webf.cych.org.tw/IpdInfo/api/PatSmpInfo?id1=%s&id2=%s&Key=%s"
CASE_VAR = "1"
CASE_BASE_HASH = "tPptRZeYS5472rEoZBd48QmkxU2Sofu5kcoHnFjHGyqt7ltKSyKHLlnUCex54ULF"

temp = ''

def get_case_num(id_num):
    con = "%s^%s^%s" % (CASE_BASE_HASH, CASE_VAR, id_num)
    sha1 = hashlib.sha1()
    sha1.update(con.encode('utf-8'))
    hashed = sha1.hexdigest()
    try:
        r = requests.get(CASE_URL % (CASE_VAR, id_num, hashed))
        mj = r.json()[0]
        print(mj)
        print(type(mj))
        print(mj['pat_no'])
        return mj["pat_no"]
    except Exception as e:
        global temp
        print('except')
        print(e)
        return None

print(get_case_num('O100440517'))
