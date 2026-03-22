def calculate_solar_yield(area, efficiency, solar_irradiation):
    """
    Calculates expected energy yield in kWh.
    Formula: Energy = Area (m2) * efficiency (%) * Irradiation (kWh/m2)
    """
    if any(val < 0 for val in [area, efficiency, solar_irradiation]):
        raise ValueError("Inputs must be non-negative.")
    return area * efficiency * solar_irradiation

def calculate_performance_ratio(actual_yield, theoretical_yield):
    """
    Calculates the Performance Ratio (PR) of a PV system.
    PR is the ratio of actual energy produced to theoretical energy.
    """
    if theoretical_yield <= 0:
        return 0.0
    pr = actual_yield / theoretical_yield
    return round(pr, 2)

def is_system_faulty(pr, threshold=0.75):
    """Checks if the performance ratio falls below a healthy threshold."""
    return pr < threshold
