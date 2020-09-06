from bs4 import BeautifulSoup, Tag
import hashlib
import sys
import time

hashtexts = [
    '3d8e5aa60c8bd46df420ce72d0d2610307236d8ed78c368889dc996ea999b673',
    '3157f285df4107b29ca7010b954cd67b2cd5b0c096749729a6fb455c1da6731e',
    'ef2dc20c5eceb099c2de3c2dfacf61b353c9f6b29d32efa7fe3b48f920b9b930',
    'b5f3c8591aeec37400a3101c693748ddf662f6c056a9f70b5602d1b5c11aa34c',
    'f79fa8f3351824680b658f8960caa0ea42d0100cfcb6ea5cd572d9582dc8306d',
    '0b4b23c0a8166c985242528f014c310ec37f517927f5969084318d09c5418fea',
    '2f0863003eea928e193d911e4480c197679a13768165a3e9a20139997665ddbe',
    '2c405b6c5eb39df10553fd5434a21aa8dd6993cd6dd32eaa016c5c8bac9c92ac',
    '7182693412685bbe0f726bc7d70a580284bd6c7c5f75ac305c29205dcb1a8a02',
    '2ff001873cca2a02ab01e4f76193dfd52f2ded7cb5d232f78d76f92d97e89bee',
    '73dc86dc80fb3e539b7fb41f3043e925c7d05a430cb96fd4e9709c5a703688f4',
    '7107eba90dac7e8e5b05d155a67783117a7ffefea59c821c39b268cd16724ee5',
]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !';

def nest_tags(names):
    current = Tag(name=names[0])
    root = current
    for i in range(1, len(names)):
        new_tag = Tag(name=names[i])
        current.append(new_tag)
        current = new_tag
    return root

def get_plaintext(known_values, test_value):
    attempt_values = known_values + [test_value]
    html = nest_tags(attempt_values)
    return str(html)

def get_hashtext(known_values, test_value):
    plaintext = get_plaintext(known_values, test_value)
    return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()

def output_overwrite(text):
    sys.stdout.write('\r' + text.ljust(80))
    sys.stdout.flush()

values = []
for hash in hashtexts:
    for candidate in alphabet:
        output_overwrite("".join(values + [candidate]))
        time.sleep(0.01)
        text = get_hashtext(values, candidate)
        if text == hash:
            values.append(candidate)
            break
