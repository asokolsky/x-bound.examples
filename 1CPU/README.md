# Example of a 1-CPU bound process.

This python test is CPU-bound.  Because of Python GIL only one CPU is used.
Launch the test like this:

```
alex@rpi4:~/Projects/x-bound.examples/1CPU $ python3 ./test.py 
Calculating Fibonacci 100
```

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

# Variations on System Load

Taken from https://access.redhat.com/solutions/1160343

Using /dev/random also creates CPU load:

```
alex@latitude:~/Projects/x-bound.examples$ dd if=/dev/urandom of=500MBfile bs=1M count=5000
5000+0 records in
5000+0 records out
5242880000 bytes (5.2 GB, 4.9 GiB) copied, 30.8968 s, 170 MB/s
```

The impact of the above can be observed with vmstat:

```
alex@latitude:~$ vmstat -w 1
procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 0  0         6176       902772      2231216      9975888    0    3   168   373  725  375  13   5  82   0   0
 0  0         6176       901252      2231216      9977860    0    0     0     0  987 1649   2   1  96   0   0
 2  0         6176       929168      2231216      9951452    0    0     0     0 1358 2128   4   2  93   0   0
 1  0         6176      1079348      2231216      9801412    0    0     0     0  993 1096   1  28  71   0   0
 1  0         6176       898496      2231228      9982344    0    0     0    48 1694 1706   2  26  73   0   0
 1  0         6176       709976      2231228     10170092    0    0     0     0 1617 1982   3  26  71   0   0
 1  0         6176       522828      2231228     10357816    0    0     0     0 1032 1110   0  29  70   0   0
 1  0         6176       335820      2231236     10543648    0    0     0    36 1238 1216   1  26  73   0   0
 2  0        11808       189716      2231112     10682852    0 5268     0 119996 2688 4421   0  30  62   8   0
 1  1        20768       152892      2230572     10712664    0 9120     4 142240 3293 4873   0  31  62   7   0
 2  1        41504       141060      2230056     10709620    0 20584     0 421992 2163 2071   1  29  42  29   0
 1  1        49184       167492      2226268     10681076    0 7816     0 414404 2205 4305   1  30  43  26   0
 1  1        60192       175288      2225272     10666072    0 11036     0 417812 2383 2923   1  28  42  29   0
 1  1        62240       153376      2223848     10686560    0 1856     0 423480 2223 2394   1  29  45  24   0
 1  0        62752       171932      2219036     10671676    0 8848     0 92912 3449 5434   1  28  67   5   0
 1  0        63264       161436      2216104     10686392   48 8780    48  8780 3349 5176   1  28  71   0   0
 1  0        63776       150200      2212944     10703072    0  588     0   716 1492 1300   1  33  67   0   0
 1  0        64544       156320      2209072     10701188  196 8892   196  8932 3408 5602   0  28  71   0   0
 1  0        65056       163212      2205112     10696832  188 8824   188  8824 3385 5492   0  29  71   0   0
 1  1        65568       159520      2201100     10707992  168 8704   168 75216 3474 5403   0  30  67   3   0
 2  1        66080       149560      2199324     10720600    0  520    16 210172 1553 1297   0  27  61  12   0
procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 1  0        66848       152956      2195044     10720376    0 8868     4 162980 2706 3735   1  27  63   9   0
 1  0        67360       151564      2189732     10727900    0  588     8 144000 1489 1688   1  25  66   9   0
 1  0        68128       153968      2183868     10730900    0 8820    12 152180 3438 5364   1  27  64   8   0
 1  1        68640       150664      2178488     10744484    0 8748     8 207432 3487 5318   0  28  57  15   0
 1  1        69408       154292      2172452     10746468  188 8796   204 375680 2369 2704   0  29  46  25   0
 2  1        70176       154348      2166736     10752144  328 8900   336 362912 3261 4884   1  28  40  31   0
 2  0        70432       156292      2161048     10753724    0  556    44 385724 2550 5443   2  30  47  21   0
 1  1        71200       158380      2155624     10760400  272 8744   288 351568 3579 5587   1  25  44  31   0
 1  0        71712       159904      2149280     10764600    0  576     8 248600 2015 2191   1  27  62  11   0
 1  0        72224       151660      2144364     10778172  164 8900   164  8900 3373 5180   0  27  73   0   0
 1  0        72736       154536      2140396     10779916    0  576     0   576 1434 1226   1  29  70   0   0
 0  1        72992       156044      2137676     10781004    0  312     8 171384 1349 2469   1  18  75   6   0
 0  0        72992       156952      2137688     10781036    0    0    12 368640 1215 1112   2   4  83  11   0
 0  0        72992       153516      2137688     10784196    0    0     0     0  528  863   2   1  98   0   0
 0  0        72992       155028      2137688     10781124    0    0     0     0  488  932   2   1  98   0   0

```

The above demonstrates:

* increased up to 30% CPU system load;
* increased CPU load spent on IO;
* increased IO output;
* swapping out

Also note how first CPU load increased with IO increase being delayed.

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
