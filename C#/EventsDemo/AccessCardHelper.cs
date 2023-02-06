using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventsDemo
{
    public class AccessCardHelper
    {
        public void GenerateAccessCard(object sender, User e)
        {
            Console.WriteLine($"An access card is generated for the user {e.UserName}");
        }
    }
}
