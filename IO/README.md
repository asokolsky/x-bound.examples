# Example of an IO-bound process.

Open test.py and specify a folder for tests, e.g. the one on a USB2 flash disk.
To launch the test on RPi4 I used:
```
alex@rpi4:~/Projects/x-bound.examples/IO $ sudo python3 ./test.py 
[sudo] password for alex: 
Writing...
Reading & writing...
Removing /boot/test.me ...
Removing /boot/test-copy.me ...
```
# Linux on RPi4

## iotop

iotop does a good job of showing the processes causing the IO.

```
Total DISK READ:         0.00 B/s | Total DISK WRITE:         8.04 M/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
19048 be/4 root        0.00 B/s    8.04 M/s  0.00 % 62.21 % python3 ./test.py
    1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % init splash
    2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
    3 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_gp]
    4 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_par_gp]
    8 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [mm_percpu_wq]
    9 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/0]
   10 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_sched]
   11 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_bh]
   12 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [migration/0]
   13 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [cpuhp/0]
   14 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [cpuhp/1]
   15 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [migration/1]
   16 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/1]
   19 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [cpuhp/2]
```

## VMSTAT

Here is an interesting read:
https://www.slashroot.in/linux-system-io-monitoring

Indeed notice the wa column:

```
alex@rpi4:~/Projects $ vmstat 3 10
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 2375652  51560 865000    0    0    13   165  136  185  6  2 91  1  0
 0  1      0 2405400  51560 920740    0    0     0 20744  527  746  0  6 78 16  0
 0  2      0 2344392  51568 961380    0    0     0 18860  436  547  0  4 66 30  0
 1  1      0 2321016  51568 886332    0    0     0 15364  435  506  0  6 53 41  0
 0  2      0 2290236  51568 946880    0    0     0  8329  431  490  0  7 73 20  0
 0  2      0 2445180  51568 887084    0    0     0 14664  489  654  0  7 71 22  0
 0  2      0 2375608  51568 929544    0    0     0 23698  473  569  0  3 57 40  0
 1  1      0 2332588  51568 975316    0    0     0 15972  446  533  1  4 56 38  0
 1  0      0 2311660  51568 925588    0    0     0  6911  479  651  1  8 67 24  0
 0  1      0 2255668  51576 972932    0    0     0 17503  409  575  0  4 64 31  0
```

## SYSSTAT

https://www.slashroot.in/examples-using-sar-command-system-monitoring-linux
https://www.tecmint.com/sysstat-commands-to-monitor-linux/

### mpstat

Clearly indicates high iowait when IO stress is running:

```
alex@rpi4:~/Projects $ mpstat 1 10
Linux 4.19.75-v7l+ (rpi4) 	10/08/2019 	_armv7l_	(4 CPU)

07:56:00 PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
07:56:01 PM  all    1.07    0.00    4.53   17.87    0.00    0.00    0.00    0.00    0.00   76.53
07:56:02 PM  all    0.27    0.00    3.76   18.82    0.00    0.00    0.00    0.00    0.00   77.15
07:56:03 PM  all    0.52    0.00    4.99   17.85    0.00    0.00    0.00    0.00    0.00   76.64
07:56:04 PM  all    0.79    0.00    6.88   29.63    0.00    0.00    0.00    0.00    0.00   62.70
07:56:05 PM  all    0.27    0.00    4.58   42.59    0.00    0.00    0.00    0.00    0.00   52.56
07:56:06 PM  all    0.27    0.00    1.33   45.33    0.00    0.00    0.00    0.00    0.00   53.07
07:56:07 PM  all    0.27    0.00    2.16   44.74    0.00    0.00    0.00    0.00    0.00   52.83
07:56:08 PM  all    1.56    0.00   11.95   35.84    0.00    0.00    0.00    0.00    0.00   50.65
07:56:09 PM  all    0.25    0.00    4.26   44.11    0.00    0.00    0.00    0.00    0.00   51.38
07:56:10 PM  all    2.40    0.00    9.60   11.73    0.00    0.00    0.00    0.00    0.00   76.27
Average:     all    0.77    0.00    5.42   30.91    0.00    0.00    0.00    0.00    0.00   62.90

```
### iostat

[iostat](https://www.computerhope.com/unix/iostat.htm) does an awesome job of
pinpointing an IO bottleneck:

```
alex@rpi4:~/Projects $ iostat -x 1 10
Linux 4.19.75-v7l+ (rpi4) 	10/08/2019 	_armv7l_	(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           6.22    0.02    1.79    1.51    0.00   90.46

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
mmcblk0          0.07    2.01      1.97    826.82     0.42    41.35  86.37  95.37    2.33 3096.20   0.15    29.81   411.88  27.76   5.76
sda              1.97    1.66     44.37    157.43     0.01     1.48   0.63  47.13    1.68   14.17   0.02    22.51    94.62   0.58   0.21

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.79    0.00    5.53   41.84    0.00   51.84

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
mmcblk0          0.00   33.00      0.00  16896.00     0.00     0.00   0.00   0.00    0.00 2931.67   2.67     0.00   512.00  30.00  99.00
sda              0.00    2.00      0.00     16.00     0.00     2.00   0.00  50.00    0.00    1.50   0.00     0.00     8.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.26    0.00    7.81   36.72    0.00   55.21

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
mmcblk0          0.00   32.00      0.00  16384.00     0.00     0.00   0.00   0.00    0.00 2442.97   1.96     0.00   512.00  30.63  98.00
sda              0.00    0.00      0.00      0.00     0.00     0.00   0.00   0.00    0.00    0.00   0.00     0.00     0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           2.03    0.00   19.80   28.68    0.00   49.49

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
mmcblk0          0.00   35.00      0.00  17920.00     0.00     0.00   0.00   0.00    0.00 2469.03   1.98     0.00   512.00  28.29  99.00
sda              0.00    3.00      0.00     72.00     0.00     7.00   0.00  70.00    0.00    1.33   0.00     0.00    24.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.53    0.00    2.93   41.76    0.00   54.79

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
mmcblk0          0.00   33.00      0.00  16896.00     0.00     7.00   0.00  17.50    0.00 2466.24   2.23     0.00   512.00  30.30 100.00
sda              0.00    0.00      0.00      0.00     0.00     0.00   0.00   0.00    0.00    0.00   0.00     0.00     0.00   0.00   0.00
```

Notice above that the device mmcblk0 (my SD card) is 100% utilized.  Also note
the fields %iowait and aqu-sz.

# Linux Laptop

From https://access.redhat.com/solutions/1160343

A large file (such as an ISO file) will be read and written to /dev/null using dd.

```
alex@latitude:~/$ dd if=bigfile.mkv of=/dev/null bs=1M
1263+1 records in
1263+1 records out
1324670521 bytes (1.3 GB, 1.2 GiB) copied, 3.16056 s, 419 MB/s
```

Thus creating an observable bytes-in load:

```
alex@latitude:~$ vmstat -w 1
procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 2  0        90144       192612      2035288     10866428    0   11   178   864  662  397  12   5  83   0   0
 0  0        90144       197624      2035288     10860580    0    0     0     0 1530 3305   6   2  92   0   0
 0  0        90144       187816      2035320     10870248    0    0     0  1016 1897 3293   6   2  91   0   0
 0  0        90144       185556      2035320     10872864    0    0     0     0 1082 1972   4   2  94   0   0
 0  0        90144       184548      2035320     10872064    0    0     0     0  812 1362   2   8  90   0   0
 0  0        90144       184548      2035320     10871360    0    0     0     0  536  963   1   1  97   0   0
 0  0        90144       188832      2035320     10865824    0    0     0     0  543  942   2   0  98   0   0
 1  0        90144       189588      2035360     10866588    0    0     0     0  589  952   2   1  98   0   0
 1  0        90144       204540      2035360     10850844    0    0     0     0 1290 2766   4   2  94   0   0
 0  0        90144       199164      2035360     10855940    0    0     0     0 1329 2780   4   2  94   0   0
 0  0        90144       199416      2035360     10855932    0    0     0     0  585 1073   2   1  98   0   0
 2  0        93216       206448      2032648     10853460    0 3120 138244  3120 1634 3003   1   5  90   4   0
 0  1        93472       209176      2023892     10858656  136 9072 416904  9072 3559 6397   1  15  79   4   0
 1  1        95520       187212      2015764     10884536    0 10832 422400 10832 3236 6245   8  18  66   8   0
 0  0       105248       207124      2010384     10866920  116 20020 316332 20020 5835 11886   4  15  70  11   0
 1  0        94240       204936      2010392     10878804  308    0   308   228 1528 3216   6   4  90   0   0
 0  0        94240       204068      2010392     10879280    0    0     0     0  815 1894   3   2  96   0   0
 0  0        94240       206840      2010392     10876724    0    0     0     0  554  892   2   1  97   0   0
 0  0        94240       206336      2010392     10875764    0    0     0     0  670 1624   3   2  96   0   0
```

Reversing the direction of IO:

```
alex@latitude:~$ dd if=/dev/zero of=500MBfile bs=1M count=500 oflag=dsync
500+0 records in
500+0 records out
524288000 bytes (524 MB, 500 MiB) copied, 4.9321 s, 106 MB/s
```

Also makes it observable with vmstat: 

```
alex@latitude:~$ vmstat -w 1
procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 0  0        93984       182980      2006880     10914204    0   12   205   849  648  400  12   4  84   0   0
 0  0        93984       189252      2006888     10908472    0    0     0    32 1506 2950   6   2  93   0   0
 0  0        93984       182152      2006888     10917032    0    0     0     0 1820 3501   8   1  91   0   0
 0  0        93984       182208      2006888     10917160    0    0     0     0  515  876   1   1  99   0   0
 0  1        93984       693192      2007036     10404688    0    0     0 19896  896 1711   2   4  92   3   0
 1  1        93984       584736      2007856     10512056    0    0     8 105872 2082 6235   4   6  76  14   0
 0  1        93984       474152      2008680     10622460    0    0     8 106896 2685 8056   6   9  71  14   0
 1  1        93984       365300      2009508     10728840    0    0     4 107124 2466 9942   6   9  72  13   0
 1  0        93984       263740      2010316     10829944    0    0     4 105848 2248 9717   4  10  73  12   0
 1  0        93984       223616      2010268     10870420    0    0     0 78600 1607 5865   2   7  83   8   0
 1  0        93984       229496      2010268     10864440    0    0     0     0  863 1331   2   1  97   0   0
 0  0        93984       232352      2010276     10860348    0    0     0    36  718 1123   2   1  97   0   0
```

# Windows on i7-8750H

Way too fast to notice anything...

