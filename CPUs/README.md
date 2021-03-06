# Example of a (Multiple) CPU bound process.

This python test is CPU-bound and takes advantage of all the available CPUs. 
Launch the test like this:

```
alex@rpi4:~/Projects/x-bound.examples/CPUs $ python3 ./test.py 
Calculating Fibonacci 100 using 3 CPUs
```

# Linux on Intel Atom C3558

Tested on a 4-core CPU with test occupying 3 of them - I left once CPU
available for the data collection activities.

## HTOP

This is what htop looks like.  Note 3 of the four CPUs available are maxed out.
Load average tells that 3 CPUs are used.  Also note runnable processes in the
S columns.

```
htop -d 40 -u alex
```

```
  1  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%]   Tasks: 221, 833 thr; 4 running
  2  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%]   Load average: 3.05 1.84 1.54 
  3  [||||||||||||||||||||||||||||||||||||||||||||                           55.6%]   Uptime: 4 days, 23:17:54
  4  [|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        81.6%]
  Mem[|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    3.42G/7.60G]
  Swp[                                                                    0K/7.87G]

  PID USER   PRI  NI  VIRT   RES   SHR S CPU% MEM%   TIME+  Command
  718 alex   20   0  194M  7764  1256 R 99.6  0.1  0:34.01 python3 test.py
  716 alex	 20   0  194M  7752  1252 R 98.4  0.1  0:34.12 python3 test.py
  717 alex	 20   0  194M  7760  1252 R 98.1  0.1  0:34.01 python3 test.py
28074 alex	 20   0 3703M  361M 57844 S 19.0  4.6 35:32.54 /usr/bin/gnome-shell
29490 alex	 20   0 2933M  395M  102M S  1.5  5.1  2:56.64 /usr/lib64/firefox/firefox https://code.visualstudio.com/
28081 alex	 20   0 3703M  361M 57844 S  1.5  4.6  4:38.26 /usr/bin/gnome-shell
28084 alex	 20   0 3703M  361M 57844 S  1.2  4.6  4:46.54 /usr/bin/gnome-shell
28082 alex	 20   0 3703M  361M 57844 S  1.2  4.6  4:42.42 /usr/bin/gnome-shell
28083 alex	 20   0 3703M  361M 57844 S  1.0  4.6  4:45.77 /usr/bin/gnome-shell
28970 alex	 20   0  803M 32452 18468 S  1.0  0.4  0:08.27 /usr/libexec/gnome-terminal-server
  722 alex	 20   0  120M  3160  1492 R  0.7  0.0  0:00.31 htop -d 40 -u alex
32309 alex	 20   0 1810M  160M 51036 S  0.7  2.1  0:33.76 /usr/lib64/firefox/firefox -contentproc -childID 13 -isForBrowser -boolPrefs 36:1|262:1|303:0| -stringPrefs 28
  715 alex	 20   0  410M 10832  4300 S  0.2  0.1  0:00.20 python3 test.py
29508 alex	 20   0 2933M  395M  102M S  0.2  5.1  0:04.25 /usr/lib64/firefox/firefox https://code.visualstudio.com/
28089 alex	 20   0 3703M  361M 57844 S  0.2  4.6  0:00.15 /usr/bin/gnome-shell
 8222 alex	 20   0 3615M  277M 58200 S  0.0  3.6 57:18.15 /usr/bin/gnome-shell
29373 alex	 20   0 2053M  328M 62788 S  0.0  4.2  4:22.92 /usr/share/code/code --type=renderer --no-sandbox --service-pipe-token=B152EBE42897F6783A22C92048E72640 --lang
 9549 alex	 20   0  452M  6128  3224 S  0.0  0.1  0:51.72 /usr/libexec/gsd-housekeeping
28277 alex	 20   0  452M  4084  3224 S  0.0  0.1  0:00.31 /usr/libexec/gsd-housekeeping
29550 alex	 20   0 2933M  395M  102M S  0.0  5.1  0:01.26 /usr/lib64/firefox/firefox https://code.visualstudio.com/
32312 alex	 20   0 1810M  160M 51036 S  0.0  2.1  0:00.95 /usr/lib64/firefox/firefox -contentproc -childID 13 -isForBrowser -boolPrefs 36:1|262:1|303:0| -stringPrefs 28
29506 alex	 20   0 2933M  395M  102M S  0.0  5.1  0:02.86 /usr/lib64/firefox/firefox https://code.visualstudio.com/
  719 alex	 20   0  410M 10832  4300 S  0.0  0.1  0:00.01 python3 test.py
 9541 alex	 20   0  761M 14636  9440 S  0.0  0.2  2:40.42 /usr/libexec/gsd-color
  491 alex	 20   0  114M  3688  1808 S  0.0  0.0  0:00.11 bash
  720 alex	 20   0  410M 10832  4300 S  0.0  0.1  0:00.00 python3 test.py
F1Help  F2Setup F3SearchF4FilterF5Tree  F6SortByF7Nice -F8Nice +F9Kill  F10Quit
```

# TOP

Here is an example of top output. Note load average and which processes are runnable.

```                                                 
top - 12:07:32 up 4 days, 23:22,  4 users,  load average: 4.35, 3.49, 2.31
Tasks: 344 total,   4 running, 340 sleeping,   0 stopped,   0 zombie
%Cpu(s): 83.1 us,  0.7 sy,  0.0 ni, 16.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  7972440 total,  1785904 free,  3425672 used,  2760864 buff/cache
KiB Swap:  8257532 total,  8257532 free,        0 used.  4024740 avail Mem 
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                
  716 alex      20   0  199400   7752   1252 R  99.0  0.1   4:37.47 python3                                                                                               
  717 alex      20   0  199400   7760   1252 R  97.7  0.1   4:38.09 python3                                                                                                
  718 alex      20   0  199400   7764   1256 R  97.0  0.1   4:37.60 python3                                                                                                
28074 alex      20   0 3792340 370260  57844 S  22.2  4.6  37:41.68 gnome-shell                                                                                            
29490 alex      20   0 3017656 438500 105068 S   1.3  5.5   3:00.52 firefox                                                                                                
28970 alex      20   0  823316  32456  18468 S   1.0  0.4   0:08.77 gnome-terminal-                                                                                        
32309 alex      20   0 1857232 167412  51036 S   0.7  2.1   0:35.84 Web Content                                                                                            
29373 alex      20   0 2110056 346972  65368 S   0.3  4.4   4:42.22 code                                                                                                   
  491 alex      20   0  116884   3688   1808 S   0.0  0.0   0:00.11 bash                                                                                                   
  715 alex      20   0  420340  10832   4300 S   0.0  0.1   0:00.40 python3                                                                                                
  806 alex      20   0  162156   2528   1600 R   0.0  0.0   0:00.07 top                                                                                                    
 5977 alex      20   0  311820  95852  15920 S   0.0  1.2   9:31.63 Xvnc                                                                                                   
 7943 alex      20   0  113176   1200   1024 S   0.0  0.0   0:00.00 xstartup                                                                                               
 7944 alex      20   0  745092   9396   6604 S   0.0  0.1   0:03.83 gnome-session-b                                                                                        
```

# VMSTAT

This is what vmstat output looks like.  Thre are always at least 3 runnable processes.

```
[alex@flattop ~]$ vmstat 3 10
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 6  0      0 1711556   2296 2759108    0    0     1     1   18   18  1  0 99  0  0
 5  0      0 1711448   2296 2759108    0    0     0     4 3431 1323 80  1 20  0  0
 5  0      0 1711200   2296 2759108    0    0     0    12 3399 1175 80  0 19  0  0
 5  0      0 1711068   2296 2759108    0    0     0     0 3400 1239 80  0 19  0  0
 3  0      0 1711012   2296 2759112    0    0     0     0 3397 1227 79  0 20  0  0
 3  0      0 1711012   2296 2759112    0    0     0     0 3443 1266 80  1 20  0  0
 3  0      0 1710516   2296 2759112    0    0     0     0 3424 1389 80  1 20  0  0
 3  0      0 1710036   2296 2759112    0    0     0     5 3454 1335 80  0 19  0  0
 3  0      0 1710036   2296 2759112    0    0     0     0 3353 1085 79  0 20  0  0
 3  0      0 1709788   2296 2759112    0    0     0    22 3444 1304 80  1 19  0  0

```
# Windows on Intel i7-8750H

6-core CPU.  cpus were set to 5 in test.py, thus 5 cores were used with the
last one left to be occupied by data collection.

## WMIC
```
C:\Users\asoko>wmic cpu get loadpercentage
LoadPercentage
36
```
## typeperf

```
PS C:\Users\asoko> typeperf "\Processor(_Total)\% Processor Time"

"(PDH-CSV 4.0)","\\L07A97UF\Processor(_Total)\% Processor Time"
"07/07/2019 14:47:14.544","51.921818"
"07/07/2019 14:47:15.554","54.011756"
"07/07/2019 14:47:16.566","50.478327"
"07/07/2019 14:47:17.577","51.956787"
"07/07/2019 14:47:18.590","51.390368"
"07/07/2019 14:47:19.598","50.796915"
"07/07/2019 14:47:20.610","51.234235"
"07/07/2019 14:47:21.623","54.735907"
"07/07/2019 14:47:22.631","53.907028"
"07/07/2019 14:47:23.637","55.453363"
"07/07/2019 14:47:24.651","50.718762"
"07/07/2019 14:47:25.654","51.031970"
"07/07/2019 14:47:26.670","51.954035"
"07/07/2019 14:47:27.677","50.980500"
"07/07/2019 14:47:28.683","51.875846"
"07/07/2019 14:47:29.689","51.301220"
"07/07/2019 14:47:30.701","52.268881"
"07/07/2019 14:47:31.705","53.058014"
"07/07/2019 14:47:32.710","51.278898"
"07/07/2019 14:47:33.712","52.083205"
"07/07/2019 14:47:34.715","52.184985"
"07/07/2019 14:47:35.731","50.809668"
"07/07/2019 14:47:36.734","51.051892"
"07/07/2019 14:47:37.745","51.058458"
"07/07/2019 14:47:38.746","50.815242"
"07/07/2019 14:47:39.761","52.284972"
```

## TaskManager

Overall CPU consumption is steady at 34%, similar to the result of
```wmic cpu get loadpercentage```.
Load is equally spread between all the 12 logical cores with significant spikes.

## TOP Equivalent

[Script](https://superuser.com/questions/176624/linux-top-command-for-windows-powershell):
```
While(1) {  $p = get-counter '\Process(*)\% Processor Time'; cls; $p.CounterSamples | sort -des CookedValue | select -f 15 | ft -a}
```

Output:
```
Path                                                       InstanceName               CookedValue
----                                                       ------------               -----------
\\l07a97uf\process(_total)\% processor time                _total                1208.64354665856
\\l07a97uf\process(idle)\% processor time                  idle                  594.210855628788
\\l07a97uf\process(python#6)\% processor time              python                101.109177004899
\\l07a97uf\process(python#1)\% processor time              python                101.109177004899
\\l07a97uf\process(python#5)\% processor time              python                101.109177004899
\\l07a97uf\process(python#8)\% processor time              python                101.109177004899
\\l07a97uf\process(python#9)\% processor time              python                101.109177004899
\\l07a97uf\process(python#7)\% processor time              python                97.9981254047478
\\l07a97uf\process(dwm)\% processor time                   dwm                   4.66657740022609
\\l07a97uf\process(taskmgr)\% processor time               taskmgr               4.66657740022609
\\l07a97uf\process(system)\% processor time                system                1.55552580007536
\\l07a97uf\process(securityhealthsystray)\% processor time securityhealthsystray                0
\\l07a97uf\process(igfxext)\% processor time               igfxext                              0
\\l07a97uf\process(securityhealthservice)\% processor time securityhealthservice                0
\\l07a97uf\process(rundll32)\% processor time              rundll32                             0
```

This is most close to what I would expect.  There are six python processes
consuming 100% of CPU time.  I undertand 5 workers, but why the 6th?