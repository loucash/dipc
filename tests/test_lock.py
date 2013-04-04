import memcache
import mock
import sys
import unittest

sys.path.append("..")


class TestDistributedLock(unittest.TestCase):

    @mock.patch.object(memcache.Client, 'add', return_value=True)
    def test_lock_success(self, mc):
        from dipc import MemcacheLock
        ml = MemcacheLock(["localhost:11211"], "lock")
        result = ml.acquire(blocking=False)
        self.assertTrue(result)

    @mock.patch.object(memcache.Client, 'add', return_value=False)
    def test_lock_failed(self, mc):
        from dipc import MemcacheLock
        ml = MemcacheLock(["localhost:11211"], "lock")
        result = ml.acquire(blocking=False)
        self.assertFalse(result)
