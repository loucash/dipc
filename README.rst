dipc
=====================

Distributed Inter-Process Communication Library implemented in Python and Memcached_. server

.. _Memcached: http://memcached.org

Using dipc
==========

dipc library has two classes for distributed lock and semaphore, MemcacheLock
and MemcacheSemaphore

Both of those clases has a first argument which is a list of memcached servers,
name of lock/semaphore, ttl - timeout (in seconds). MemcacheSemaphore class has additional
parameter value - which is number of processes that can access critical
section.

acquire() method will wait forever until lock will be granted. You can specify 
argument blocking=False, and then will this methid will return True/False 
depending on if lock was granted or not.

    >>> from dipc import MemcacheLock
    ... ml = MemcacheLock(["localhost:11211"], "lock", ttl=60)
    ... ml.acquire()
    ... # critical section
    ... ml.release()

    >>> from dipc import MemcacheSemaphore
    ... ml = MemcacheSemaphore(["localhost:11211"], "semaphore", value=10, ttl=60)
    ... ml.acquire()
    ... # critical section
    ... ml.release()
