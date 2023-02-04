using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

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
