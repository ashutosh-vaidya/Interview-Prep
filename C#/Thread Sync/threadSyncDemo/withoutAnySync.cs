using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace threadSyncDemo
{
    internal class withoutAnySync
    {
        public static void DoSomething()
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} starting...");
            Thread.Sleep(5000);
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} completed...");
        }
    }
}
