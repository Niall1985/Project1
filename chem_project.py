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
    reaction_type = input("Enter reaction type [Isothermal reversible expansion/Isothermal reversible compression/Isothermal irreversible expansion/Isothermal irreversible compression/adiabatic reversible expansion/adiabatic reversible compression/adiabatic irreversible expansion/adiabatic irreversible compression]:").lower()
    if reaction_type == "isothermal reversible expansion" or  reaction_type == "isothermal reversible compression":
        reaction_type=reaction_type.split()
        print("Change in internal energy for an Isothermal reversible",reaction_type[2],"is 0 J")
    elif reaction_type == "isothermal irreversible expansion" or  reaction_type == "isothermal irreversible compression":
        reaction_type=reaction_type.split()
        print("Change in internal energy for an Isothermal irreversible",reaction_type[2],"is 0 J")
    elif reaction_type == "adiabatic reversible expansion" or reaction_type == "adiabatic reversible compression" or reaction_type=="adiabatic irreversible expansion" or reaction_type=="adiabatic irreversible compression" or reaction_type=="Isochoric" or reaction_type=="Isobaric":
        reaction_type=reaction_type.split()
        q=0
        gamma = float(input("Enter gamma value [Enter 0 is no value is given]:"))
        if gamma == 0:
            Cv = float(input("Enter Cv value:"))
            Cp=Cv+8.314
            gamma = Cp/Cv
            num_moles = int(input("Enter number of moles:"))
            T1 = float(input("Enter Temperature T1 in Kelvin:"))
            T2 = float(input("Enter Temperature T2 in Kelvin:"))
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = -(nRg_1*d_T)
            d_U = W
            if  reaction_type[2]=="expansion":
                print("The change in internal energy is:",d_U,"J")
            elif  reaction_type[2]=="compression":
                print("The change in internal energy is:",-d_U,"J")
        else:
            num_moles = int(input("Enter number of moles:"))
            T1 = float(input("Enter Temperature T1 in Kelvin:"))
            T2 = float(input("Enter Temperature T2 in Kelvin:"))
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = -(nRg_1*d_T)
            d_U = W
            if  reaction_type[2]=="expansion":
                print("The change in internal energy is:",d_U,"J")
            elif  reaction_type[2]=="compression":
                print("The change in internal energy is:",-d_U,"J")
    
    else:
        print("Invalid input")
        sys.exit(0)
#work done
def Work_Done():
    reaction_type = input("Enter reaction type [Isochoric/Isobaric/Isothermal reversible expansion/Isothermal reversible compression/Isothermal irreversible expansion/Isothermal irreversible compression/adiabatic reversible expansion/adiabatic reversible compression/adiabatic irreversible expansion/adiabatic irreversible compression]:").lower()
    if reaction_type == "isothermal reversible expansion" or reaction_type == "isothermal reversible compression":
        reaction_type=reaction_type.split()
        num_moles = int(input("Enter number of moles:"))
        T = float(input("Enter the temperature value in kelvin:"))
        v1 = int(input("Enter volume v1 [enter 0 is no volume is specified]:"))
        if v1 == 0 :
            p1 = int(input("Enter pressure p1:"))
            p2 = int(input("Enter pressure p2:"))
            lnp = p1/p2
            lnp_main = math.log(lnp)
            W = num_moles*8.314*T*lnp_main
            if reaction_type[2]=="expansion":
                print("Work done in isothermal reversible expansion is:",W,"J")
                print("Total Heat in isothermal reversible expansion is:",-W,"J")
            else:
                print("Work done in isothermal reversible compression is:",W,"J")
                print("Total Heat in isothermal reversible compression is:",-W,"J")
        else:
            v2 = int(input("Enter vlolume v2 :"))
            lnv = v2/v1
            lnv_main = math.log(lnv)
            W = -num_moles*8.314*T*lnv_main
            if reaction_type[2]=="expansion":
                print("Work done in isothermal reversible expansion is:",W,"J")
                print("Total Heat in isothermal reversible expansion is:",-W,"J")
            else:
                print("Work done in isothermal reversible compression is:",W,"J")
                print("Total Heat in isothermal reversible compression is:",-W,"J")
    elif    reaction_type == "isochoric":
        print("Work done in isochoric process is 0")
    elif reaction_type == "isothermal irreversible expansion" or reaction_type == "isothermal irreversible compression" or reaction_type == "isobaric":
        reaction_type=reaction_type.split()
        p=int(input("Enter External pressure:"))
        v1=int(input("Enter volume 1 [Enter 0 if volume is not given]:"))
        if v1==0:
            p1=int(input("Enter the pressure 1:"))
            p2=int(input("Enter the pressure 2:"))
            n=int(input("Enter thr number of moles"))
            T1=float(input("Enter the temperature 1: "))
            T2=float(input("Enter the temperature 2: "))
            W=-p*n*8.314*((T2/p2)-(T1/p1))
            if reaction_type[0]=="isobaric":
                print("Work done in",reaction_type[0],"is:",W,"J")
                print("Total Heat in ",reaction_type[0],"is:",-W,"J")
            else:
                print("Work done in isothermal irreversible",reaction_type[2],"is:",W,"J")
                print("Total Heat in isothermal irreversible",reaction_type[2],"is:",-W,"J")
        else:
            v2=int(input("Enter volume 2:"))
            W=-p*(v2-v1)
            if reaction_type[0]=="isobaric":
                print("Work done in",reaction_type[0],"is:",W,"J")
                print("Total Heat in ",reaction_type[0],"is:",-W,"J")
            else:
                print("Work done in isothermal irreversible",reaction_type[2],"is:",W,"J")
                print("Total Heat in isothermal irreversible",reaction_type[2],"is:",-W,"J")
    elif reaction_type == "adiabatic reversible expansion" or reaction_type == "adiabatic reversible compression" or reaction_type == "adiabatic irreversible expansion" or reaction_type == "adiabatic irreversible compression":
        reaction_type=reaction_type.split()
        q=0
        gamma = float(input("Enter gamma value [Enter 0 is no value is given]:"))
        if gamma == 0:
            Cv = float(input("Enter Cv value:"))
            Cp=Cv+8.314
            gamma = Cp/Cv
            num_moles = int(input("Enter number of moles:"))
            T1 = float(input("Enter Temperature T1 in Kelvin:"))
            T2 = float(input("Enter Temperature T2 in Kelvin[Enter 0 if T2 is not known]:"))
            if T2==0:
                v1=int(input("Enter volume 1 :"))
                v2=int(input("Enter volume 2 :"))
                T2=T1*(pow((v1/v2),(gamma-1)))
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            # d_U = W
            if reaction_type[2]=="expansion":
                print("The work done in adiabatic reversible expansion is:",W,"J")
                print("Total Heat in isothermal irreversible",reaction_type[2],"is:", 0,"J")
            else:
                print("The work done in adiabatic reversible compression is:",W,"J")
                print("Total Heat in isothermal irreversible",reaction_type[2],"is:", 0,"J")
        else:
            num_moles = int(input("Enter number of moles:"))
            T1 = float(input("Enter Temperature  T1 in Kelvin:"))
            T2 = float(input("Enter Temperature T2 in Kelvin[Enter 0 if T2 is not known]:"))
            if T2==0:
                v1=int(input("Enter volume 1 :"))
                v2=int(input("Enter volume 2 :"))
                T2=T1*(pow((v1/v2),(gamma-1)))
            d_T = T2-T1
            gamma_1 = gamma-1
            nR = num_moles*8.314
            nRg_1 = nR/gamma_1
            W = nRg_1*d_T
            if reaction_type[2]=="expansion":
                print("The work done in adiabatic reversible expansion is:",W,"J")
                print("Total Heat in isothermal irreversible",reaction_type[2],"is:", 0,"J")
            else:
                print("The work done in adiabatic reversible compression is:",W,"J")
                print("Total Heat in isothermal irreversible",reaction_type[2],"is:", 0,"J")
    else:
        print("Invalid input")
        sys.exit(0)
            
# #chanhge in enthalpy
# nCpdT
def Change_in_Enthalpy():
    reaction_type = input("Enter reaction type [Isothermal reversible expansion/Isothermal reversible compression/Isothermal irreversible expansion/Isothermal irreversible compression/adiabatic reversible expansion/adiabatic reversible compression/adiabatic irreversible expansion/adiabatic irreversible compression]:").lower()
    if reaction_type == "isothermal reversible expansion" or reaction_type == "isothermal reversible compression" or reaction_type == "isothermal irreversible expansion" or reaction_type == "isothermal irreversible compression":
        reaction_type=reaction_type.split()
        print("Change in enthalpy is 0 as change in temperature is 0 J ")
        
    elif reaction_type == "adiabatic reversible expansion" or reaction_type=="adiabatic reversible compression" or reaction_type == "adiabatic irreversible expansion" or reaction_type=="adiabatic irreversible compression" or reaction_type=="Isochoric" or reaction_type=="Isobaric":
        num_moles = int(input("Enter the number of moles:"))
        T1 = float(input("Enter temperature 1 in k:"))
        T2 = float(input("Enter temperature 2 in k:"))
        d_T = T2-T1
        Cp = float(input("Enter Cp Value [enter 0 if Cv is given]:"))
        if Cp == 0:
            Cv = float(input("Enter Cv value:"))
            Cp = 8.314+Cv
            d_H = num_moles*Cp*d_T
            print("Change in Enthalpy for",reaction_type,"is:",d_H,"J")
        else:
            d_H = num_moles*Cp*d_T
            print("Change in Enthalpy for",reaction_type,"is:",d_H,"J")
    else:
        print("Invalid input")
        sys.exit(0)
    

# change in entropy
def change_in_entropy():
    process_input = input("Enter the type of process [Isothermal/Isobaric/Isochoric]:").lower()
    if process_input == "isothermal":
        num_moles = int(input("Enter the number of moles:"))
        v1 = int(input("Enter volume v1 [enter 0 is v1 is not given]:"))
        if v1 == 0:
            p1 = int(input("Enter pressure p1:"))
            p2 = int(input("Enter pressure p2:"))
            lnp = p1/p2
            lnp_main = math.log(lnp)
            d_S = num_moles*8.314*lnp_main
            print("The change in entropy in an isothermal process is:",d_S,"J")
        else:
            v2 = int(input("Enter volume v2 :"))
            lnv = v2/v1
            lnv_main = math.log(lnv)
            d_S = num_moles*8.314*lnv_main
            print("The entropy change in an isothermal process is:",d_S,"J")
    elif process_input == "isochoric":
        num_moles = int(input("Enter the number of moles:"))
        Cv = float(input("Enter the Cv value:"))
        T1 = float(input("Enter the temperature T1 in Kelvin:"))
        T2 = float(input("Enter the temperature T2 in Kelvin:"))
        lnt = T2/T1
        lnt_main = math.log(lnt)
        d_S = num_moles*8.314*Cv*lnt_main
        print("The change in entropy in an isochoric process is:",d_S,"J")
    elif process_input == "isobaric":
        num_moles = int(input("Enter the number of moles:"))
        T1 = float(input("Enter the temperature T1 in Kelvin:"))
        T2 = float(input("Enter the temperature T2 in Kelvin:"))
        lnt = T2/T1
        lnt_main = math.log(lnt)
        Cp = float(input("Enter the Cp value [Enter 0 if no Cv is specified in question]:"))
        if Cp == 0:
            Cv = float(input("Enter the Cv value:"))
            Cp = Cv+8.314
            d_S = num_moles*8.314*Cp*lnt_main
            print("The change in entropy in an isobaric process is:",d_S,"J")
        else:
            d_S = num_moles*8.314*Cp*lnt_main
            print("The change in entropy in an isobaric process is:",d_S,"J")
    else:
        print("Invalid input")
        sys.exit(0)
        
        
# #work done in a heat engine
def Work_done_in_a_Heat_Engine():
    qh = float(input("Enter qh value:"))
    tc = float(input("Enter temperature tc value in Kelvin:"))
    th = float(input("Enter temperature th value in Kelvin:"))
    tch = tc/th
    w = qh*(1-tch)
    print("Work done by the heat engine is:",w,"J")
# #efficiency of a heat engine
def Efficiency_of_a_heat_Engine():
    qc = float(input("Enter qc value [enter 0 if Tc is given]:"))
    if qc == 0 :
        tc = float(input("Enter temperature Tc value in Kelvin:"))
        th = float(input("Enter temperature Th value in Kelvin:"))
        tch = tc/th
        efficiency = 1-tch
        print("The efficiency of the heat engine is:",efficiency*100,"%")
    else:
        qh = float(input("Enter qh value [enter 0 if Th is given]:"))
        qch = qc/qh
        efficiency = 1-qch
        print("The efficiency of the heat engine is:",efficiency*100,"%")
while True:
    menu()
