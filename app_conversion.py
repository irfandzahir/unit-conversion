import streamlit as st

# Comprehensive conversion factors from the table
conversion_factors = {
    "Mass": {
        "kg": {"g": 1000, "metric ton (tonne)": 0.001, "lbm": 2.20462, "oz": 35.27392},
        "g": {"kg": 0.001, "lbm": 0.00220462, "oz": 0.03527392},
        "metric ton (tonne)": {"kg": 1000, "lbm": 2204.62},
        "lbm": {"kg": 0.453592, "g": 453.592, "oz": 16},
        "oz": {"kg": 0.0283495, "lbm": 0.0625}
    },
    "Length": {
        "m": {"cm": 100, "mm": 1000, "microns (µm)": 1e6, "angstroms (Å)": 1e10, "ft": 3.28084, "mile": 0.000621371},
        "cm": {"m": 0.01, "ft": 0.0328084},
        "mm": {"m": 0.001, "ft": 0.00328084},
        "microns (µm)": {"m": 1e-6},
        "angstroms (Å)": {"m": 1e-10},
        "ft": {"m": 0.3048, "in": 12, "yard": 0.333333, "mile": 0.000189394},
        "in": {"ft": 0.0833333, "cm": 2.54},
        "yard": {"ft": 3},
        "mile": {"m": 1609.34}
    },
    "Volume": {
        "m³": {"L": 1000, "cm³": 1e6, "mL": 1e6, "ft³": 35.3147},
        "L": {"m³": 0.001, "gal (UK)": 0.219969, "gal (US)": 0.264172, "qt": 1.05669},
        "cm³": {"m³": 1e-6},
        "mL": {"m³": 1e-6},
        "ft³": {"m³": 0.0283168, "in³": 1728},
        "gal (UK)": {"L": 4.54609, "gal (US)": 1.20095},
        "gal (US)": {"L": 3.78541, "gal (UK)": 0.832674},
        "qt": {"L": 0.946353, "gal (US)": 0.25},
        "in³": {"ft³": 0.000578704}
    },
    "Density": {
        "g/cm³": {"kg/m³": 1000, "lbm/ft³": 62.42796},
        "kg/m³": {"g/cm³": 0.001, "lbm/ft³": 0.06242796},
        "lbm/ft³": {"g/cm³": 0.0160185, "kg/m³": 16.0185}
    },
    "Force": {
        "N": {"lbf": 0.224809, "dynes": 1e5},
        "lbf": {"N": 4.44822, "dynes": 4.44822e5},
        "dynes": {"N": 1e-5, "lbf": 2.24809e-6}
    },
    "Pressure": {
        "atm": {"Pa": 101325, "kPa": 101.325, "bar": 1.01325, "psi": 14.6959, "mmHg": 760, "inHg": 29.9213},
        "Pa": {"atm": 9.86923e-6, "bar": 1e-5, "psi": 0.000145038, "mmHg": 0.00750062},
        "kPa": {"atm": 0.00986923, "Pa": 1000, "psi": 0.145038},
        "bar": {"atm": 0.986923, "Pa": 100000, "psi": 14.5038},
        "psi": {"atm": 0.068046, "Pa": 6894.76, "bar": 0.0689476},
        "mmHg": {"atm": 0.00131579, "Pa": 133.322, "inHg": 0.0393701},
        "inHg": {"atm": 0.0334211, "mmHg": 25.4}
    },
    "Energy": {
        "J": {"ergs": 1e7, "cal": 0.23901, "Btu": 9.486e-4, "kWh": 2.77778e-7},
        "kWh": {"J": 3.6e6, "cal": 860420, "Btu": 3412.14},
        "cal": {"J": 4.184, "kWh": 1.16279e-6, "Btu": 0.00396567},
        "Btu": {"J": 1055.06, "cal": 252.164}
    },
    "Power": {
        "W": {"hp": 0.00134102, "Btu/s": 9.486e-4, "ft·lbf/s": 0.73756},
        "hp": {"W": 745.7, "Btu/s": 0.706787},
        "Btu/s": {"W": 1055.06, "hp": 1.41485}
    }
}

st.title("Comprehensive Unit Conversion Tool")

# Select the quantity type
quantity_type = st.selectbox("Select Quantity Type", list(conversion_factors.keys()))

# Select the units for conversion
unit_from = st.selectbox("From Unit", list(conversion_factors[quantity_type].keys()))
unit_to = st.selectbox("To Unit", list(conversion_factors[quantity_type][unit_from].keys()))

# Input value to convert
value = st.number_input(f"Enter value in {unit_from}", min_value=0.0, format="%f")

# Perform conversion
if st.button("Convert"):
    factor = conversion_factors[quantity_type][unit_from][unit_to]
    result = value * factor
    st.write(f"{value} {unit_from} = {result} {unit_to}")

st.write("Unit conversion tool based on standard conversion factors from the provided table.")
