using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace Funzioni_bidimensionali
{
    public partial class Form1 : Form
    {
        double[,] data;
        public Form1()
        {
            InitializeComponent();
            int p = 2;
            data = new double[200, 200];
            for (int i = 0; i < data.GetLength(0); i++)
                for (int j = 0; j < data.GetLength(1); j++)
                {
                    data[i, j] = Math.Sin(Math.Sqrt(Math.Pow(i, p) + Math.Pow(j, p))) / Math.Sqrt(Math.Pow(i, p) + Math.Pow(j, p)+0.0001);
                }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            double interval = Interval(data);
            for (int i = 0; i < data.GetLength(0)-1; i++)
                for (int j = 0; j < data.GetLength(1)-1; j++)
                {
                    int px1 = i * Width / data.GetLength(0);
                    int py1 = j * Height / data.GetLength(1);
                    int pz1 = (int)(data[i, j] * Height / interval);
                    int ppx1 = px1 + py1 / 2;
                    int ppy1 = pz1 + py1 / 2;

                    int px2 = (i+1) * Width / data.GetLength(0);
                    int py2 = j * Height / data.GetLength(1);
                    int pz2 = (int)(data[i+1, j] * Height / interval);
                    int ppx2 = px2 + py2 / 2;
                    int ppy2 = pz2 + py2 / 2;
                    e.Graphics.DrawLine(Pens.Red, ppx1, Height/2 + ppy1, ppx2, Height/2 + ppy2);
                }
            for (int j = 0; j < data.GetLength(1) - 1; j++)
                for (int i = 0; i < data.GetLength(0)-1; i++)
                {
                    int px1 = i * Width / data.GetLength(0);
                    int py1 = j * Height / data.GetLength(1);
                    int pz1 = (int)(data[i, j] * Height / interval);
                    int ppx1 = px1 + py1 / 2;
                    int ppy1 = pz1 + py1 / 2;

                    int px2 = i * Width / data.GetLength(0);
                    int py2 = (j+1) * Height / data.GetLength(1);
                    int pz2 = (int)(data[i, j+1] * Height / interval);
                    int ppx2 = px2 + py2 / 2;
                    int ppy2 = pz2 + py2 / 2;
                    e.Graphics.DrawLine(Pens.Red, ppx1, Height/2 + ppy1, ppx2, Height/2 + ppy2);
                }
            Bitmap bmp = convertDataToBitmap(data);
            e.Graphics.DrawImage(bmp, Width-bmp.Width, 0);
            e.Graphics.DrawLine(Pens.Black, 1, 1, 1, Height);
            e.Graphics.DrawLine(Pens.Black, 0, Height / 2, Width, Height / 2);
        }

        private void pictureBox1_Resize(object sender, EventArgs e)
        {
            Invalidate(true);
        }
        double Interval(double[,] data)
        {
            double result;

            result = MaxMin(data)[0] - MaxMin(data)[1];
            return result;
        }
        double[] MaxMin(double[,] data)
        {
            double[] result = new double[2];
            double min, max;
            min = data[0, 0];
            max = data[0, 0];
            for (int i = 0; i < data.GetLength(0); i++)
                for (int j = 0; j < data.GetLength(1); j++)
                {
                    min = Math.Min(data[i, j], min);
                    max = Math.Max(data[i, j], max);
                }
            result[0] = min;
            result[1] = max;
            return result;
        }
        Bitmap convertDataToBitmap(double[,] data)
        {
            Bitmap bmp = new Bitmap(data.GetLength(0), data.GetLength(1));

            double[] maxMin = new double[2];
            maxMin = MaxMin(data);
            double difference = maxMin[1] - maxMin[0];

            for (int i = 0; i < data.GetLength(0); i++)
                for (int j = 0; j < data.GetLength(1); j++)
                {
                    int gray = (int)(255 * (data[i, j] - maxMin[0]) / difference);

                    bmp.SetPixel(i, j, Color.FromArgb(gray, gray, gray));
                }

            return bmp;
        }
    }
}
