using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics; 

using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;


//파이선을 실행하기 위해 추가
using IronPython;
using IronPython.Hosting;
using IronPython.Runtime;
using IronPython.Modules;

namespace DemoWin
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            var engine = IronPython.Hosting.Python.CreateEngine();


            var scope = engine.CreateScope();

            try
            {
                //파이선 프로그램 파일 실행.
                var source = engine.CreateScriptSourceFromFile("c:\\work\\simple.py");
                source.Execute(scope);

                // call def HelloWorld() :
                var Fnhelloworld = scope.GetVariable<Func<object>>("HelloWorld");
                Console.WriteLine(Fnhelloworld());

                // call def HelloWorld2(data) :
                var Fnhelloworld2 = scope.GetVariable<Func<object, object>>("HelloWorld2");
                Debug.WriteLine(Fnhelloworld2("HelloWorld 2 "));

                // call def ListTest() :
                var FnListTest = scope.GetVariable<Func<object>>("ListTest");

                IronPython.Runtime.List r = (IronPython.Runtime.List)FnListTest();

                foreach (string data in r)
                {
                    Debug.WriteLine("result: {0}", data);
                }

                // call class MyClass
                var myClass = scope.GetVariable<Func<object, object>>("MyClass");
                var myInstance = myClass("hello");

                Debug.WriteLine(engine.Operations.GetMember(myInstance, "value"));

            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.Message);
            }
            
        }
    }
}
