"""
SciPy Constants

Constants in SciPy
As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.

These constants can be helpful when you are working with Data Science.

PI is an example of a scientific constant.

"""
from scipy import constants

print('Print the constant value of PI :')
print(constants.pi)

"""
Constant Units
A list of all units under the constants module can be seen using the dir() function.
"""
print('\nA list of all units under the constants module :')
print(dir(constants))

"""
Unit Categories

The units are placed under these categories:
-Metric
-Binary
-Mass
-Angle
-Time
-Length
-Pressure
-Volume
-Speed
-Temperature
-Energy
-Power
-Force
"""

"""
Metric (SI) Prefixes:
Return the specified unit in meter (e.g. centi returns 0.01)
"""
print('\nMetric Prefixes  :')
print('\nyotta = ', constants.yotta)            # 1e+24
print('\nzetta = ', constants.zetta)      # 1e+21
print('\nexa = ', constants.exa)          # 1e+18
print('\npeta = ', constants.peta)        # 1000000000000000.0
print('\ntera = ', constants.tera)        # 1000000000000.0
print('\ngiga = ', constants.giga)        # 1000000000.0
print('\nmega = ', constants.mega)        # 1000000.0
print('\nkilo = ', constants.kilo)        # 1000.0
print('\nhecto = ', constants.hecto)      # 100.0
print('\ndeka = ', constants.deka)        # 10.0
print('\ndeci = ', constants.deci)        # 0.1
print('\ncenti = ', constants.centi)      # 0.01
print('\nmilli = ', constants.milli)      # 0.001
print('\nmicro = ', constants.micro)      # 1e-06
print('\nnano = ', constants.nano)        # 1e-09
print('\npico = ', constants.pico)        # 1e-12
print('\nfemto = ', constants.femto)      # 1e-15
print('\natto = ', constants.atto)        # 1e-18
print('\nzepto = ', constants.zepto)      # 1e-21

"""
Binary Prefixes:
Return the specified unit in bytes (e.g. kibi returns 1024)
"""
print('\nBinary Prefixes :')
print('\nkibi = ', constants.kibi)      # 1024
print('\nmebi = ', constants.mebi)      # 1048576
print('\ngibi = ', constants.gibi)      # 1073741824
print('\ntebi = ', constants.tebi)      # 1099511627776
print('\npebi = ', constants.pebi)      # 1125899906842624
print('\nexbi = ', constants.exbi)      # 1152921504606846976
print('\nzebi = ', constants.zebi)      # 1180591620717411303424
print('\nyobi = ', constants.yobi)      # 1208925819614629174706176

"""
Mass:
Return the specified unit in kg (e.g. gram returns 0.001)
"""
print('\nMass  :')
print('\ngram = ', constants.gram)                  # 0.001
print('\nmetric_ton = ', constants.metric_ton)      # 1000.0
print('\ngrain = ', constants.grain)                # 6.479891e-05
print('\nlb = ', constants.lb)                      # 0.45359236999999997
print('\npound = ', constants.pound)                # 0.45359236999999997
print('\noz = ', constants.oz)                      # 0.028349523124999998
print('\nounce = ', constants.ounce)                # 0.028349523124999998
print('\nstone = ', constants.stone)                # 6.3502931799999995
print('\nlong_ton = ', constants.long_ton)          # 1016.0469088
print('\nshort_ton = ', constants.short_ton)        # 907.1847399999999
print('\ntroy_ounce = ', constants.troy_ounce)      # 0.031103476799999998
print('\ntroy_pound = ', constants.troy_pound)      # 0.37324172159999996
print('\ncarat = ', constants.carat)                # 0.0002
print('\natomic_mass = ', constants.atomic_mass)    # 1.6605390666e-27
print('\nm_u = ', constants.m_u)                    # 1.6605390666e-27
print('\nu = ', constants.u)                        # 1.6605390666e-27

"""
Angle:
Return the specified unit in radians (e.g. degree returns 0.017453292519943295)
"""
print('\nAngle  :')
print('\ndegree = ', constants.degree)          # 0.017453292519943295
print('\narcmin = ', constants.arcmin)          # 0.0002908882086657216
print('\narcminute = ', constants.arcminute)    # 0.0002908882086657216
print('\narcsec = ', constants.arcsec)          # 4.84813681109536e-06
print('\narcsecond = ', constants.arcsecond)    # 4.84813681109536e-06

"""
Time:
Return the specified unit in seconds (e.g. hour returns 3600.0)
"""
print('\nTime  :')
print('\nminute = ', constants.minute)              # 60.0
print('\nhour = ', constants.hour)                  # 3600.0
print('\nday = ', constants.day)                    # 86400.0
print('\nweek = ', constants.week)                  # 604800.0
print('\nyear = ', constants.year)                  # 31536000.0
print('\nJulian_year = ', constants.Julian_year)    # 31557600.0

"""
Length:
Return the specified unit in meters (e.g. nautical_mile returns 1852.0)
"""
print('\nLength  :')
print('\ninch = ', constants.inch)                              # 0.0254
print('\nfoot = ', constants.foot)                              # 0.30479999999999996
print('\nyard = ', constants.yard)                              # 0.9143999999999999
print('\nmile = ', constants.mile)                              # 1609.3439999999998
print('\nmil = ', constants.mil)                                # 2.5399999999999997e-05
print('\npt = ', constants.pt)                                  # 0.00035277777777777776
print('\npoint = ', constants.point)                            # 0.00035277777777777776
print('\nsurvey_foot = ', constants.survey_foot)                # 0.3048006096012192
print('\nsurvey_mile = ', constants.survey_mile)                # 1609.3472186944373
print('\nnautical_mile = ', constants.nautical_mile)            # 1852.0
print('\nfermi = ', constants.fermi)                            # 1e-15
print('\nangstrom = ', constants.angstrom)                      # 1e-10
print('\nmicron = ', constants.micron)                          # 1e-06
print('\nau = ', constants.au)                                  # 149597870691.0
print('\nastronomical_unit = ', constants.astronomical_unit)    # 149597870691.0
print('\nlight_year = ', constants.light_year)                  # 9460730472580800.0
print('\nparsec = ', constants.parsec)                          # 3.0856775813057292e+16

"""
Pressure:
Return the specified unit in pascals (e.g. psi returns 6894.757293168361)
"""
print('\nPressure  :')
print('\natm = ', constants.atm)                # 101325.0
print('\natmosphere = ', constants.atmosphere)  # 101325.0
print('\nbar = ', constants.bar)                # 100000.0
print('\ntorr = ', constants.torr)              # 133.32236842105263
print('\nmmHg = ', constants.mmHg)              # 133.32236842105263
print('\npsi = ', constants.psi)                # 6894.757293168361

"""
Area:
Return the specified unit in square meters(e.g. hectare returns 10000.0)
"""
print('\nhectare = ', constants.hectare)    # 10000.0
print('\nacre = ', constants.acre)          # 4046.8564223999992

"""
Volume:
Return the specified unit in cubic meters (e.g. liter returns 0.001)
"""
print('\nVolume  :')
print('\nliter = ', constants.liter)                      # 0.001
print('\nlitre = ', constants.litre)                      # 0.001
print('\ngallon = ', constants.gallon)                    # 0.0037854117839999997
print('\ngallon_US = ', constants.gallon_US)              # 0.0037854117839999997
print('\ngallon_imp = ', constants.gallon_imp)            # 0.00454609
print('\nfluid_ounce = ', constants.fluid_ounce)          # 2.9573529562499998e-05
print('\nfluid_ounce_US = ', constants.fluid_ounce_US)    # 2.9573529562499998e-05
print('\nfluid_ounce_imp = ', constants.fluid_ounce_imp)  # 2.84130625e-05
print('\nbarrel = ', constants.barrel)                    # 0.15898729492799998
print('\nbbl = ', constants.bbl)                          # 0.15898729492799998

"""
Speed:
Return the specified unit in meters per second (e.g. speed_of_sound returns 340.5)
"""
print('\nSpeed :')
print('\nkmh = ', constants.kmh)                                    # 0.2777777777777778
print('\nmph = ', constants.mph)                                    # 0.44703999999999994
print('\nmach = ', constants.mach)                                  # 340.5
print('\nspeed_of_sound = ', constants.speed_of_sound)              # 340.5
print('\nknot = ', constants.knot)                                  # 0.5144444444444445

"""
Temperature:
Return the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)
"""
print('\nTemperature :')
print('\nzero_celsius = ', constants.zero_Celsius)              # 273.15
print('\ndegree_Fahrenheit = ', constants.degree_Fahrenheit)    # 0.5555555555555556

"""
Energy:
Return the specified unit in joules (e.g. calorie returns 4.184)
"""
print('\nEnergy  :')
print('\neV = ', constants.eV)                          # 1.6021766208e-19
print('\nelectron_volt = ', constants.electron_volt)    # 1.6021766208e-19
print('\ncalorie = ', constants.calorie)                # 4.184
print('\ncalorie_th = ', constants.calorie_th)          # 4.184
print('\ncalorie_IT = ', constants.calorie_IT)          # 4.1868
print('\nerg = ', constants.erg)                        # 1e-07
print('\nBtu = ', constants.Btu)                        # 1055.05585262
print('\nBtu_IT = ', constants.Btu_IT)                  # 1055.05585262
print('\nBtu_th = ', constants.Btu_th)                  # 1054.3502644888888
print('\nton_TNT = ', constants.ton_TNT)                # 4184000000.0

"""
Power:
Return the specified unit in watts (e.g. horsepower returns 745.6998715822701)
"""
print('\nPower  :')
print('\nhp = ', constants.hp)                      # 745.6998715822701
print('\nhorsepower = ', constants.horsepower)      # 745.6998715822701

"""
Force:
Return the specified unit in newton (e.g. kilogram_force returns 9.80665)
"""
print('\nForce  :')
print('\ndyn = ', constants.dyn)                        # 1e-05
print('\ndyne = ', constants.dyne)                      # 1e-05
print('\nlbf = ', constants.lbf)                        # 4.4482216152605
print('\npound_force = ', constants.pound_force)        # 4.4482216152605
print('\nkgf = ', constants.kgf)                        # 9.80665
print('\nkilogram_force = ', constants.kilogram_force)  # 9.80665
