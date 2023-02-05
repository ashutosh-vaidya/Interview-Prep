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
 
> Using the `using` block is recommended way since class `Mutex` is derived from `WaitHandle` which implements `IDisposible` interface. If `using` is not used then we have to make sure to call `Dispose()` manually. 

If a thread terminates while owning a mutex, the mutex is said to be abandoned. The state of the mutex is set to signaled, and the next waiting thread gets ownership. Beginning in version 2.0 of the .NET Framework, an `AbandonedMutexException` is thrown in the next thread that acquires the abandoned mutex. 

In the case of a system-wide mutex, an abandoned mutex might indicate that an application has been terminated abruptly (for example, by using Windows Task Manager).

>***Caution:*** An abandoned mutex often indicates a serious error in the code. When a thread exits without releasing the mutex, the data structures protected by the mutex might not be in a consistent state. The next thread to request ownership of the mutex can handle this exception and proceed, if the integrity of the data structures can be verified. 

**Types of Mutex**

Mutexes are of two types: 
1. Local mutexes, which are unnamed. A local mutex exists only within your process. It can be used by any thread in your process that has a reference to the Mutex object that represents the mutex. Each unnamed Mutex object represents a separate local mutex.
2. Named system mutexes, this are visible throughout the operating system, and can be used to synchronize the activities of processes. You can create a Mutex object that represents a named system mutex by using a constructor that accepts a name. The operating-system object can be created at the same time, or it can exist before the creation of the Mutex object. You can create multiple Mutex objects that represent the same named system mutex, and you can use the `OpenExisting` method to open an existing named system mutex.

**4) Semaphore:**

Using Mutex, only one external thread can access our application code at any given point in time and this we have already seen in our previous article. But, if we want more control over the number of external threads that can access our application code, then we need to use the Semaphore class in C#.

In simplar words, the Semaphore class is used to limit the number of external threads that can access a shared resource concurrently.

Syntax:
```C#
public static Semaphore semaphore = new Semaphore(initialCount:2, maximumCount:3)
public void criticalWorkMethod()
{
    //External Thread trying to access critical shared resource
    semaphore.WaitOne();
    //Following code block can be accessed by maximum 2 threads
        //Do some work
        //Completed the work
    //release the lock
    semaphore.Release();
 }
 ```
The count on a semaphore is decremented each time a thread enters the semaphore, and incremented when a thread releases the semaphore. When the count is zero, subsequent requests block until other threads release the semaphore. When all threads have released the semaphore, the count is at the maximum value specified when the semaphore was created.

There is no guaranteed order, such as FIFO or LIFO, in which blocked threads enter the semaphore.

**5) SemaphoreSlim:**

The SemaphoreSlim Class in C# is recommended for synchronization within a single app. The SemaphoreSlim class represents a lightweight, fast semaphore that can be used for waiting within a single process when wait times are expected to be very short.

Unlike the Semaphore class, the SemaphoreSlim class doesn’t support named system semaphores. You can use it as a local semaphore only.

**Signaling Methodology**

Along with all these locking mechanisms, we can also achieve thread synchronization using the Signaling technique. Here once thread 1 got access to the critical resource/method it signals other threads to wait and once it is done with the process it signals other threads that the resource is now available for access.

Use case of this 

There are two ways of signaling methodology,

**1) AutoResetEvent:** 

AutoResetEvent is used to send signals between two threads. This class Notifies a waiting thread that an event has occurred.

This is a sealed class and hence cannot be inherited. And it is inherited from the `EventWaitHandle` class.

**How AutoResetEvent Work in C#?**

The AutoResetEvent in C# maintains a boolean variable in memory. If the boolean variable is false then it blocks the thread and if the boolean variable is true it unblocks the thread. So, when we create an instance of AutoResetEvent class, we need to pass the default value of the boolean value to the constructor of AutoResetEvent class. The following is the syntax to instantiate an AutoResetEvent object.
```C#
AutoResetEvent autoResetEvent = new AutoResetEvent(false);
```

The WaitOne method blocks the current thread and waits for the signal by another thread. That means the WaitOne method puts the current thread into a Sleep state of the thread. The WaitOne method returns true if it receives the signal else returns false. We need to call the WaitOne method on the AutoResetEvent object as follows.
```C#
autoResetEvent.WaitOne();
//or we can use
autoResetEvent.WaitOne(TimeSpan.FromSeconds(2);
```

The Set method sent the signal to the waiting thread to proceed with its work. Following is the syntax to call the Set method.
```C#
autoResetEvent.Set();
```

>**Note:** The most important point that you need to remember is both threads will share the same AutoResetEvent object. Any thread can enter into a wait state by calling the WaitOne() method of the AutoResetEvent object. When the other thread calls the Set() method it unblocks the waiting thread.

There is no guarantee that every call to the Set method will release a thread. If two calls are too close together, so that the second call occurs before a thread has been released, only one thread is released. It’s as if the second call did not happen. Also, if Set is called when there are no threads waiting and the AutoResetEvent is already signaled, the call has no effect.

**2) ManualResetEvent:**

The ManualResetEvent Class in C# works exactly the same as the AutoResetEvent Class in C#. The one and the only difference between AutoResetEvent and ManualResetEvent in C# is that for each WaitOne method there should be a corresponding Set method in AutoResetEvent while for all the WaitOne methods, one Set method is enough to release in the case of ManualResetEvent.

Ref: 
* [Thread Synchronization in C# .Net made easy! | Lock | Monitor | Mutex | Semaphore](https://youtu.be/5Zv8fF-KPrE)
* [Thread Synchronization in C#](https://dotnettutorials.net/lesson/thread-synchronization-in-csharp/)
* [Lock](https://dotnettutorials.net/lesson/locking-in-multithreading/)
* [Monitor](https://dotnettutorials.net/lesson/multithreading-using-monitor/)
* [Mutex](https://dotnettutorials.net/lesson/mutex-in-multithreading/)
* [Semaphor](https://dotnettutorials.net/lesson/semaphore-in-multithreading/)
* [SemaphoreSlim](https://dotnettutorials.net/lesson/semaphoreslim-class-in-csharp/)
* [AutoResetEvent and ManualResetEvent](https://dotnettutorials.net/lesson/autoresetevent-and-manualresetevent-in-csharp/)
