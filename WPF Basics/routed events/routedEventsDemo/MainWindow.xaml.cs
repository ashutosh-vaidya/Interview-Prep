using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace routedEventsDemo
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

        private void OuterButton_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Outer Button is clicked...", "Information", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void InnerChangeTitleBtn_Click(object sender, RoutedEventArgs e)
        {
            this.Title = "Title changed by inner button"; 
            MessageBox.Show("Inner Button is clicked for Changing the title...", "Information", MessageBoxButton.OK, MessageBoxImage.Information);

        }

        private void InnerBubbleEventBtn_Click(Object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Inner Button is clicked for Bubble Event...", "Information", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void InnerTunnelEventBtn_PreviewMouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            MessageBox.Show("Inner Button is clicked for Tunnel Event...", "Information", MessageBoxButton.OK, MessageBoxImage.Information);

        }

        private void OuterButton_PreviewMouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            MessageBox.Show("Outer Button is clicked Tunneling ...", "Information", MessageBoxButton.OK, MessageBoxImage.Information);
        }
    }
}
