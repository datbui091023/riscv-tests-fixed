import targets
import testlib

class myrtl_hart(targets.Hart):
    xlen = 64
    ram = 0x80000000
    ram_size = 0x1000000
    bad_address = 0xdeadbeef
    reset_vectors = [0x1000]
    misa = 0x8000000000141125  # hoặc misa đúng của bạn

class myrtl(targets.Target):
    harts = [myrtl_hart()]
    openocd_config_path = "myrtl.cfg"
    timeout_sec = 180
