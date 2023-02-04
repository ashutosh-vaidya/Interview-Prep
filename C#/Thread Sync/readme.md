This repo contains the demo for the Thread Synchronization in C#.

Ref: [Thread Synchronization in C# .Net made easy! | Lock | Monitor | Mutex | Semaphore](https://youtu.be/5Zv8fF-KPrE)

**What is Thread Synchronization**

Data inconsistency occurs when more than one thread accesses a shared resource such as in-memory data (instance of class, class variables) and external objects (files, database) at the same time. For example, let's assume thread 1 is writing the data to a file, and at the same time thread 2 attempting to read that file. This will cause data inconstancy and the potential to read stale data. To avoid this, thread synchronization can be implemented.

Synchronization ensures that only one thread is accessing the shared resource at any given point and prevents the other thread access to it at the same time. The protected resource can be called a critical section and synchronization makes sure that only one thread can enter the critical section.

**Ways of Thread Synchronization**

1. Lock
2. Monitor
3. Manual Reset Event
4. Auto Reset Event
5. Mutex
6. Semaphore
7. Semaphore Slim
