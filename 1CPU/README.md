# Example of a 1-CPU bound process.

This python test is CPU-bound.  Because of Python GIL only one CPU is used.

# Linux on Atom C3558

## HTOP

This is what htop output looks like.  Note one of the four CPUs available is
maxed out.  Load average tells that no more than 1.5 CPUs are used.

```
htop -d 40 -u alex
```

```
  1  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   89.1%]   Tasks: 218, 833 thr; 2 running
  2  [||||||||||||||                                                         17.1%]   Load average: 1.15 1.36 1.13 
  3  [||||||||||||||||                                                       20.1%]   Uptime: 4 days, 22:31:28
  4  [|||||||||||||||                                                        18.2%]
  Mem[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||       3.16G/7.60G]
  Swp[                                                                    0K/7.87G]

  PID USER   PRI  NI  VIRT   RES   SHR S CPU% MEM%   TIME+  Command
30569 alex   20   0  120M  4584  2008 R 99.6  0.1 14:06.51 python test.py
28074 alex   20   0 3695M  353M 57844 S 34.3  4.5 11:30.33 /usr/bin/gnome-shell
28081 alex	 20   0 3695M  353M 57844 S  3.5  4.5  1:31.13 /usr/bin/gnome-shell
28083 alex	 20   0 3695M  353M 57844 S  2.7  4.5  1:32.44 /usr/bin/gnome-shell
28084 alex	 20   0 3695M  353M 57844 S  2.5  4.5  1:32.85 /usr/bin/gnome-shell
29321 alex	 20   0 1720M  132M 66464 S  2.2  1.7  0:28.64 /usr/share/code/code .
28082 alex	 20   0 3695M  353M 57844 S  2.0  4.5  1:31.36 /usr/bin/gnome-shell
28970 alex	 20   0  803M 31368 18456 S  1.0  0.4  0:03.28 /usr/libexec/gnome-terminal-server
31200 alex	 20   0  120M  3136  1484 R  0.7  0.0  0:00.16 htop -d 40

F1Help  F2Setup F3SearchF4FilterF5Tree  F6SortByF7Nice -F8Nice +F9Kill  F10Quit

```

# TOP

Here is an example of top output.  Note 100% CPU consumption.  Apparently 100% refers
to a single CPU and is not normalized across all the CPUs.  Load average same as in htop.

```                                                 
[alex@flattop ~]$ top -d 3 -u alex

top - 11:32:15 up 4 days, 22:47,  3 users,  load average: 1.62, 1.52, 1.43
Tasks: 343 total,   2 running, 341 sleeping,   0 stopped,   0 zombie
%Cpu(s): 31.9 us,  0.8 sy,  0.0 ni, 67.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  7972440 total,  2149072 free,  3111400 used,  2711968 buff/cache
KiB Swap:  8257532 total,  8257532 free,        0 used.  4373312 avail Mem 
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                 
30569 alex      20   0  123368   4584   2008 R 100.0  0.1  29:24.19 python                                                 
28074 alex      20   0 3784396 362332  57840 S  23.3  4.5  19:23.07 gnome-shell                                            
28970 alex      20   0  822660  31756  18460 S   0.7  0.4   0:05.06 gnome-terminal-                                        
31978 alex      20   0  162156   2528   1600 R   0.7  0.0   0:00.06 top                                                    
 9541 alex      20   0  779600  14636   9440 S   0.3  0.2   2:39.45 gsd-color                                              
 5977 alex      20   0  311820  95852  15920 S   0.0  1.2   9:31.61 Xvnc                                                   
 7943 alex      20   0  113176   1200   1024 S   0.0  0.0   0:00.00 xstartup                                               

```

# VMSTAT

This is what vmstat output looks like.  Usually there is just 1 runnable process.
Sometimes 2.

```
[alex@flattop ~]$ vmstat 3 10
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 2175960   2296 2698216    0    0     1     1   13   12  1  0 99  0  0
 1  0      0 2175324   2296 2698216    0    0     0     0 1357  898 29  0 70  0  0
 1  0      0 2175484   2296 2698216    0    0     0     0 1338  887 29  0 71  0  0
 1  0      0 2175324   2296 2698216    0    0     0     0 1359  924 29  1 71  0  0
 1  0      0 2175004   2296 2698216    0    0     0    12 1321  909 29  0 71  0  0
 1  0      0 2175764   2296 2698224    0    0     0    16 1654 1515 30  1 70  0  0
 2  0      0 2175888   2296 2698224    0    0     0     0 1359  972 29  0 71  0  0
 1  0      0 2175976   2296 2698224    0    0     0     0 1353 1028 29  1 70  0  0
 1  0      0 2175764   2296 2698224    0    0     0     0 1338  858 29  0 71  0  0
 1  0      0 2175764   2296 2698224    0    0     0     0 1379  968 29  1 70  0  0
```

# Windows on i7-8750H

## WMIC

```
C:\Users\asoko>wmic cpu get loadpercentage
LoadPercentage
2
```

## typeperf

```
C:\Users\asoko>typeperf "\Processor(_Total)\% Processor Time"

"(PDH-CSV 4.0)","\\L07A97UF\Processor(_Total)\% Processor Time"
"07/07/2019 13:36:25.480","9.220876"
"07/07/2019 13:36:26.495","9.105775"
"07/07/2019 13:36:27.503","10.956450"
"07/07/2019 13:36:28.516","9.049064"
"07/07/2019 13:36:29.533","10.180323"
"07/07/2019 13:36:30.543","9.291024"
"07/07/2019 13:36:31.560","9.528610"
"07/07/2019 13:36:32.567","8.230706"
"07/07/2019 13:36:33.581","8.628567"
"07/07/2019 13:36:34.592","9.879079"
"07/07/2019 13:36:35.609","8.671926"
"07/07/2019 13:36:36.612","8.460848"
"07/07/2019 13:36:37.625","9.102830"
"07/07/2019 13:36:38.633","10.256026"
"07/07/2019 13:36:39.636","9.196064"
"07/07/2019 13:36:40.651","8.607710"
"07/07/2019 13:36:41.655","9.748047"
"07/07/2019 13:36:42.658","15.476312"

The command completed successfully.
```

## TaskManager

Task manager barely registers this load.  Overall CPU consumption is indicated
as 6%.  Individual cores are barely loaded at all - at least none of them
approaches 100%.  They have intermittent spikes which I have trouble
attributing to anything.

## TOP Equivalent

[Script](https://superuser.com/questions/176624/linux-top-command-for-windows-powershell):
```
While(1) {  $p = get-counter '\Process(*)\% Processor Time'; cls; $p.CounterSamples | sort -des CookedValue | select -f 15 | ft -a}
```

Output:
```
Path                                                 InstanceName       CookedValue
----                                                 ------------       -----------
\\l07a97uf\process(_total)\% processor time          _total        1199.58538386979
\\l07a97uf\process(idle)\% processor time            idle          1088.71228035422
\\l07a97uf\process(python#2)\% processor time        python        100.093774007107
\\l07a97uf\process(dwm)\% processor time             dwm            3.0798084309879
\\l07a97uf\process(taskmgr)\% processor time         taskmgr        3.0798084309879
\\l07a97uf\process(ctfmon)\% processor time          ctfmon        1.53990421549395
\\l07a97uf\process(conhost#8)\% processor time       conhost       1.53990421549395
\\l07a97uf\process(system)\% processor time          system        1.53990421549395
\\l07a97uf\process(powermgr)\% processor time        powermgr                     0
\\l07a97uf\process(webcompanion)\% processor time    webcompanion                 0
\\l07a97uf\process(svchost#8)\% processor time       svchost                      0
\\l07a97uf\process(rundll32)\% processor time        rundll32                     0
\\l07a97uf\process(svchost#9)\% processor time       svchost                      0
\\l07a97uf\process(runtimebroker#2)\% processor time runtimebroker                0
\\l07a97uf\process(svchost#10)\% processor time      svchost                      0

```

