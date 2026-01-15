"""
This module handles the organization and processing of LAS files based on the PetroLuminary style guide.
"""
import re
import shutil
import lasio
import pandas as pd
from pathlib import Path
from datetime import datetime

def get_basin_from_api(filename, api_map):
    """
    Parses a filename to extract an API number and determine the basin.

    Parameters
    ----------
    filename : str
        The filename to parse.
    api_map : dict
        A dictionary mapping API codes to basin and county information.

    Returns
    -------
    tuple
        A tuple containing (basin, county, method).
    """
    pattern = r'(\d{2})[-_]?(\d{3})[-_]?(\d{5})'
    match = re.search(pattern, filename)
    if match:
        state, county_code, _ = match.groups()
        if state in api_map['mappings']:
            state_data = api_map['mappings'][state]
            if county_code in state_data['counties']:
                data = state_data['counties'][county_code]
                return data['basin'], data['county'], f"API-{state}-{county_code}"
    return None, None, None

def get_basin_from_county_name(county_name, api_map):
    """
    Looks up a basin from a county name using the api_map.

    Parameters
    ----------
    county_name : str
        The name of the county to look up.
    api_map : dict
        A dictionary mapping API codes to basin and county information.

    Returns
    -------
    tuple
        A tuple containing (basin, county, method).
    """
    if not county_name:
        return None, None, None
    clean_county = str(county_name).strip().lower()
    for state_data in api_map['mappings'].values():
        for county_data in state_data['counties'].values():
            if county_data['county'].lower() == clean_county:
                return county_data['basin'], county_data['county'], "Header-Lookup"
    return None, None, None

def process_las_file(log_file, api_map, dest_dir):
    """
    Processes a single LAS file to determine its basin and copy it to the correct destination.

    Parameters
    ----------
    log_file : pathlib.Path
        The path to the LAS file.
    api_map : dict
        The mapping for API and county lookups.
    dest_dir : pathlib.Path
        The root destination directory.

    Returns
    -------
    dict
        A dictionary containing tracking information for the processed file.
    """
    filename = log_file.name
    basin, assigned_county, method_used = get_basin_from_api(filename, api_map)
    status = "Mapped via API" if basin else "Init"

    if not basin:
        try:
            las = lasio.read(str(log_file), ignore_header_errors=True)
            header_county = None
            for mnemonic in ['COUNTY', 'CNTY', 'CTY']:
                item = las.well.get(mnemonic)
                if item and item.value:
                    header_county = item.value
                    break
            
            if header_county:
                basin, assigned_county, method_used = get_basin_from_county_name(header_county, api_map)
                if basin:
                    status = "Mapped via Header"
                else:
                    status = f"MISSING MAP DATA: Found '{header_county}'"
                    assigned_county = f"Unmapped: {header_county}"
            else:
                status = "No County in Header"
        except Exception as e:
            status = f"LAS Read Error: {str(e)[:30]}"

    dest_folder = dest_dir / basin if basin else dest_dir / "_Uncategorized"
    basin = basin or "Uncategorized"
    if not method_used:
        method_used = "Failed Lookup"

    try:
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest_path = dest_folder / filename
        shutil.copy(str(log_file), str(dest_path))
    except Exception as e:
        dest_path = f"Copy Failed: {e}"

    return {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'filename': filename,
        'destination': str(dest_path),
        'basin': basin,
        'county': assigned_county or "Unknown",
        'method': method_used,
        'status': status
    }
