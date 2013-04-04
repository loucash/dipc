import memcache
import mock
import sys
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
