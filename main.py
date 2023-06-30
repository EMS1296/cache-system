from cache import Cache

# Example usage:
cache = Cache(3)
cache.put("key1", "value1")
cache.put("key2", "value2")
cache.put("key3", "value3")
cache.put("key4", "value4")

print(cache.get("key4"))
print(cache.get("key3"))
print(cache.get("key2"))
print(cache.get("key1"))  # Output: None
