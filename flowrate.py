def flowrate(mass_in: int):
        if mass_in <= 4500:
            out_m6 = (0.0515*0.5* mass_in) + (0.9485 * mass_in)
            cr_frac = ((0.0515*0.5* mass_in))/(out_m6)
            print(out_m6)
            print(cr_frac)
            return
        elif mass_in > 4500: 
            diff = mass_in - 4500 
            out_m6 = (0.0515 * diff) + (0.9485 * mass_in) + (0.05 * 0.0515 * 4500)
            cr_frac = ((0.0515 * diff)+ (0.05 * 0.0515 * 4500))/(out_m6)
            print(out_m6)
            print(cr_frac)
            return 


flowrate(1000)
flowrate(2000)
flowrate(3000)
flowrate(4000)
flowrate(5000)
flowrate(6000)
flowrate(7000)
flowrate(8000)
flowrate(9000)
flowrate(10000)

