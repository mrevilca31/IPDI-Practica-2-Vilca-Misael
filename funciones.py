import numpy as np

''' BIBLIOTECA DE FUNCIONES '''


''' PASAJE ENTRE RGB e YIQ '''


def pasar_a_YIQ(img):
    R, G, B = canalesRGB(img)

    Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
    I = (0.59590059 * R) + (-0.27455667 * G) + (-0.32134392 * B)
    Q = (0.21153661 * R) + (-0.52273617 * G) + (0.31119955 * B)
    return (Y, I, Q)


def pasar_a_RGB(y, i, q):
    Y, I, Q = normalizar_YIQ(y, i, q)

    r = (Y+0.9563*I+0.621*Q)*255
    g = (Y-0.2721*I-0.6474*Q)*255
    b = (Y-1.1070*I+1.7046*Q)*255

    r = np.clip(r, 0, 255)
    g = np.clip(g, 0, 255)
    b = np.clip(b, 0, 255)
    dimension = Y.shape

    img = np.zeros((dimension[0], dimension[1], 3), dtype='uint8')
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b
    return(img)


def canalesRGB(img):
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    return (r, g, b)


def normalizar_RGB(img):
    return img/255


def normalizar_YIQ(y, i, q):
    Y = np.clip(y, 0.0, 1.0)
    I = np.clip(i, -0.5957, 0.5957)
    Q = np.clip(q, -0.5226, 0.5226)
    return (Y, I, Q)


''' ARITMETICA DE PIXELES '''


def cuasiSumaRGB_Clamp(img1, img2):
    return np.clip(img1 + img2, 0, 1)


def cuasiRestaRGB_Clamp(img1, img2):
    return np.clip(img1 - img2, 0, 1)


def cuasiSumaRGB_Prom(img1, img2):
    return (img1 + img2)/2


def cuasiRestaRGB_Prom(img1, img2):
    return (img1 - img2)/2 + 0.5


def cuasiSumaYIQ_Clamp(YA, IA, QA, YB, IB, QB):
    YC = np.clip(YA + YB, 0, 1)
    IC = (YA*IA+YB*IB)/(YA+YB)
    QC = (YA*QA+YB*QB)/(YA+YB)
    return (YC, IC, QC)


def cuasiRestaYIQ_Clamp(YA, IA, QA, YB, IB, QB):
    YC = np.maximum(YA - YB, 0)
    IC = (YA*IA-YB*IB)/(YA+YB)
    QC = (YA*QA-YB*QB)/(YA+YB)
    return (YC, IC, QC)


def cuasiSumaYIQ_Prom(YA, IA, QA, YB, IB, QB):
    YC = (YA+YB)/2
    IC = (YA*IA+YB*IB)/(YA+YB)
    QC = (YA*QA+YB*QB)/(YA+YB)
    return (YC, IC, QC)


def cuasiRestaYIQ_Prom(YA, IA, QA, YB, IB, QB):
    YC = (YA-YB)/2+0.5
    IC = (YA*IA-YB*IB)/(YA+YB)
    QC = (YA*QA-YB*QB)/(YA+YB)
    return (YC, IC, QC)


def productoRGB(img1, img2):
    return np.clip(img1*img2, 0, 1)


def cocienteRGB(img1, img2):
    img2 = np.clip(img2, 0.001, 1)
    return img1/img2


def restaAbsoluta(img1, img2):
    return np.clip(np.abs(img1-img2), 0, 1)


def ifLigther(img1, img2):
    return np.maximum(img1, img2)


def ifDarker(img1, img2):
    return np.minimum(img1, img2)
