#
# * Decorators for distributed lock and semaphore based on Memcache
#
# Lukasz Biedrycki <lukasz.biedrycki@gmail.com>
#

from lock import MemcacheLock
from semaphore import MemcacheSemaphore


def distributed_lock(hosts, name, ttl=30):
    def _memcache_lock(f):
        def wrapper(*args, **kwargs):
            if callable(hosts):
                hostlist = hosts()
            if not isinstance(hostlist, list):
                hostlist = [hostlist]
            ml = MemcacheLock(hostlist, name, ttl)
            with ml:
                return f(*args, **kwargs)
        return wrapper
    return _memcache_lock


def distributed_semaphore(hosts, name, value, ttl=30):
    def _memcache_semaphore(f):
        def wrapper(*args, **kwargs):
            if callable(hosts):
                hostlist = hosts()
            if not isinstance(hostlist, list):
                hostlist = [hostlist]
            ms = MemcacheSemaphore(hostlist, name, value, ttl)
            with ms:
                return f(*args, **kwargs)
        return wrapper
    return _memcache_semaphore
