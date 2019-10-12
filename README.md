# Resource-bound Apps

Here are some examples of resource-bound apps and how to identify those using
mostly command line utilities.  On Linux and Windows.

## Examples by Resource

[1-cpu-bound](./1CPU)

[cpu-bound](./CPUs)

ram-bound

[io-bound](./IO)

# Tested Configurations

| Param | RPi4 | Tiny Server | Workstation Laptop |
|-------|------|-------------|--------------------|
| CPU | [Broadcom BCM2711](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/) | [Intel Atom C3558](https://ark.intel.com/content/www/us/en/ark/products/97937/intel-atom-processor-c3558-8m-cache-up-to-2-20-ghz.html) | [Intel i7-8750H](https://ark.intel.com/content/www/us/en/ark/products/134906/intel-core-i7-8750h-processor-9m-cache-up-to-4-10-ghz.html) |
| Cores | 4/4 | 4/4   | 6/12    |
| RAM (GB)  | 4 | 8 | 16  |
| OS    | Raspbian 10 buster | CentOS 7.6.1810 | Windows 10 |
| OS Build | 4.19.75-v7l+ #1270 SMP Tue Sep 24 18:51:41 BST 2019 armv7l GNU/Linux | 3.10.0-957.21.3.el7.x86_64 | 10.0.18362 |
| Python | Python 3.7.3 (default, Apr  3 2019, 05:39:12)  [GCC 8.2.0] | v3.6.8, May  2 2019, 20:40:44, GCC 4.8.5 20150623 (Red Hat 4.8.5-36)  | v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05, MSC v.1916 64 bit AMD64 |
