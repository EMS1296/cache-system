
# Top-Level Function Explanation:
1. get(key): This function takes a key as input and retrieves the corresponding value from the cache if it exists. It returns the value associated with the key or None if the key is not found in the cache.
1. put(key, value): This function adds or updates a key-value pair in the cache. If the key already exists in the cache, its value is updated. If the cache is full, it triggers the eviction policy to make space for the new key-value pair.
1. evict_oldest(): This function is responsible for evicting the oldest object from the cache. It removes the object that has been present in the cache for the longest duration, based on the eviction policy.

# Data Structure Used:
1. The data structure used in this cache system design is a combination of a dictionary (hash table) and a doubly linked list. The dictionary provides fast key-value lookups, while the doubly linked list maintains the order of the objects in the cache.
1. The dictionary (self.cache) stores the key-value pairs, allowing quick access to the values by their keys. The doubly linked list tracks the order of the objects, with the head representing the most recently used object and the tail representing the least recently used object.

# Eviction Policy:
1. The eviction policy employed in this cache system design is to evict the oldest object. When the cache reaches its maximum capacity and a new object needs to be added, the evict_oldest() function is called to remove the tail object from the doubly linked list and the dictionary.
1. The oldest object is determined by its position in the doubly linked list, with the tail being the oldest. By evicting the oldest object, the cache makes room for new objects while maintaining a limited size.

# Alternative Eviction Policies:
1. Least Recently Used (LRU): This policy evicts the least recently used object. The cache tracks the order of object usage, and when the cache is full, the least recently used object (tail) is evicted.
1. Most Recently Used (MRU): This policy evicts the most recently used object. In contrast to LRU, the MRU policy removes the most recently accessed object (head) when the cache reaches its capacity.
1. Least Frequently Used (LFU): This policy evicts the least frequently used object. The cache keeps track of the frequency of object accesses, and when the cache is full, the object with the lowest access frequency is evicted.
1. Random: This policy evicts a random object from the cache. It selects an object at random and removes it when the cache is full.
1. These alternative eviction policies offer different trade-offs in terms of cache performance, memory utilization, and implementation complexity. The choice of eviction policy depends on the specific requirements and characteristics of the system in which the cache is used.

# System Design:
The cache system design consists of two main components: the Cache class and the Node class. The Cache class handles the cache operations and maintains the key-value pairs, while the Node class represents individual objects in the cache, forming a doubly linked list.

The Cache class has the following attributes and methods:
## Attributes:
 * capacity: Represents the maximum capacity of the cache.
 * cache: Stores the key-value pairs in a dictionary for fast access.
 * head: Points to the most recently used object in the doubly linked list.
 * tail: Points to the least recently used object in the doubly linked list.
## Methods:
 * get(key): Retrieves the value associated with the given key from the cache.
 * put(key, value): Adds or updates the key-value pair in the cache.
 * evict_oldest(): Evicts the oldest object from the cache.
The Node class represents an object in the cache and has the following attributes:
* key: Represents the key associated with the object.
* value: Represents the value associated with the object.
* prev: Points to the previous object in the doubly linked list.
* next: Points to the next object in the doubly linked list.
## Use Cases:
The cache system can be used in scenarios where there is a need to store frequently accessed data for fast retrieval. Some use cases include:

Caching database query results to improve performance.
Storing computed values or expensive computations to avoid redundant processing.
Storing frequently accessed configuration or reference data.
Steps to Run:

To run the cache system, follow these steps:

1. Set up a Python development environment with Python 3 installed.
1. Create a new Python file, e.g., cache.py.
1. Copy and paste the cache system code into cache.py.
1. Create another Python file, e.g., main.py, to use the cache system.
1. In main.py, import the Cache class from cache.py.
1. Instantiate a Cache object with a desired capacity.
1. Use the cache object's get() and put() methods to interact with the cache system.
1. Run the main.py file to execute the cache system.
