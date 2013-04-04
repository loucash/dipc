#
# * Distributed lock based on Memcache
#
# Lukasz Biedrycki <lukasz.biedrycki@gmail.com>
#

import logging
import memcache
import time

log = logging.getLogger(__name__)


class MemcacheLock(object):

    def __init__(self, hosts, name, ttl=30, debug=False):
        self.client = memcache.Client(hosts, debug=debug)
        self.name = name
        self.ttl = ttl
        self._when_locked = None

    def acquire(self, blocking=True):
        while True:
            result = self.client.add(self.name, "1", time=self.ttl)
            if result:
                self._when_locked = time.time()
                return True
            if not blocking:
                break
            time.sleep(0.5)
        return False

    __enter__ = acquire

    def is_locked(self):
        locked = self._when_locked is not None and \
            self._when_locked > time.time() - self.ttl
        return locked

    def release(self):
        if self.is_locked():
            self._when_locked = None
            self.client.delete(self.name)

    def __exit__(self, t, v, tb):
        self.release()
