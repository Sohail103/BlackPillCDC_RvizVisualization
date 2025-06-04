import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/hdd/stm32/stm32_projects/BlackPillCDC/BlackPillCDC_RvizVisualization/install/serial_mpu_reader'
