using System;
using System.Threading;

namespace threadSyncDemo
{
    internal class usingLock
    {
        private static object _locker = new object();
        public static void DoSomething()
        {
            lock(_locker)
            {
                Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} starting...");
                Thread.Sleep(5000);
                Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} completed...");
            }
        }
    }
}
