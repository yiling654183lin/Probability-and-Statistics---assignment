using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace RedioButtonsTest
{
    public partial class Radio_buttons_test_form : Form
    {
        private MessageBoxIcon iconType;
        private MessageBoxButtons buttonType; //之後就不必再作設定
        public Radio_buttons_test_form()
        {
            InitializeComponent();
        }
        private void buttonType_checkedChanged(object sender, EventArgs e)
        {
            if (sender == OKButton)
                buttonType = MessageBoxButtons.OK;
            else if (sender == OKCancelButton)
                buttonType = MessageBoxButtons.OKCancel;
        }

        private void displayButton_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show(
                "This is your custom messageBox",
                "Custom Message",
                buttonType,
                MessageBoxIcon.Information);
        }

        private void ExitButton_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show(
                "Are you sure you want to exit?",
                "Exit",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                Application.Exit();
            }
        }
    }
}
