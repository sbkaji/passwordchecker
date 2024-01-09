import requests
import hashlib
import sys
import time
import random

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    print("Searching on web...")
    time.sleep(5)
    print("***************")
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f'Request failed : {res.status_code}. Please try again with different charater string')
    else:
        return res


def get_hash_leak_count(hashes, hash):

    hashes = (line.split(':') for line in hashes.text.splitlines())
    for val, count in hashes:
        if(hash == val):
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    md5password=hashlib.md5(password.encode('utf-8')).hexdigest().upper()
    print("Encryption on process:")
    time.sleep(5)
    print("SHA1:",sha1password)
    print("MD5:",md5password)
    first_5_char, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first_5_char)

    return get_hash_leak_count(res, tail)


def main(passwords):
        count = pwned_api_check(passwords)
        if(count):
            print(
                f'Alert entered password:{passwords} is already breached. It was found used {count} times...')
            print("Suggestions:")   
            symbo=["@", "#", "$", "_", "%", "&"]
            charl = ["1", "2", "3", "4", "5", "6"]
            charl2 = ["7", "8", "9", "0", "1", "2"]
            char=random.choice(charl)
            char2=random.choice(charl2)
            sugges=char + random.choice(symbo) + passwords + char2
            print("password: ",sugges)
        else:
            print(f'Sucess! This password not found in database !!You can use this password')
            print("For Better Security we suggest:")   
            symbo=["@", "#", "$", "_", "%", "&"]
            charl = ["1", "2", "3", "4", "5", "6"]
            charl2 = ["7", "8", "9", "0", "1", "2"]
            char=random.choice(charl)
            char2=random.choice(charl2)
            sugges=char + random.choice(symbo) + passwords + char2
            print("password: ",sugges)


if(__name__ == '__main__'):
    print("Note: The password entered here is not saved in any server.")
    passwords = input("Enter your password to check: ")
    if(passwords==""):
          print("Empty input is not accepted")
          exit() 
sys.exit(main(passwords))       
    