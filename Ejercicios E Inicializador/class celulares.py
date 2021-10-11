'''
programa con clase Celulares e inicializador para listar sus caracteristicas
'''
print("Celulares disponibles:")

#clase Celulares como plantilla para caracteristicas de telefonos
class Celulares:
    def __init__(self,bra,m,d,cpu,s,camr,camf,bat):
        self.brand = bra
        self.model = m
        self.display = d
        self.cpu = cpu
        self.storage = s
        self.camera_rear = camr
        self.camera_front = camf
        self.battery = bat

#models (brand,model,display,cpu,storage,rear camera, front camera, battery)
sa_galaxy_s21u = Celulares("Samsung","Galaxy S21 Ultra","1440 x 3200","Snapdragon 888 / Exynos 2100","128GB/256GB/512GB","108MP+10MP+10MP+12MP","40MP","5,000mAh")
ap_iphone_13pro = Celulares("Apple","iPhone 13 Pro Max","1170 x 2532","A15 Bionic","128GB/256GB/512GB/1TB","12MP+12MP+12MP","12MP","3,095mAh/4,352mAh")
op_9_pro = Celulares("OnePlus","9 Pro","1440 x 3216","Snapdragon 888","128/256GB","48MP+50MP+8MP+2MP","16MP","4,500mAh")
sa_galaxy_note20u = Celulares("Samsung","Galaxy Note 20 Ultra","1440 x 3088","Exynos 990 / Snapdragon 865 Plus","128GB/256/512GB","108MP/12MP+12MP+12MP","10MP","4,500mAh")
ap_iphone_se = Celulares("Apple","iPhone SE","1134 x 750","A13 Bionic","64/128/256GB","12MP","7MP","1,821mAh")

#funcion para imprimir los objetos utilizando los parametros de la clase
def imprimir_Celulares():
    print(">",sa_galaxy_s21u.brand, sa_galaxy_s21u.model, "| Resolucion:",sa_galaxy_s21u.display, "| CPU:",sa_galaxy_s21u.cpu, "| Almacenamiento:",sa_galaxy_s21u.storage, "| Camara trasera:",sa_galaxy_s21u.camera_rear, "| Camara frontal:",sa_galaxy_s21u.camera_front, "| Bateria:",sa_galaxy_s21u.battery)
    print(">",ap_iphone_13pro.brand, ap_iphone_13pro.model, "| Resolucion:",ap_iphone_13pro.display, "| CPU:",ap_iphone_13pro.cpu, "| Almacenamiento:",ap_iphone_13pro.storage, "| Camara trasera:",ap_iphone_13pro.camera_rear, "| Camara frontal:",ap_iphone_13pro.camera_front, "| Bateria:",ap_iphone_13pro.battery)
    print(">",op_9_pro.brand, op_9_pro.model, "| Resolucion:",op_9_pro.display, "| CPU:",op_9_pro.cpu, "| Almacenamiento:",op_9_pro.storage, "| Camara trasera:",op_9_pro.camera_rear, "| Camara frontal:",op_9_pro.camera_front, "| Bateria:",op_9_pro.battery)
    print(">",sa_galaxy_note20u.brand, sa_galaxy_note20u.model, "| Resolucion:",sa_galaxy_note20u.display, "| CPU:",sa_galaxy_note20u.cpu, "| Almacenamiento:",sa_galaxy_note20u.storage, "| Camara trasera:",sa_galaxy_note20u.camera_rear, "| Camara frontal:",sa_galaxy_note20u.camera_front, "| Bateria:",sa_galaxy_note20u.battery)
    print(">",ap_iphone_se.brand, ap_iphone_se.model, "| Resolucion:",ap_iphone_se.display, "| CPU:",ap_iphone_se.cpu, "| Almacenamiento:",ap_iphone_se.storage, "| Camara trasera:",ap_iphone_se.camera_rear, "| Camara frontal:",ap_iphone_se.camera_front, "| Bateria:",ap_iphone_se.battery)

imprimir_Celulares()