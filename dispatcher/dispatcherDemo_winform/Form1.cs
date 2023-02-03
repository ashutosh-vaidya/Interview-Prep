namespace dispatcherDemo_winform
{
    public partial class Form1 : Form
    {
        //This Code throws the exception 
        //System.InvalidOperationException,
        //Message=Cross-thread operation not valid:
        //public Form1()
        //{
        //    InitializeComponent();
        //}

        //private void button1_Click(object sender, EventArgs e)
        //{
        //    //This Code throws the exception 
        //    //System.InvalidOperationException,
        //    //Message=Cross-thread operation not valid:
        //    Thread t = new Thread(new ThreadStart(setTextToTextBox));
        //    t.Start();
        //}

        //private void setTextToTextBox()
        //{
        //    textBox1.Text = "Setting the text on button click!";
        //}

        delegate void setTextCallbackDelegate(String text);
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Thread t = new Thread(new ThreadStart(setTextToTextBox));
            t.Start();
        }

        private void setTextToTextBox()
        {
            setTextCallBack("Setting the text on button click!");
        }

        private void setTextCallBack(string text)
        {
            if (this.textBox1.InvokeRequired)
            {
                setTextCallbackDelegate d = new setTextCallbackDelegate(setTextCallBack);
                this.Invoke(d, new object[] { text });
            } else
            {
                this.textBox1.Text = text;
            }
        }
    }
}