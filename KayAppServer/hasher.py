import hashlib



def h(word):
    hash = hashlib.sha256()
    hash.update(word.encode('utf-8'));
    return hash.hexdigest();
