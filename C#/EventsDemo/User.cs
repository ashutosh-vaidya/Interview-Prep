using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventsDemo
{
    public class User : EventArgs
    {
        public int UserId { get; set; }
        public string UserName { get; set; }
        public string Role { get; set; }
        public string UserEmail { get; set; }
        public User(int id, string name, string role)
        {
            this.UserId = id;
            this.UserName = name;
            this.Role = role;
        }
    }
}
