import math

def imprimir_resultados_directos():
    print("="*75)
    print(" SOLUCIÓN DIRECTA DE CASOS - DISEÑO DE EJES ".center(75))
    print("="*75)

    # =========================================================
    # CÁLCULOS CASO 1 (Ejercicio resuelto 7-1 de Shigley)
    # =========================================================
    print("\n" + " CASO 1 (Ejercicio 7-1) ".center(75, "-"))
    
    # Datos iniciales Caso 1 (Basados en el libro de Shigley 7-1)
    d_1 = 1.10
    Ma_1 = 1260.0
    Mm_1 = 0.0
    Ta_1 = 0.0
    Tm_1 = 1100.0
    Sut_1 = 105000.0
    Sy_1 = 82000.0
    Se_1 = 30000.0
    
    # a) y b) Valores de gráficas
    q_1 = 0.85
    q_cort_1 = 0.88
    Kt_1 = 1.68
    Kts_1 = 1.48

    # c) Factores por fatiga
    Kf_1 = 1 + q_1 * (Kt_1 - 1)
    Kfs_1 = 1 + q_cort_1 * (Kts_1 - 1)

    # d) Esfuerzos nominales
    sigma_a_1 = Kf_1 * (32 * Ma_1) / (math.pi * d_1**3)
    sigma_m_1 = Kf_1 * (32 * Mm_1) / (math.pi * d_1**3)
    tau_a_1 = Kfs_1 * (16 * Ta_1) / (math.pi * d_1**3)
    tau_m_1 = Kfs_1 * (16 * Tm_1) / (math.pi * d_1**3)

    # e) Esfuerzos de Von Mises principales
    sigma_a_prima_1 = math.sqrt(sigma_a_1**2 + 3 * tau_a_1**2)
    sigma_m_prima_1 = math.sqrt(sigma_m_1**2 + 3 * tau_m_1**2)

    # f) Esfuerzo máximo de Von Mises
    sigma_max_prima_1 = math.sqrt((sigma_m_1 + sigma_a_1)**2 + 3 * (tau_m_1 + tau_a_1)**2)

    # g) Factor de diseño (Fluencia)
    ny_1 = Sy_1 / sigma_max_prima_1

    # h) Criterios de falla por fatiga
    n_goodman_1 = 1 / ((sigma_a_prima_1 / Se_1) + (sigma_m_prima_1 / Sut_1))
    n_soderberg_1 = 1 / ((sigma_a_prima_1 / Se_1) + (sigma_m_prima_1 / Sy_1))
    n_asme_1 = 1 / math.sqrt((sigma_a_prima_1 / Se_1)**2 + (sigma_m_prima_1 / Sy_1)**2)
    
    A_gerb_1 = sigma_a_prima_1 / Se_1
    B_gerb_1 = sigma_m_prima_1 / Sut_1
    n_gerber_1 = (-A_gerb_1 + math.sqrt(A_gerb_1**2 + 4 * B_gerb_1**2)) / (2 * B_gerb_1**2)

    # Impresión estructurada Caso 1
    print(f"a) Sensibilidades a la muesca : q = {q_1:.2f}, q_cortante = {q_cort_1:.2f}")
    print(f"b) Factores teóricos          : Kt = {Kt_1:.2f}, Kts = {Kts_1:.2f}")
    print(f"c) Factores por fatiga        : Kf = {Kf_1:.3f}, Kfs = {Kfs_1:.3f}")
    print(f"d) Esfuerzos nominales (psi)  : sigma_a = {sigma_a_1:.2f}, tau_a = {tau_a_1:.2f}")
    print(f"                                sigma_m = {sigma_m_1:.2f}, tau_m = {tau_m_1:.2f}")
    print(f"e) Von Mises principales (psi): sigma_a' = {sigma_a_prima_1:.2f}, sigma_m' = {sigma_m_prima_1:.2f}")
    print(f"f) Von Mises máximo (psi)     : sigma_max' = {sigma_max_prima_1:.2f}")
    print(f"g) Factor de fluencia (n_vM)  : n_y = {ny_1:.3f}")
    print("h) Factores de fatiga         :")
    print(f"      - n_Goodman             = {n_goodman_1:.3f}")
    print(f"      - n_Soderberg           = {n_soderberg_1:.3f}")
    print(f"      - n_Gerber              = {n_gerber_1:.3f}")
    print(f"      - n_ASME                = {n_asme_1:.3f}")


    # =========================================================
    # CÁLCULOS CASO 2 (Unidades: Sistema Inglés - pulg, lbf, psi)
    # =========================================================
    print("\n" + " CASO 2 ".center(75, "-"))
    
    # Datos iniciales Caso 2
    d_2 = 1.10
    Ma_2 = 1260.0
    Tm_2 = 1100.0
    Sut_2 = 105000.0
    Sy_2 = 82000.0
    Se_2 = 30000.0
    
    # a) y b) Valores leídos de gráficas para r=0.11 y D/d=1.5
    q_2 = 0.85
    q_cort_2 = 0.88
    Kt_2 = 1.68
    Kts_2 = 1.48

    # c) Factores por fatiga
    Kf_2 = 1 + q_2 * (Kt_2 - 1)
    Kfs_2 = 1 + q_cort_2 * (Kts_2 - 1)

    # d) Esfuerzos nominales
    sigma_a_2 = Kf_2 * (32 * Ma_2) / (math.pi * d_2**3)
    sigma_m_2 = 0.0  # Porque Mm = 0
    tau_a_2 = 0.0    # Porque Ta = 0
    tau_m_2 = Kfs_2 * (16 * Tm_2) / (math.pi * d_2**3)

    # e) Esfuerzos de Von Mises principales
    sigma_a_prima_2 = math.sqrt(sigma_a_2**2 + 3 * tau_a_2**2)
    sigma_m_prima_2 = math.sqrt(sigma_m_2**2 + 3 * tau_m_2**2)

    # f) Esfuerzo máximo de Von Mises
    sigma_max_prima_2 = math.sqrt((sigma_m_2 + sigma_a_2)**2 + 3 * (tau_m_2 + tau_a_2)**2)

    # g) Factor de diseño (Fluencia)
    ny_2 = Sy_2 / sigma_max_prima_2

    # h) Criterios de falla por fatiga
    n_goodman_2 = 1 / ((sigma_a_prima_2 / Se_2) + (sigma_m_prima_2 / Sut_2))
    n_soderberg_2 = 1 / ((sigma_a_prima_2 / Se_2) + (sigma_m_prima_2 / Sy_2))
    n_asme_2 = 1 / math.sqrt((sigma_a_prima_2 / Se_2)**2 + (sigma_m_prima_2 / Sy_2)**2)
    
    A_gerb_2 = sigma_a_prima_2 / Se_2
    B_gerb_2 = sigma_m_prima_2 / Sut_2
    n_gerber_2 = (-A_gerb_2 + math.sqrt(A_gerb_2**2 + 4 * B_gerb_2**2)) / (2 * B_gerb_2**2)

    # Impresión estructurada Caso 2
    print(f"a) Sensibilidades a la muesca : q = {q_2:.2f}, q_cortante = {q_cort_2:.2f}")
    print(f"b) Factores teóricos          : Kt = {Kt_2:.2f}, Kts = {Kts_2:.2f}")
    print(f"c) Factores por fatiga        : Kf = {Kf_2:.3f}, Kfs = {Kfs_2:.3f}")
    print(f"d) Esfuerzos nominales (psi)  : sigma_a = {sigma_a_2:.2f}, tau_a = {tau_a_2:.2f}")
    print(f"                                sigma_m = {sigma_m_2:.2f}, tau_m = {tau_m_2:.2f}")
    print(f"e) Von Mises principales (psi): sigma_a' = {sigma_a_prima_2:.2f}, sigma_m' = {sigma_m_prima_2:.2f}")
    print(f"f) Von Mises máximo (psi)     : sigma_max' = {sigma_max_prima_2:.2f}")
    print(f"g) Factor de fluencia (n_vM)  : n_y = {ny_2:.3f}")
    print("h) Factores de fatiga         :")
    print(f"      - n_Goodman             = {n_goodman_2:.3f}  <-- (Solicitado en caso 2)")
    print(f"      - n_Soderberg           = {n_soderberg_2:.3f}")
    print(f"      - n_Gerber              = {n_gerber_2:.3f}")
    print(f"      - n_ASME                = {n_asme_2:.3f}")


    # =========================================================
    # CÁLCULOS CASO 3 (Unidades: Sistema Internacional - m, N, Pa)
    # =========================================================
    print("\n" + " CASO 3 ".center(75, "-"))
    
    # Datos iniciales Caso 3
    d_3 = 0.10  # 10 cm en metros
    Ma_3 = 70.0
    Mm_3 = 55.0
    Ta_3 = 45.0
    Tm_3 = 35.0
    Sut_3 = 700e6
    Sy_3 = 560e6
    Se_3 = 210e6
    
    # En este caso los factores se dan directamente en el problema
    Kf_3 = 2.2
    Kfs_3 = 1.8

    # d) Esfuerzos nominales
    sigma_a_3 = Kf_3 * (32 * Ma_3) / (math.pi * d_3**3)
    sigma_m_3 = Kf_3 * (32 * Mm_3) / (math.pi * d_3**3)
    tau_a_3 = Kfs_3 * (16 * Ta_3) / (math.pi * d_3**3)
    tau_m_3 = Kfs_3 * (16 * Tm_3) / (math.pi * d_3**3)

    # e) Esfuerzos de Von Mises principales
    sigma_a_prima_3 = math.sqrt(sigma_a_3**2 + 3 * tau_a_3**2)
    sigma_m_prima_3 = math.sqrt(sigma_m_3**2 + 3 * tau_m_3**2)

    # f) Esfuerzo máximo de Von Mises
    sigma_max_prima_3 = math.sqrt((sigma_m_3 + sigma_a_3)**2 + 3 * (tau_m_3 + tau_a_3)**2)

    # g) Factor de diseño (Fluencia)
    ny_3 = Sy_3 / sigma_max_prima_3

    # h) Criterios de falla por fatiga
    n_goodman_3 = 1 / ((sigma_a_prima_3 / Se_3) + (sigma_m_prima_3 / Sut_3))
    n_soderberg_3 = 1 / ((sigma_a_prima_3 / Se_3) + (sigma_m_prima_3 / Sy_3))
    n_asme_3 = 1 / math.sqrt((sigma_a_prima_3 / Se_3)**2 + (sigma_m_prima_3 / Sy_3)**2)
    
    A_gerb_3 = sigma_a_prima_3 / Se_3
    B_gerb_3 = sigma_m_prima_3 / Sut_3
    n_gerber_3 = (-A_gerb_3 + math.sqrt(A_gerb_3**2 + 4 * B_gerb_3**2)) / (2 * B_gerb_3**2)

    # Impresión estructurada Caso 3
    print("a) Sensibilidades a la muesca : No aplica (Kf y Kfs proporcionados)")
    print("b) Factores teóricos          : No aplica (Kf y Kfs proporcionados)")
    print(f"c) Factores por fatiga        : Kf = {Kf_3:.2f}, Kfs = {Kfs_3:.2f}")
    print(f"d) Esfuerzos nominales (Pa)   : sigma_a = {sigma_a_3:.2e}, tau_a = {tau_a_3:.2e}")
    print(f"                                sigma_m = {sigma_m_3:.2e}, tau_m = {tau_m_3:.2e}")
    print(f"e) Von Mises principales (Pa) : sigma_a' = {sigma_a_prima_3:.2e}, sigma_m' = {sigma_m_prima_3:.2e}")
    print(f"f) Von Mises máximo (Pa)      : sigma_max' = {sigma_max_prima_3:.2e}")
    print(f"g) Factor de fluencia (n_vM)  : n_y = {ny_3:.1f}")
    print("h) Factores de fatiga         :")
    print(f"      - n_Goodman             = {n_goodman_3:.1f}")
    print(f"      - n_Soderberg           = {n_soderberg_3:.1f}")
    print(f"      - n_Gerber              = {n_gerber_3:.1f}  <-- (Solicitado en caso 3)")
    print(f"      - n_ASME                = {n_asme_3:.1f}")
    print("="*75 + "\n")

if __name__ == "__main__":
    imprimir_resultados_directos()