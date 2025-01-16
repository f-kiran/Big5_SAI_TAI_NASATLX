# Big-5, SAI, TAI, and NASA-TLX Metrics Calculator

This repository calculates psychological and workload metrics (Big-5, SAI, TAI, and NASA-TLX) from an XLSX file containing corresponding data.

## Setup
1. Clone the repository:
`git clone <repo-url>`
2. Install dependencies:
`pip install -r requirements.txt`
3. Place your XLSX file in the `data` directory.

## Usage
Run the scripts for each metric:

`cd script/`

`python script/big5.py`

`python script/sai.py`

`python script/tai.py`

`python script/nasa_tlx.py`


## File Structure
```
Big5_SAI_TAI_NASATLX/
├── data/                # Input XLSX files
├── results/             # Output results
├── script/              # Scripts for metric calculations
├── README.md            # Documentation for the repository
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files

```