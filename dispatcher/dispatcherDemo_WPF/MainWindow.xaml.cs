using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace dispatcherDemo_WPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Thread t = new Thread(new ThreadStart(setText));
            t.Start();
        }

        private void setText()
        {
            this.Dispatcher.Invoke(new Action(() => { txtBox1.Text = "Setting this text using button click!"; }));
        }

        //This Code throws the exception 
        //System.InvalidOperationException,
        //Message=The calling thread cannot access this object because a different thread owns it.

        //public MainWindow()
        //{
        //    InitializeComponent();
        //}

        //private void Button_Click(object sender, RoutedEventArgs e)
        //{
        //    Thread t = new Thread(new ThreadStart(setText));
        //    t.Start();
        //}

        //private void setText()
        //{
        //    txtBox1.Text = "Setting this text using button click!";
        //}
    }
}
