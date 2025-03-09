# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = False
    inc_serial          = False


class Global_WS2812:

    numpix_1            = 46            # Anzahl LEDs im 1. Stripe
    numpix_2            = 46            # Anzahl LEDs im 2. Stripe

    seg_01_strip        = 0             #  1. Ledsegment -> Stripe      # 1. Laser Hinlauf
    seg_01_start        = 0             #  1. Ledsegment -> Start
    seg_01_count        = 45            #  1. Ledsegment -> Anzahl

    seg_02_strip        = 1             #  2. Ledsegment -> Stripe      # 2. Laser Rücklauf
    seg_02_start        = 0             #  2. Ledsegment -> Start
    seg_02_count        = 45            #  2. Ledsegment -> Anzahl

# -----------------------------------------------------------------------------

    color_def           = (  5,  0,  0)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (  0,200,  0)
    color_blink_off     = (  0, 10,  0)


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