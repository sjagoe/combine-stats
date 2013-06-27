combine-stats
=============

::

    $ ls
    ThreadPoolWorker-1.pstats
    ThreadPoolWorker-2.pstats
    MainThread.pstats
    $ combine-stats . --pattern "ThreadPoolWorker*" --output thread-pool.pstats
    
