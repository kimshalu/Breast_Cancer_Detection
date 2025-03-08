# Helper functions for encoding
def encode_age(age):
    # Example function to categorize age into bins (e.g., 0-5 years, 6-10 years, etc.)
    if age < 20:
        return 0
    elif age < 30:
        return 1
    elif age < 40:
        return 2
    elif age < 50:
        return 3
    else:
        return 4

def convert_race_to_int(race):
    # Example function to convert race/ethnicity to integer values
    race_mapping = {
        "Non-Hispanic white": 0,
        "Non-Hispanic black": 1,
        "Asian/Pacific Islander": 2,
        "Native American": 3,
        "Hispanic": 4,
        "Other/mixed": 5,
        "Unknown": 6
    }
    return race_mapping.get(race, 6)  # Default to Unknown
def convert_breast_cancer_history_to_int(first_degree_hx):
    # Example function to convert history of breast cancer in a first degree relative to integer values
    hx_mapping = {
        "No": 0,
        "Yes": 1,
        "Unknown": 9
    }
    return hx_mapping.get(first_degree_hx, 9)
def convert_age_menarche_to_int(age_menarche):
    # Example function to convert age at menarche to integer values
    menarche_mapping = {
        "Age >14": 0,
        "Age 12-13": 1,
        "Age <12": 2,
        "Unknown": 9
    }
    return menarche_mapping.get(age_menarche, 9)  # Default to 9 if input is unknown
def convert_age_first_birth_to_int(age_first_birth):
    # Example function to convert age at first birth to integer values
    first_birth_mapping = {
        "Age < 20": 0,
        "Age 20-24": 1,
        "Age 25-29": 2,
        "Age > 30": 3,
        "Nulliparous": 4,
        "Unknown": 9
    }
    return first_birth_mapping.get(age_first_birth, 9)  # Default to 9 if input is unknown
def convert_birads_breast_density_to_int(breast_density):
    # Example function to convert BI-RADS breast density to integer values
    density_mapping = {
        "Almost entirely fat": 1,
        "Scattered fibroglandular densities": 2,
        "Heterogeneously dense": 3,
        "Extremely dense": 4,
        "Unknown or different measurement system": 9
    }
    return density_mapping.get(breast_density, 9)  # Default to 9 if input is unknown
def convert_current_hrt_to_int(current_hrt):
    # Example function to convert the use of hormone replacement therapy to integer values
    hrt_mapping = {
        "No": 0,
        "Yes": 1,
        "Unknown": 9
    }
    return hrt_mapping.get(current_hrt, 9)  # Default to 9 if input is unknown
def convert_menopausal_status_to_int(menopaus):
    # Example function to convert menopausal status to integer values
    menopausal_mapping = {
        "Pre- or peri-menopausal": 1,
        "Post-menopausal": 2,
        "Surgical menopause": 3,
        "Unknown": 9
    }
    return menopausal_mapping.get(menopaus, 9)  # Default to 9 if input is unknown
def convert_bmi_to_group(bmi):
    # Example function to convert BMI to specified group categories
    if 10 <= bmi < 25:
        return 1  # BMI in the range 10-24.99
    elif 25 <= bmi < 30:
        return 2  # BMI in the range 25-29.99
    elif 30 <= bmi < 35:
        return 3  # BMI in the range 30-34.99
    elif bmi >= 35:
        return 4  # BMI of 35 or more
    else:
        return 9  # Unknown or invalid BMI (e.g., less than 10 or invalid)
def convert_biophx_to_int(biophx):
    # Example function to convert previous breast biopsy or aspiration to integer values
    biophx_mapping = {
        "No": 0,
        "Yes": 1,
        "Unknown": 9
    }
    return biophx_mapping.get(biophx, 9)  # Default to 9 if input is unknown
