using System;
using System.IO;
using System.Diagnostics;
using System.Collections.Generic;

namespace win {
    public class shell {
        public static string exec(string command) {
            var p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            
            string eOut = null;
            p.ErrorDataReceived += new DataReceivedEventHandler((s, e) => {
                eOut += e.Data;
            });
            p.Start();
            p.StandardInput.WriteLine(@command);
            p.StandardInput.Flush();
            p.StandardInput.Close();
            eOut += p.StandardOutput.ReadToEnd();
            return eOut;
        }

        public static string execp(string command) {
            var p = new Process();
            p.StartInfo.FileName = "powershell.exe";
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            
            string eOut = null;
            p.ErrorDataReceived += new DataReceivedEventHandler((s, e) => {
                eOut += e.Data;
            });
            p.Start();
            p.StandardInput.WriteLine(@command);
            p.StandardInput.Flush();
            p.StandardInput.Close();
            eOut += p.StandardOutput.ReadToEnd();
            return eOut;
        }
    }
}