# #############################################################################
# ### MyGlobal
# ### V 1.01
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = False
    inc_serial          = False
    inc_i2c             = False


class Global_WS2812:

    numpix_1            = 50            # Anz. LEDs im 1. Stripe -> Einschlagbahn und Splitter
    numpix_2            = 50            # Anz. LEDs im 2. Stripe -> Umlaufbahn innen innen
    # numpix_3          = 196           # Anz. LEDs im 3. Stripe -> Umlaufbahn innen aussen
    # numpix_4          = 196           # Anz. LEDs im 4. Stripe -> Umlaufbahn aussen innen
    # numpix_5          = 196           # Anz. LEDs im 5. Stripe -> Umlaufbahn aussen aussen
    # numpix_6          = 8             # Anz. LEDs im 6. Stripe -> Splitter-Strahl

    seg_01_strip        = 0             #  1. Seg -> Stripe      # Laser Hinlauf
    seg_01_start        = 0             #  1. Seg -> Start
    seg_01_count        = 50            #  1. Seg -> Anzahl

    seg_02_strip        = 1             #  2. Seg -> Stripe      # Laser Rücklauf
    seg_02_start        = 0             #  2. Seg -> Start
    seg_02_count        = 50            #  2. Seg -> Anzahl


# -----------------------------------------------------------------------------
    #                        R   G   B
    color_off           = (  0,  0,  0)
    color_def           = (  0,  0,  1)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 30, 30, 30)
    
    color_anim_1_def    = (  2,  0,  0)
    color_anim_1_on     = ( 220, 0,  0)
    color_anim_1_half   = (  50, 0,  0)
    
    color_anim_2_def    = (  2,  0,  0)
    color_anim_2_on     = (  0,200,  0)
    color_anim_2_half   = (  0, 50,  0)

    color_anim_3_def    = (  2,  0,  0)
    color_anim_3_on     = (200,  0,  0)
    color_anim_3_half   = ( 50,  0,  0)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
