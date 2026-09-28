namespace YapayZekaGUI
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            picCanvas = new PictureBox();
            btnPredict = new Button();
            btnClear = new Button();
            lblResult = new Button();
            ((System.ComponentModel.ISupportInitialize)picCanvas).BeginInit();
            SuspendLayout();
            // 
            // picCanvas
            // 
            picCanvas.BackColor = SystemColors.ControlText;
            picCanvas.Location = new Point(20, 20);
            picCanvas.Name = "picCanvas";
            picCanvas.Size = new Size(280, 280);
            picCanvas.TabIndex = 0;
            picCanvas.TabStop = false;
            picCanvas.MouseDown += picCanvas_MouseDown;
            picCanvas.MouseMove += picCanvas_MouseMove;
            picCanvas.MouseUp += picCanvas_MouseUp;
            // 
            // btnPredict
            // 
            btnPredict.Location = new Point(320, 20);
            btnPredict.Name = "btnPredict";
            btnPredict.Size = new Size(120, 40);
            btnPredict.TabIndex = 1;
            btnPredict.Text = "Predict";
            btnPredict.UseVisualStyleBackColor = true;
            btnPredict.Click += btnPredict_Click;
            // 
            // btnClear
            // 
            btnClear.Location = new Point(320, 70);
            btnClear.Name = "btnClear";
            btnClear.Size = new Size(120, 40);
            btnClear.TabIndex = 2;
            btnClear.Text = "Clear";
            btnClear.UseVisualStyleBackColor = true;
            btnClear.Click += btnClear_Click;
            // 
            // lblResult
            // 
            lblResult.AutoSize = true;
            lblResult.Font = new Font("Segoe UI", 16.2F, FontStyle.Bold, GraphicsUnit.Point, 162);
            lblResult.Location = new Point(320, 130);
            lblResult.Name = "lblResult";
            lblResult.RightToLeft = RightToLeft.No;
            lblResult.Size = new Size(188, 48);
            lblResult.TabIndex = 3;
            lblResult.Text = "Prediction: -";
            lblResult.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(lblResult);
            Controls.Add(btnClear);
            Controls.Add(btnPredict);
            Controls.Add(picCanvas);
            Name = "Form1";
            Text = "DigitRecognizer1.0";
            ((System.ComponentModel.ISupportInitialize)picCanvas).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private PictureBox picCanvas;
        private Button btnPredict;
        private Button btnClear;
        private Button lblResult;
    }
}
