**What is Dispatcher in WPF**

**Ans:** By default the .Net application along with WPF are based on STA (Single Threaded Apartment). Single threaded apartments contains only one (main) thread. 

As a result, every WPF element has thread affinity. This means that such an element should only be accessed from the thread that created it. Every element that needs thread affinity, therefore, eventually derives from the DispatcherObject class. This class includes a Dispatcher property that returns the Dispatcher object associated with the WPF element.

Dispatcher need to handle multithreading in WPF

**Problem:** If we create an application where we have a button and a textbox and on button click we are setting some text on the textbox. If no threading use then it works fine. But as soon as we use threading by creating a new thread and try to set the textbox text in that thread application gives an error. 

in winform it will throw,
> System.InvalidOperationException, Message=Cross-thread operation not valid:

in WPF it will throw,
> System.InvalidOperationException,   Message=The calling thread cannot access this object because a different thread owns it.

Problematic code,
```C#
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
            txtBox1.Text = "Setting this text using button click!";
        }
```

Solution:
```C#
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
```