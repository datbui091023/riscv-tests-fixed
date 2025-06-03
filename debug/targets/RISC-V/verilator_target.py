import targets
import testlib
import os

class verilator_hart(targets.Hart):
    xlen = 32
    ram = 0x1C000000
    ram_size = 0x100000
    bad_address = ram - 8
    instruction_hardware_breakpoint_count = 2
    reset_vectors = [0x1000]
    link_script_path = "spike32.lds"
    misa = 0x40001104  # RV32IMC, cập nhật đúng giá trị của bạn nếu cần

class verilator_target(targets.Target):
    harts = [verilator_hart()]
    openocd_config_path = "dm_debug.cfg"
    timeout_sec = 180

    def create(self):
         return testlib.Openocd(server_cmd=f"openocd  -f {self.openocd_config_path}")
    # #     return testlib.Openocd(server_cmd=(
    # #     "openocd --command 'gdb_port 0; tcl_port 0; telnet_port disabled'"
    # #     f" -f {self.openocd_config_path}"
    # # ))
    #     #return testlib.Openocd(config = self.openocd_config_path)
    #     # os.environ["REMOTE_BITBANG_HOST"] = "localhost"
    #     # os.environ["REMOTE_BITBANG_PORT"] = "9999"
    #     # return testlib.Openocd(
    #     #     config=self.openocd_config_path,
    #     #     server_cmd=None,
    #     #     freertos=False,
    #     #     debug_openocd=False
    #     # )    
    #     #return testlib.Openocd(self)
    #     #return testlib.Openocd(server_cmd=f"openocd -c 'gdb port 3333' -c 'tcl port 0' -c 'telnet port disabled' -f {self.openocd_config_path}")
    #     #return testlib.Openocd(config = self.openocd_config_path)    
    #     return testlib.Openocd(server_cmd=f"openocd -f {self.openocd_config_path}")    




   
