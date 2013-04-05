import memcache
import mock
import sys
import time
import unittest

sys.path.append("..")

from dipc import MemcacheSemaphore


class TestDistributedSemaphore(unittest.TestCase):

    @mock.patch.object(memcache.Client, 'add', return_value=True)
    def test_semaphore_success(self, mc):
        ml = MemcacheSemaphore(["localhost:11211"], "lock", 1)
        result = ml.acquire(blocking=False)
        self.assertTrue(result)

    @mock.patch.object(memcache.Client, 'add', return_value=False)
    def test_semaphore_failed(self, mc):
        ml = MemcacheSemaphore(["localhost:11211"], "lock", 1)
        result = ml.acquire(blocking=False)
        self.assertFalse(result)

    @mock.patch.object(memcache.Client, 'delete')
    @mock.patch.object(memcache.Client, 'add', return_value=True)
    def test_semaphore_released(self, mc_add, mc_delete):
        ml = MemcacheSemaphore(["localhost:11211"], "lock", 1, ttl=300)
        ml.acquire(blocking=False)
        ml.release()
        self.assertTrue(mc_delete.called)

    @mock.patch.object(memcache.Client, 'delete')
    @mock.patch.object(memcache.Client, 'add', return_value=True)
    def test_semaphore_released_lock_timeouted(self, mc_add, mc_delete):
        ml = MemcacheSemaphore(["localhost:11211"], "lock", 1, ttl=1)
        ml.acquire(blocking=False)
        time.sleep(2)
        ml.release()
        self.assertFalse(mc_delete.called)
