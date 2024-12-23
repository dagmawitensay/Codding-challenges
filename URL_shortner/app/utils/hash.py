import hashlib
import string

BASE62_ALPHABET = string.ascii_letters + string.digits

def base62_encode(num: int) -> str:
    """Encodes an integer into a Base62 string"""
    if num == 0:
        return BASE62_ALPHABET[0]
    base62 = []
    while num > 0:
        num, remainder = divmod(num, 62)
        base62.append(BASE62_ALPHABET[remainder])
    
    return "".join(reversed(base62))

def shorten_url_helper(long_url: str) -> str:
    """Generates a shortened URL key using SHA256 and Base62."""
    # Step 1: Generate SHA256 hash
    sha256_hash = hashlib.sha256(long_url.encode()).hexdigest()
    
    truncated_hash = sha256_hash[:7] 
    hash_int = int(truncated_hash, 16)

    # Step 3: Encode the integer in Base62
    short_key = base62_encode(hash_int)

    return short_key