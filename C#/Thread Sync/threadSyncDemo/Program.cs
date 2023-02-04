using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace threadSyncDemo
{
    internal class Program
    {
        private static object _locker = new object();
        private static ManualResetEvent _mre = new ManualResetEvent(false);
        private static AutoResetEvent _are = new AutoResetEvent(true);
        private static Mutex _mutex = new Mutex();
        private static Semaphore _semaphore = new Semaphore(2, 2);
        static void Main(string[] args)
        {
            for (int i = 0; i < 5; i++)
            {
                //Without using any locking or sync
                //All thread runs back to back withou stopping for other thread.

                //new Thread(DoSomething).Start();

                //using lock
                //Thread will wait to earlier therad to finish

                //new Thread(DoSomethingWithLock).Start();

                //using monitor
                //This work similar to Lock, infact lock is synatactical sugar to monitor
                //The difference between lock and monitor is you can add try catch and finally block 
                //if exception occured after monitor.Enter() it can be handled and in finally we can release the lock
                //This will prevent application from the deadlock, however this can also potential lead to more issues
                //since the faulty resource is now available for all the waiting threads. 

                //new Thread(DoSomethingWithMonitor).Start();
            }

            //using ManualResetEvent
            //This is useful when two threads are dependent on each other
            //For example, one thread is writing in to file and other threads are reading it.

            //new Thread(write).Start();

            //for (int i = 0;i < 5; i++)
            //{
            //    new Thread(read).Start();
            //}

            //using AutoResetEvent
            //This useful when all the thread wants to write to the file

            //for (int i = 0; i < 5; i++)
            //{
            //    new Thread(write1).Start();
            //}


            //Problem with AutoResetEvent is you can set the same object from another (main) thread 
            //See below

            //Thread.Sleep(1000);
            //_are.Set();

            //This leads to chaotic code.
            //To solve this we can use Mutex

            //Mutex
            //for (int i = 0; i < 5; i++)
            //{
            //    new Thread(writeMutex).Start();
            //}

            //Thread.Sleep(1000);
            //_mutex.ReleaseMutex(); // This will throw exception System.ApplicationException: 'Object synchronization method was called from an unsynchronized block of code.'

            //Semaphore
            // Summary:
            //     Limits the number of threads that can access a resource or pool of resources
            //     concurrently.
            //If we want to allow multiple thread to access the resource we can use semaphore
            //It will limit the threads using min, max property

            for (int i = 0; i < 5; i++)
            {
                new Thread(readSemaphore).Start();
            }            
            Console.ReadLine();
        }

        public static void DoSomething()
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} starting...");
            Thread.Sleep(5000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} completed...");
        }

        public static void DoSomethingWithLock()
        {
            lock(_locker)
            {
                Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} starting...");
                Thread.Sleep(5000);
                Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} completed...");
            }

        }

        public static void DoSomethingWithMonitor()
        {
            Monitor.Enter(_locker);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} starting...");
            Thread.Sleep(5000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} completed...");
            Monitor.Exit(_locker);

            //Can support try catch and finally
            //try
            //{
            //    Monitor.Enter(_locker);
            //    Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} starting...");
            //    Thread.Sleep(5000);
            //    Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} completed...");
            //}
            //catch (Exception ex)
            //{
            //    throw;
            //}
            //finally { Monitor.Exit(_locker); }
        }

        public static void writeMutex()
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} waiting...");
            _mutex.WaitOne();
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} writing...");
            Thread.Sleep(5000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} writing completed...");
            _mutex.ReleaseMutex();
        }


        public static void write1()
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} waiting...");
            _are.WaitOne();
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} writing...");
            Thread.Sleep(5000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} writing completed...");
            _are.Set();
        }

        public static void write()
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} writing...");
            _mre.Reset();
            Thread.Sleep(5000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} writing completed...");
            _mre.Set();
        }
        public static void read() {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} waiting...");
            _mre.WaitOne();
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} reading...");
            Thread.Sleep(2000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} reading completed...");
        }

        public static void readSemaphore()
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} waiting...");
            _semaphore.WaitOne();
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} reading...");
            Thread.Sleep(2000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} reading completed...");
            _semaphore.Release();
        }
    }
}
