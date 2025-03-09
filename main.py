######################################################
### Main-Program                                   ###
### Projekt : Grace-C_Pico-01                      ###
### Version : 0.99                                 ###
### Datum   : 09.03.2025                           ###
######################################################
from machine import Pin, Timer      # type: ignore
from module_init import Global_Module as MyModule
from module_init import Global_WS2812 as MyGlobal

import time                         # type: ignore

anim_dir = False
anim_count = 0

def anim_step():
    global anim_dir, anim_count

    print(anim_dir)
    print(MyGlobal.numpix_1)
    print(anim_count)

    #MyWS2812.led_obj[0].set_pixel(anim_count,(40,40,40))
    if anim_count < (MyGlobal.numpix_1 - 1):
        anim_count = anim_count + 1
    else:
        anim_count = 0
        MyWS2812.do_all_on()
        anim_dir = not anim_dir

    if anim_dir == True:
        MyWS2812.set_led_obj(0,"on")
        MyWS2812.set_led_obj(1,"off")
    else:
        MyWS2812.set_led_obj(0,"off")
        MyWS2812.set_led_obj(1,"on")

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    blink_couter = 0
    
    MyWS2812.do_all_def()	# Alle Leds auf Default-Wert

    #--------------------------------------------
    # Test
    #MyWS2812.do_all_on()
    #--------------------------------------------   
    
    while (True):

        if blink_couter > 20:
            blink_couter = 0
            print("Animation")
            anim_step()
        


        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep(0.01)        # 10ms
        


    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
