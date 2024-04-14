#chem project, thermodynamic calculator
# enthalpy, entropy, internal energy, workdone, gibbs bakchodi, gamma, cp,cv,isothermal reversible
#adiabatic compression and expansion n stuff
import sys
import math
def menu():
    print("Choice:")
    print("1) Change in Internal Energy")
    print("2) Work Done")
    print("3) Change in Enthalpy")
    print("4) Change in Entropy")
    print("5) Work done in a Heat Engine")
    print("6) Efficiency of a heat Engine")
    print("7) Exit")
    input_choice = int(input("Enter choice number:"))
    if input_choice == 1:
        Change_internal_energy()
    elif input_choice == 2:
        Work_Done()
    elif input_choice == 3:
        Change_in_Enthalpy()
    elif input_choice == 4:
        change_in_entropy()
    elif input_choice == 5:    
        Work_done_in_a_Heat_Engine()
    elif input_choice == 6:
        Efficiency_of_a_heat_Engine()
    elif input_choice == 7:
        sys.exit(0)
    else:
        print("Invalid input")

#change in internal energy
def Change_internal_energy():
    reaction_type = input("Enter reaction type [Isothermal reversible expansion/Isothermal reversible compression/adiabatic reversible expansion/adiabatic reversible compression]:").lower()
    if reaction_type == "isothermal reversible expansion":
        print("Change in internal energy for an Isothermal reversible expansion is 0")
    elif reaction_type == "isothermal reversible compression":
        print("Change in internal energy for an Isothermal reversible compression is 0")
    elif reaction_type == "adiabatic reversible expansion":
        q=0
        gamma = float(input("Enter gamma value [Enter 0 is no value is given]:"))
        if gamma == 0:
            Cv = float(input("Enter Cv value:"))
            Cp = float(input("Enter Cp value:"))
            gamma = Cp/Cv
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = -(nRg_1*d_T)
            d_U = W
            print("The change in internal energy is:",d_U)
        else:
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = -(nRg_1*d_T)
            d_U = W
            print("The change in internal energy is:",d_U)
    elif reaction_type == "adiabatic reversible compression":
        q=0
        gamma = float(input("Enter gamma value [Enter 0 is no value is given]:"))
        if gamma == 0:
            Cv = float(input("Enter Cv value:"))
            Cp = float(input("Enter Cp value:"))
            gamma = Cp/Cv
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            d_U = W
            print("The change in internal energy is:",d_U)
        else:
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            d_U = W
    else:
        print("Invalid input")
        sys.exit(0)

#work done
def Work_Done():
    reaction_type = input("Enter reaction type [Isothermal reversible expansion/Isothermal reversible compression/adiabatic reversible expansion/adiabatic reversible compression]:").lower()
    if reaction_type == "isothermal reversible expansion":
        num_moles = int(input("Enter number of moles:"))
        T = int(input("Enter the temperature value in kelvin:"))
        v1 = int(input("Enter volume v1 [enter 0 is no volume is specified]:"))
        v2 = int(input("Enter vlolume v2 [enter 0 is no volume is specified]:"))
        if v1 == 0 and v2 == 0:
            p1 = int(input("Enter pressure p1:"))
            p2 = int(input("Enter pressure p2:"))
            lnp = p1/p2
            lnp_main = math.log(lnp)
            W = num_moles*8.314*T*lnp_main
            print("Work done in isothermal reversible expansion is:",W)
        else:
            lnv = v2/v1
            lnv_main = math.log(lnv)
            W = num_moles*8.314*T*lnv_main
            print("Work done in isothermal reversible expansion is:",W)

    elif reaction_type == "isothermal reversible compression":
        num_moles = int(input("Enter number of moles:"))
        T = int("Enter the temperature value in kelvin:")
        v1 = int(input("Enter volume v1 [enter 0 is no volume is specified]:"))
        v2 = int(input("Enter vlolume v2 [enter 0 is no volume is specified]:"))
        if v1 == 0 and v2 == 0:
            p1 = int(input("Enter pressure p1:"))
            p2 = int(input("Enter pressure p2:"))
            lnp = p1/p2
            lnp_main = math.log(lnp)
            W = num_moles*8.314*T*lnp_main
            print("Work done in isothermal reversible expansion is:",W)
        else:
            lnv = v2/v1
            lnv_main = math.log(lnv)
            W = num_moles*8.314*T*lnv_main
            print("Work done in isothermal reversible expansion is:",W)
        
    elif reaction_type == "adiabatic reversible expansion":
        q=0
        gamma = float(input("Enter gamma value [Enter 0 is no value is given]:"))
        if gamma == 0:
            Cv = float(input("Enter Cv value:"))
            Cp = float(input("Enter Cp value:"))
            gamma = Cp/Cv
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            # d_U = W
            print("The work done in adiabatic reversible expansion is:",W)
        else:
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            # d_U = W
            print("The work done in adiabatic reversible expansion is:",W)
    elif reaction_type == "adiabatic reversible compression":
        q=0
        gamma = float(input("Enter gamma value [Enter 0 is no value is given]:"))
        if gamma == 0:
            Cv = float(input("Enter Cv value:"))
            Cp = float(input("Enter Cp value:"))
            gamma = Cp/Cv
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            print("The work done in adiabatic reversible expansion is:",W)
        else:
            num_moles = int("Enter number of moles:")
            T1 = input("Enter Temperature in Kelvin:")
            T2 = input("Enter Temperature in Kelvin:")
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            print("The work done in adiabatic reversible expansion is:",W)
    else:
        print("Invalid input")
        sys.exit(0)
            
# #chanhge in enthalpy
# nCpdT
def Change_in_Enthalpy():
    reaction_type = input("Enter reaction type [Isothermal reversible expansion/Isothermal reversible compression/adiabatic reversible expansion]:").lower()
    if reaction_type == "isothermal reversible expansion":
        print("Change in enthalpy is 0 as change in temperature is 0")
    elif reaction_type == "isothermal reversible compression":
        print("Change in enthalpy is 0 as change in temperature is 0")
    elif reaction_type == "adiabatic reversible expansion":
        num_moles = int(input("Enter the number of moles:"))
        T1 = int(input("Enter temperature 1 in k:"))
        T2 = int(input("Enter temperature 2 in k:"))
        d_T = T2-T1
        Cp = float(input("Enter Cp Value [enter 0 if Cv is given]:"))
        if Cp == 0:
            Cv = float(input("Enter Cv value:"))
            Cp = 8.3114*Cv
            d_H = num_moles*Cp*d_T
            print("Change in Enthalpy is:",d_H)
        else:
            d_H = num_moles*Cp*d_T
            print("Change in Enthalpy is:",d_H)
    else:
        print("Invalid input")
        sys.exit(0)
    

# change in entropy
def change_in_entropy():
    process_input = input("Enter the type of process [Isothermal/Isobaric/Isochoric]:").lower()
    if process_input == "isothedrmal":
        num_moles = int(input("Enter the number of moles:"))
        v1 = int(input("Enter volume v1 [enter 0 is v1 is not given]:"))
        v2 = int(input("Enter volume v2 [enter 0 is v2 is not given]:"))
        if v1 == 0 and v2 == 0:
            p1 = int(input("Enter pressure p1:"))
            p2 = int(input("Enter pressure p2:"))
            lnp = p1/p2
            lnp_main = math.log(lnp)
            d_S = num_moles*8.314*lnp_main
            print("The change in entropy in an isothermal process is:",d_S)
        else:
            lnv = v2/v1
            lnv_main = math.log(lnv)
            d_S = num_moles*8.314*lnv_main
            print("The entropy change in an isothermal process is:",d_S)
    elif process_input == "isochoric":
        num_moles = int(input("Enter the number of moles:"))
        Cv = float(input("Enter the Cv value:"))
        T1 = int(input("Enter the temperature T1 in Kelvin:"))
        T2 = int(input("Enter the temperature T2 in Kelvin:"))
        lnt = T2/T1
        lnt_main = math.log(lnt)
        d_S = num_moles*8.314*Cv*lnt_main
        print("The change in entropy in an isochoric process is:",d_S)
    elif process_input == "isobaric":
        num_moles = int(input("Enter the number of moles:"))
        T1 = int(input("Enter the temperature T1 in Kelvin:"))
        T2 = int(input("Enter the temperature T2 in Kelvin:"))
        lnt = T2/T1
        lnt_main = math.log(lnt)
        Cp = float(input("Enter the Cp value [Enter 0 if no Cv is specified in question]:"))
        if Cp == 0:
            Cv = float(input("Enter the Cv value:"))
            Cp = Cv+8.314
            d_S = num_moles*8.314*Cp*lnt_main
            print("The change in entropy in an isobaric process is:",d_S)
        else:
            d_S = num_moles*8.314*Cp*lnt_main
            print("The change in entropy in an isobaric process is:",d_S)
    else:
        print("Invalid input")
        sys.exit(0)
        
        
# #work done in a heat engine
def Work_done_in_a_Heat_Engine():
    qh = float(input("Enter qh value:"))
    tc = int(input("Enter temperature tc value in Kelvin:"))
    th = int(input("Enter temperature th value in Kelvin:"))
    tch = tc/th
    w = qh*(1-tch)
    print("Work done by the heat engine is:",w)
# #efficiency of a heat engine
def Efficiency_of_a_heat_Engine():
    qc = float(input("Enter qc value [enter 0 if Tc is given]:"))
    qh = float(input("Enter qh value [enter 0 if Th is given]:"))
    if qc == 0 and qh == 0:
        tc = int(input("Enter temperature Tc value in Kelvin:"))
        th = int(input("Enter temperature Th value in Kelvin:"))
        tch = tc/th
        efficiency = 1-tch
        print("The efficiency of the heat engine is:",efficiency)
    else:
        qch = qc/qh
        efficiency = 1-qch
        print("The efficiency of the heat engine is:",efficiency)
while True:
    menu()