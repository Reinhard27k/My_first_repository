# My_first_repository
A simple tool to check if solar panels are hitting their target output. I built this to help identify when a system needs maintenance (like cleaning or repairs) by comparing theoretical math against actual meter readings.

## What it does
The logic is in `energy_tools.py` and uses three main functions:
* **Yield Calculation**: Figures out how many kWh a system *should* produce based on its size, efficiency, and local sunlight.
* **Performance Ratio (PR)**: The core metric—compares actual production to the theoretical max.
* **Fault Detection**: A quick check that flags any system with a PR below 0.75.

## Example Scenario
If you have a **20m²** array with **18% efficiency** on a day with **6.5 kWh/m²** of sun:
* **Expected:** 23.4 kWh
* **Actual Meter Reading:** 16.0 kWh
* **Result:** PR is **0.68** (This would be flagged as "Faulty").

## Setup & Testing
Install dependencies:
`pip install -r requirements.txt`

Run the tests:
`pytest test_energy_tools.py`

This repo uses GitHub Actions to run these tests automatically on every push.

The aim of this repository is to get used to the git environment and fulfill the requirements of the first assignment of the lecture "370.062 Open Source Energy System Modeling". 

