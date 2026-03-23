## Developed with assistance from Gemini (AI)
# Author: Reinahrd Köppel

import pytest
from energy_tools import calculate_solar_yield, calculate_performance_ratio, is_system_faulty

def test_yield_calculation():
    # 10m2 panel * 20% efficiency * 5kWh/m2 radiation = 10kWh
    assert calculate_solar_yield(10, 0.20, 5) == 10.0

def test_negative_input_error():
    with pytest.raises(ValueError):
        calculate_solar_yield(-10, 0.2, 5)

def test_performance_ratio():
    assert calculate_performance_ratio(8, 10) == 0.8
    assert calculate_performance_ratio(5, 0) == 0.0

def test_system_faulty():
    assert is_system_faulty(0.60) is True
    assert is_system_faulty(0.90) is False
