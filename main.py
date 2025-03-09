######################################################
### Main-Program                                   ###
### Projekt: Hera-Mission                          ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
import time                                                 # type: ignore

state_0_flag = False

class AnimSeq:
    def __init__(self):
        self.pos = 0
        self.max = 7
        self.end = False
        self.state_flag = False
        self.button_flag = False
        self.wait_tick = 0
        self.wait_count = 100
    
    def reset(self):
        self.pos = 0
        self.end = False
        self.state_flag = False
        self.button_flag = False

    def get_state(self):
        return self.pos

    def next_state(self):
        if self.pos > self.max and not self.end:
            self.pos = 0
            self.end = True
        else:
            self.pos = self.pos + 1
            self.state_flag = False
        return self.pos
    
    def wait(self):
        if self.wait_tick < self.wait_count:
            self.wait_tick = self.wait_tick + 1
        else:
            self.wait_tick = 0
            self.next_state()

def anim_step():
    #print("Anim-Step")
    if myseq.get_state() == 0:
        if myseq.state_flag == False:
            print("State -> 0")
            MyWS2812.do_all_def()
            myseq.state_flag = True
            myseq.next_state()
    
    if myseq.get_state() == 1:
        if myseq.state_flag == False:
            print("State -> 1")
            MyWS2812.do_all_off()
            myseq.state_flag = True
            myseq.next_state()
    
    if myseq.get_state() == 2:
        if myseq.state_flag == False:
            print("State -> 2")
            myseq.state_flag = True
        if not MyWS2812.get_anim_end(0):
            MyWS2812.do_anim_step(0)
        else:
            MyWS2812.set_anim_end(0)
            myseq.next_state()

    if myseq.get_state() == 3:
        if myseq.state_flag == False:
            print("State -> 7")
            MyWS2812.do_all_def()
            myseq.reset()

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():
    
    global myseq

    myseq = AnimSeq()

    print("=== Start Main ===")

    anim_couter = 0

    try:
        print("Start Main Loop")
 
        while (True):
            
            anim_step()

            # Loop-Delay !!!
            time.sleep_ms(10)        # 3ms
    
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")
        MyWS2812.do_all_off() 

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_i2c:
        #print("I2C_MCP23017 -> Load-Module")
        import libs.module_i2c as MyGPIO
        #print("I2C -> Setup")
        MyGPIO.i2c_setup()
        ### Test ###
        #print("I2C -> SetOutput")
        #MyGPIO.i2c_write(0,True)
        #time.sleep(0.5)
        #MyGPIO.i2c_write(0,False)

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import libs.module_ws2812_v3 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
