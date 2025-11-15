def cm_to_m(cm):
    return cm / 100


def m_to_cm(m):
    return m * 100


def cm_to_inches(cm):
    # 1 inch = 2.54 cm
    return cm / 2.54


def feet_inches_to_cm(feet, inches):
    # najpierw zamieniamy na całkowite cale
    total_inches = feet * 12 + inches
    # 1 inch = 2.54 cm
    return total_inches * 2.54

