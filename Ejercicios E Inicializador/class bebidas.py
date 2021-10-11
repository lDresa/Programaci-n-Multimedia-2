print("Menu de bebidas")

class Bebidas:
    base = "liquido"
    compuesto = "agua"
    tipo = ["pura","carbonizada","alcoholica","jugo","lacteos"]

    def __init__(self,ti,s,c,ta):
        self.tipo = ti
        self.sabor = s
        self.cantidad = c
        self.tamano = ta

jugo_mz = Bebidas("jugo","manzana","500 ml","medio")
refrezco_nj = Bebidas("refrezco","naranja","1 L","grande")
vino_ti = Bebidas("vino","tinto","750 ml","mediana")
leche_vc = Bebidas("leche","vaca","1 L","grande")
agua_lm = Bebidas("agua","limon","250 ml","pequena")

def imprimir_Bebidas():
    print(">",jugo_mz.tipo,"de",jugo_mz.sabor,"-",jugo_mz.cantidad,"-",jugo_mz.tamano)
    print(">",refrezco_nj.tipo,"de",refrezco_nj.sabor,"-",refrezco_nj.cantidad,"-",refrezco_nj.tamano)
    print(">",vino_ti.tipo,"de",vino_ti.sabor,"-",vino_ti.cantidad,"-",vino_ti.tamano)
    print(">",leche_vc.tipo,"de",leche_vc.sabor,"-",leche_vc.cantidad,"-",leche_vc.tamano)
    print(">",agua_lm.tipo,"de",agua_lm.sabor,"-",agua_lm.cantidad,"-",agua_lm.tamano)

imprimir_Bebidas()