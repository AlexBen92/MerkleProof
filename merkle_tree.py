import hashlib
def build_merkle_tree(data):
 if len(data) == 1:
 return data[0]
next_level = []
 for i in range(0, len(data), 2):
 hash_1 = hashlib.sha256(data[i].encode()).hexdigest()
 if i + 1 < len(data):
 hash_2 = hashlib.sha256(data[i + 1].encode()).hexdigest()
 else:
 hash_2 = hash_1
 next_level.append(hashlib.sha256((hash_1 + hash_2).encode()).hexdigest())
return build_merkle_tree(next_level)
# Example usage
data = ['transaction1', 'transaction2', 'transaction3', 'transaction4']
merkle_root = build_merkle_tree(data)
print("Merkle Root:", merkle_root)