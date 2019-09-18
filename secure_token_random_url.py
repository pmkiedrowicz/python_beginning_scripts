'''
Generate random secure token of 64 bytes and random URL.
'''
import secrets


def secure_token():
    return secrets.token_bytes(64)


def random_url():
    return secrets.token_urlsafe(32)


url = "www.google.com/?reset_password="+random_url()

print("Secure 64b token: ", secure_token())
print("Random url: ", url)
