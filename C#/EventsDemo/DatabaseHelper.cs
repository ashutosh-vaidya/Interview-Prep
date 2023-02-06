using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventsDemo
{
    public class DatabaseHelper
    {
        public void SaveToDatabase(object sender, User e)
        {
            Console.WriteLine($"Data for User {e.UserName} is saved to database");
        }
    }
}
