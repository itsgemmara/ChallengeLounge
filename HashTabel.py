import operator
import mmh3
import xxhash
import hashlib


def murmurhash(message):
    hash_value = mmh3.hash(str(message), seed=0)
    return hash_value


def sha_256(message):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode('utf-8'))
    hash_value = sha256_hash.digest()
    return hash_value


def sha3_256(message):
    sha3_hash = hashlib.sha3_256()
    sha3_hash.update(message.encode('utf-8'))
    hash_value = sha3_hash.digest()
    return hash_value


def xxhash32(message):
    hasher = xxhash.xxh32()
    hasher.update(message.encode('utf-8'), seed=0)
    hash_value = hasher.digest()
    return hash_value


class HashTabel:
    """
    Hash functions
    ---------
    - hash_sha3_256
    - hash_sha_256
    - xxhash32 
    - murmurhash

    Params
    ----------
    - initial_capacity `int`
    - load_factor `float`
    - self.hash_function `str`

    """        

    def __init__(self, initial_capacity: int=10, load_factor: float=0.75, hash_function: str='sha_256'):
        self.capacity = initial_capacity
        self.buckets = [[] for i in range(self.capacity)]
        self.number_of_elements = 0 #size
        self.load_factor = load_factor
        self.hash_function = hash_function

    # ---------- validate ------------

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def load_factor(self):
        return self._load_factor
    
    @property
    def hash_function(self):
        return self._hash_function

    @capacity.setter
    def capacity(self, value):
        if type(value) != int:
            raise Exception("capacity should be integer. not {}".format(type(value)))
        self._capacity = value
        
    @load_factor.setter
    def load_factor(self, value):
        if type(value) != float and type(value) != int:
            raise Exception("load_factor should be an integer number or a float number. not {}".format(type(value)))
        self._load_factor = value

    @hash_function.setter
    def hash_function(self, value):
        if value not in['sha_256', 'sha3_256', 'xxhash32', 'murmurhash']:
            raise Exception("hash function should be one of the (sha_256, sha3_256, xxhash32, murmurhash) not {}".format(value))
        self._hash_function = value

    # ----------- hash --------------

    def _hash(self, hessed_key):
        return hessed_key % self.capacity

    def hash_sha_256(self, key):
        hashed_message = sha_256(key)
        hash_value = int.from_bytes(hashed_message, "big")
        return hash_value

    def hash_sha3_256(self, key):
        hashed_message = sha3_256(key)
        hash_value = int.from_bytes(hashed_message, "big")
        return hash_value

    def hash_xxhash32(self, key):
        hashed_message = xxhash32(key)
        hash_value = int.from_bytes(hashed_message, "big")
        return hash_value

    def hash_murmurhash(self, key):
        hashed_message = murmurhash(key)
        hash_value = int.from_bytes(hashed_message, "big")
        return hash_value
    
    # ----------- index -------------
    
    def get_index(self, key):
        if self.hash_function == 'sha_256':
            hashed_msg = self.hash_sha_256(key)
        elif self.hash_function == 'sha3_256':
            hashed_msg = self.hash_sha3_256(key)
        elif self.hash_function == 'xxhash32':
            hashed_msg = self.hash_xxhash32(key)
        elif self.hash_function == 'murmurhash':
            hashed_msg = self.hash_murmurhash(key)
        else:
            raise Exception("coulden't hash key using {} hash function".format(self.hash_function))
        return self._hash(hashed_msg)
    
    # ----------- resize ------------
    
    def _resize(self, up=True):
        if up:
            self.capacity *= 2
        else:
            self.capacity = max(self.capacity // 2, 1)
        new_buckets = [[] for _ in range(self.capacity)]
        for bucket in self.buckets:
            for key, val in bucket:
                new_buckets[self.get_index(key)].append((key, val))
        self.buckets = new_buckets
                    
    # ----------- insert ------------

    def insert(self, key, value):
        index = self.get_index(key,)
        bucket = self.buckets[index]
        for c, (existing_key, existing_value) in enumerate(bucket):
            if key == existing_key:
                bucket[c] = (key, value)
                return
        bucket.append((key, value))
        self.number_of_elements += 1
        if self.capacity >= self.capacity * self.load_factor:
            self._resize()
    
    # ------------ get --------------

    def get(self, key):
        index = self.get_index(key, )
        bucket = self.buckets[index]
        for existing_key, value in bucket:
            if key == existing_key:
                return value
        return KeyError('{} not found!'.format(key))
    
    # ----------- remove ------------

    def remove(self, key):
        index = self.get_index(key,)
        bucket = self.buckets[index]
        for c, (existing_key, value) in enumerate(bucket):
            if key == existing_key:
                del bucket[c]
                self.size -= 1
                if self.size <= self.capacity * 0.25:
                    self._resize(up=False)
                return
        return KeyError('{} not found!'.format(key))
    
    # ------------- itrate -------------

    def __iter__(self):
        for bucket in self.buckets:
            for key, value in bucket:
                yield key, value
        
    
