# Fraction to Gauge Converter

This project provides a simple Python script that converts a fraction to a percentage and then represents it as a gauge. This script includes error handling and can be easily tested using the `pytest` framework.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Test Results](#test-results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This script takes a fraction input from the user, converts it to a percentage, and then returns a gauge value. The gauge indicates whether the fraction is empty ("E"), full ("F"), or a specific percentage.

## Features

- Convert a fraction to a percentage.
- Handle invalid inputs gracefully.
- Represent the percentage as a gauge value.
- Unit tests for all functionalities using `pytest`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bonheurNE07/fraction-to-gauge.git
   cd fraction-to-gauge
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using the following command:

```bash
python fraction_module.py
```

The script will prompt you to enter a fraction, convert it to a percentage, and display the corresponding gauge value.

## Testing

To run the tests, use the `pytest` command:

```bash
(venv) @bonheurNE07 ➜ /workspaces/Fraction-to-Gauge-Converter (main) $ pytest test_fraction_module.py
```

This will run all the test functions and provide a report on their success or failure.

### Test Coverage

- **`test_convert_value_error`**: Ensures `convert` raises a `ValueError` for invalid fractions.
- **`test_convert_zero_division_error`**: Ensures `convert` raises a `ZeroDivisionError` when the denominator is zero.
- **`test_convert_success`**: Checks that `convert` returns the correct percentages for valid inputs.
- **`test_gauge`**: Verifies that `gauge` returns the correct gauge representation based on the fraction value.

## Test Results

The output might look like this:

```
(venv) @bonheurNE07 ➜ /workspaces/Fraction-to-Gauge-Converter (main) $ pytest test_fraction_module.py
===================================================== test session starts =====================================================
platform linux -- Python 3.10.13, pytest-8.2.2, pluggy-1.5.0
rootdir: /workspaces/Fraction-to-Gauge-Converter
collected 4 items                                                                                                             

test_fraction_module.py ....                                                                                            [100%]

====================================================== 4 passed in 0.02s ======================================================
(venv) @bonheurNE07 ➜ /workspaces/Fraction-to-Gauge-Converter (main) $ 
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact me at [bonheurndezenc@gmail.com](mailto:bonheurndezenc@gmail.com).

---

Thank you for using this script! If you find it helpful, please consider giving it a star on GitHub.
```
