**What is Thread Synchronization**

Data inconsistency occurs when more than one thread accesses a shared resource such as in-memory data (instance of class, class variables) and external objects (files, database) at the same time. For example, let's assume thread 1 is writing the data to a file, while thread 2 attempting to read that file. This will cause data inconstancy and the potential to read stale data. To avoid this, thread synchronization can be implemented.

Synchronization ensures that only one thread is accessing the shared resource at any given point and prevents the other thread from accessing it simultaneously. The protected resource can be called a critical section, and synchronization ensures that only one thread can enter the critical section.

**Ways of Thread Synchronization**

**1) Lock:** 

The lock statement acquires the mutual exclusion lock for a given object, executes a statement block, and then releases the lock. While a lock is held, the thread that holds the lock can again acquire and release the lock. Any other thread is blocked from acquiring the lock and waits until the lock is released.

Lock is syntactic sugar to Monitor, in simpler words internally uses Monitor class.

Syntax:
```C#
public static readonly object obj = new object();
lock(obj) {
  //Critical Shared Resource doing something
}
```
>**NOTE:** Avoid using the same lock object instance for different shared resources, as it might result in a deadlock.

**2) Monitor:**

The Monitor Class in C# Provides a mechanism that synchronizes access to objects. In simple words, we can say that, like the lock, we can also use this Monitor Class to protect the shared resources in a multi-threaded environment from concurrent access. This can be done by acquiring an exclusive lock on the object so that only one thread can enter the critical section at any given point in time.

The Monitor class is a static class and belongs to the `System.Threading namespace`.

Syntax:
```C#
private static readonly lockObj = new object();

public void criticalMethod()
{
    //Entering critical code and locking it
    Monitor.Enter(obj);
    //Accessing critical resource to do something
    //All critical work is done
    //Exiting and releasing the shared resource
    Monitor.Exit(obj);
 }
 ```
 
We can also wrap the code in try-finally like this:
```C#
private static readonly lockObj = new object();
public void criticalMethod()
{
    try
    {
        //Entering critical code and locking it
        Monitor.Enter(obj);
        //Accessing critical resource to do something
     }
     finally
     {
         //All critical work is done
         //Exiting and releasing the shared resource
         Monitor.Exit(obj);
      }
 }
 ``` 
But it may not be a good idea. See this => [Lock and exceptions do not mix](https://learn.microsoft.com/en-us/archive/blogs/ericlippert/locks-and-exceptions-do-not-mix)

Monitor class have following methods which are also termed as a action that can be taken by the threads that access synchronized objects:

|Action|	Description|
|---|---|
|Enter, TryEnter|Acquires a lock for an object. This action also marks the beginning of a critical section. No other thread can enter the critical section unless it is executing the instructions in the critical section using a different locked object.|
|Wait|	Releases the lock on an object in order to permit other threads to lock and access the object. The calling thread waits while another thread accesses the object. Pulse signals are used to notify waiting threads about changes to an object's state.|
|Pulse (signal), PulseAll|	Sends a signal to one or more waiting threads. The signal notifies a waiting thread that the state of the locked object has changed, and the owner of the lock is ready to release the lock. The waiting thread is placed in the object's ready queue so that it might eventually receive the lock for the object. Once the thread has the lock, it can check the new state of the object to see if the required state has been reached.|
|Exit|	Releases the lock on an object. This action also marks the end of a critical section protected by the locked object.|

**Limitations of Lock and Monitor**

Lock and Monitor both work on in-process threads i.e threads generated inside the application itself. If an external process or thread enters the critical section then lock and monitor have no control over them. This is where we can use Mutex and Semaphore.

**3) Mutex:**

A Mutex is just like a lock, but it can work across multiple processes. In other words, Mutex can be computer-wide as well as application-wide. A common use case for a cross-process Mutex is to ensure that only one instance of a program can run at a time.

With a Mutex class, you call the `WaitOne()` method to lock and `ReleaseMutex()` to unlock. Closing or disposing a Mutex automatically releases it. Just as with the lock statement, a Mutex can be released only from the same thread that obtained it.

> Acquiring and releasing an uncontended Mutex takes a few microseconds — about 50 times slower than a lock.

Syntax:
```C#
using(Mutex mutex = new Mutex(false))
{
    //Entering the critical code
    if(!mutex.WaitOne(TimeSpan.FromSeconds(3), false))
    {
        //Accessing critical code to do something
    }
 }
 
 //This can also written as follows
 private static Mutex mutex = new Mutex();
 private static void criticalMethod()
 {
     //Entering critical code
     try
     {
         //block the current thread until recieves a signal
         mutex.WaitPne();
         //gets the access to the shared resource to do something
         //completes the works
      }
      finally
      {
          //release the shared resource
          mutex.ReleaseMutex();
      }
 } 
 ```
 
Using the `using` block is recommended way since class `Mutex` is derived from `WaitHandle` which implements `IDisposible` interface. If `using` is not used then we have to make sure to call `Dispose()` manually.  
    










4. Manual Reset Event
5. Auto Reset Event
6. Mutex
7. Semaphore
8. Semaphore Slim

Ref: 
* [Thread Synchronization in C# .Net made easy! | Lock | Monitor | Mutex | Semaphore](https://youtu.be/5Zv8fF-KPrE)
* [Thread Synchronization in C#](https://dotnettutorials.net/lesson/thread-synchronization-in-csharp/)
* [Lock](https://dotnettutorials.net/lesson/locking-in-multithreading/)
* [Monitor](https://dotnettutorials.net/lesson/multithreading-using-monitor/)
* [Mutex](https://dotnettutorials.net/lesson/mutex-in-multithreading/)
* [Semaphor](https://dotnettutorials.net/lesson/semaphore-in-multithreading/)
* [SemaphoreSlim](https://dotnettutorials.net/lesson/semaphoreslim-class-in-csharp/)
