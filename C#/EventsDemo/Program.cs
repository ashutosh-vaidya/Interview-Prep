using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventsDemo
{
    internal class Program
    {
        ////Declare the delegate
        //public delegate void EventDelegte();

        ////Declare the event
        //public static EventDelegte EventHandler;

        public static void Main(string[] args)
        {
            EmailHelpercs email = new EmailHelpercs();
            AccessCardHelper card = new AccessCardHelper();
            DatabaseHelper db = new DatabaseHelper();

            //UserProcessor.UserProcessorEvent += email.GenerateEmailId;
            UserProcessor.UserProcessorEvent += card.GenerateAccessCard;
            UserProcessor.UserProcessorEvent += db.SaveToDatabase;

            UserProcessor.myEvent += email.GenerateEmailId;


            Console.WriteLine("1.Add New: For creating new user");
            Console.WriteLine("2.Exit: To end the program");

            while (true)
            {
                Console.WriteLine("Enter Command");
                var command = Console.ReadLine();
                if (command == "Exit")
                {
                    break;
                }
                else if (command == "Add New")
                {
                    Console.Write("\nEnter Name: ");
                    var name = Console.ReadLine();
                    Console.Write("\nEnter Id: ");
                    var id = int.Parse(Console.ReadLine());
                    Console.Write("\nEnter Role: ");
                    var role = Console.ReadLine();
                    Console.Write("Do you want to generate email id [Y/N]:");
                    var resonse = Console.ReadLine();

                    if (resonse == "Y")
                    {
                        UserProcessor.UserProcessorEvent -= email.GenerateEmailId;
                        UserProcessor.UserProcessorEvent += email.GenerateEmailId;
                    }
                    else
                    if (resonse == "N") {
                        UserProcessor.UserProcessorEvent -= email.GenerateEmailId;
                    }
                    UserProcessor.CreateUser(id, name, role);
                    UserProcessor.CreateUserUsingDelegate(id, name, role);
                }
                else
                {
                    Console.WriteLine("Invalid Command");
                }
            }
        }


        
        //public void RaiseEvent()
        //{
        //    //Raise the Event
        //    EventHandler?.Invoke();
        //}

    }
}
