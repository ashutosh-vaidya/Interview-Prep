using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventsDemo
{
    public static class UserProcessor
    {
        public static event EventHandler<User> UserProcessorEvent;

        public delegate void myEventDelegate();

        public static myEventDelegate myEvent;

        public static void CreateUser(int id, string name, string role)
        {
            User user = new User(id, name, role);
            Console.WriteLine($"User {user.UserName} with role {user.Role} is Created.");
            UserProcessorEvent?.Invoke(null, user);
        }

        public static void CreateUserUsingDelegate(int id, string name, string role)
        {
            User user = new User(id, name, role);
            Console.WriteLine($"User {user.UserName} with role {user.Role} is Created.");
            myEvent?.Invoke();
        }
    }
}
