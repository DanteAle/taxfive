# RBA = Remuneracion Bruta Anual
# RM = Remuneracion Mensual
# M = meses
# ext = ingresos extra
# RNA = Remuneracion Neta Anual
# UIT = 4300
# RBA = Remuneracion Bruta Anual
# R_M = Retencion del Mes
# IAP = Impuesto Anual Proyectado
# M_R = Mes por el cual se calcula la Retencion
# RAM = Retencion Adicional del Mes

def RBA(RM, M, ext):
    return ((RM*M)+ext)


def RNA(RBA, UIT):
    return (RBA-7*(UIT))


def IAP(RNA, UIT):
    if (RNA <= 5*UIT):
        return (RNA*0.08)
    elif (5*UIT < RNA and RNA <= 20*UIT):
        return (RNA*0.14)
    elif (20*UIT < RNA and RNA <= 35*UIT):
        return (RNA*0.17)
    elif (35*UIT < RNA and RNA <= 45*UIT):
        return (RNA*0.20)
    elif (45*UIT < RNA):
        return (RNA*0.30)
    else:
        return 0


def BLOCK(M_R):
    if M_R <= 3:
        return 0
    elif M_R == 4:
        return 2
    elif M_R <= 7:
        return 3
    elif M_R == 8:
        return 4
    elif M_R <= 11:
        return 5
    return -1


def R_M(M_R, IAP, RET):
    d = [12, 9, 8, 5, 4, 1]
    return (IAP-RET)/d[BLOCK(M_R)]


def RAM(suma, IAP_1, UIT):
    if (suma <= 5*UIT):
        return ((suma*0.08)-IAP_1)
    elif (5*UIT < suma and suma <= 20*UIT):
        return ((suma*0.14)-IAP_1)
    elif (20*UIT < suma and suma <= 35*UIT):
        return ((suma*0.17)-IAP_1)
    elif (35*UIT < suma and suma <= 45*UIT):
        return ((suma*0.20)-IAP_1)
    elif (45*UIT < suma):
        return ((suma*0.30)-IAP_1)


def app(RM_1, M, ext, RBA_1, UIT, M_R, IAP_1, suma, RNA_1, R_M_1, TRM, MA, MIA, RMA, var, RAM_1):
    M = int(input("Ingrese el numero de mes actual: "))
    RM_1 = int(input("Ingrese remuneracion mensual: "))
    ext = int(input("Ingrese otros ingresos: "))
    UIT = 4300
    RBA_1 = RBA(RM_1, 12-M, ext)
    print("Remuneracion Bruta Anual: ", RBA_1)
    RNA_1 = RNA(RBA_1, UIT)
    print("Remuneracion Neta Anual: ", RNA_1)
    if (RNA_1 <= 7*UIT):
        print("\nNo se califica para retencion\n")
        print("\nSiguiente calculo\n")
        app(RM_1, 12-M+1, ext, RBA_1, UIT, M_R, IAP_1, suma,
            RNA_1, R_M, TRM, MA, MIA, RMA, var, RAM_1)
    else:
        IAP_1 = IAP(RNA_1, UIT)
        print("Impuesto Anual Proyectado: ", IAP_1)
        # M = int(input("Ingrese el número del mes: "))
        if (M > 0):
            B = BLOCK(M)
            print(M, B)
            RET = 0
            if B == 1:
                RET = int(
                    input("Ingrese las retenciones del mes de enero a marzo: "))
            elif B == 2:
                RET = int(
                    input("Ingrese las retenciones del mes de enero a abril: "))
            elif B == 3:
                RET = int(
                    input("Ingrese las retenciones del mes de enero a julio: "))
            elif B == 4:
                RET = int(
                    input("Ingrese las retenciones del mes de enero a agosto: "))
            elif B == 5:
                RET = int(
                    input("Ingrese las retenciones del mes de enero a noviembre: "))

            R_M_1 = R_M(M, IAP_1, RET)

            # I_A = int(
            #     input("Ingrese importe por pagos distintos (Ingresos Adicionales)"))
            RAM_1 = RAM(RNA_1 + ext, IAP_1, UIT)

            RET_M_1 = R_M_1 - RAM_1

            print(f"La retencion adicional del mes es: {RET_M_1}")

        else:
            print("\nError\n")
            print("\nSiguiente calculo\n")
            app(RM_1, M, ext, RBA_1, UIT, M_R, IAP_1, suma,
                RNA_1, R_M_1, TRM, MA, MIA, RMA, var, RAM_1)
