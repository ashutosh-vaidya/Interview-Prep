using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventsDemo
{
    public class EmailHelpercs
    {
        public void GenerateEmailId(object sender, User u)
        {
            u.UserEmail = u.UserName + "@eventsDemo.com";
            Console.WriteLine($"Email id {u.UserEmail} is generated for user {u.UserName} and welcome email is sent.");
        }

        public void GenerateEmailId()
        {
            Console.WriteLine("Email id is Generator.");
        }
    }
}
