using System;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Windows.Forms;

namespace YapayZekaGUI
{
    public partial class Form1 : Form
    {
        private bool isDrawing = false;
        private Point lastPoint;
        private Bitmap canvasBitmap;

        public Form1()
        {
            InitializeComponent();

            canvasBitmap = new Bitmap(picCanvas.Width, picCanvas.Height);
            using (Graphics g = Graphics.FromImage(canvasBitmap))
            {
                g.Clear(Color.Black);
            }
            picCanvas.Image = canvasBitmap;
        }

        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDrawing = true;
                lastPoint = e.Location;
            }
        }

        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                using (Graphics g = Graphics.FromImage(canvasBitmap))
                {
                    using (Pen pen = new Pen(Color.White, 18))
                    {
                        pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
                        pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;
                        g.DrawLine(pen, lastPoint, e.Location);
                    }
                }
                lastPoint = e.Location;
                picCanvas.Invalidate(); 
            }
        }

        private void picCanvas_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDrawing = false;
            }
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            using (Graphics g = Graphics.FromImage(canvasBitmap))
            {
                g.Clear(Color.Black);
            }
            picCanvas.Invalidate();
            lblResult.Text = "Prediction: -";
        }

        private void btnPredict_Click(object sender, EventArgs e)
        {
            try
            {
                string imagePath = Path.Combine(Application.StartupPath, "input.png");
                using (Bitmap resized = new Bitmap(28, 28))
                {
                    using (Graphics g = Graphics.FromImage(resized))
                    {
                        g.InterpolationMode = InterpolationMode.HighQualityBicubic;
                        g.DrawImage(canvasBitmap, 0, 0, 28, 28);
                    }
                    resized.Save(imagePath, ImageFormat.Png);
                }

                string pythonScript = Path.Combine(Application.StartupPath, "..\\..\\..\\..\\YapayZeka\\predict.py");

                ProcessStartInfo start = new ProcessStartInfo();
                start.FileName = "python";
                start.Arguments = $"\"{pythonScript}\" \"{imagePath}\"";
                start.UseShellExecute = false;
                start.RedirectStandardOutput = true;
                start.RedirectStandardError = true;
                start.CreateNoWindow = true;

                lblResult.Text = "Prediction: Thinking...";
                Application.DoEvents();

                using (Process process = Process.Start(start))
                {
                    string output = process.StandardOutput.ReadToEnd().Trim();
                    string error = process.StandardError.ReadToEnd().Trim();

                    if (!string.IsNullOrEmpty(error))
                    {
                        MessageBox.Show("Python Hatası:\n" + error);
                        lblResult.Text = "Prediction: Error!";
                    }
                    else if (!string.IsNullOrEmpty(output))
                    {
                        lblResult.Text = $"Prediction: {output}";
                    }
                    else
                    {
                        lblResult.Text = "Prediction: Empty!";
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("C# Hatası: " + ex.Message);
            }
        }
    }
}