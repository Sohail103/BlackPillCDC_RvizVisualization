import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/hdd/STM32/STM32Projects/BlackPillCDC/BlackPillCDC_RvizVisualization/install/serial_mpu_reader'
