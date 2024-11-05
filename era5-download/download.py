import xarray as _xr
import cdsapi as _cdsapi

# location of downloaded files
_path = "/srvfs/scratch/avoigt/msc-intro-computational-meteorology-exercises-w2024/"

def era5_land(_year, _month):
    """
    Downloads era5 land data for a given year and month.
    """
    _dataset = "reanalysis-era5-land"
    _request = {
        "variable": [
            "2m_temperature", "surface_solar_radiation_downwards",
            "10m_u_component_of_wind", "10m_v_component_of_wind"
        ],
        "year": _year,
        "month": _month,
        "day": [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
            "25", "26", "27", "28", "29", "30", "31"],
        "time": [
            "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
            "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
            "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"],
        "data_format": "netcdf",
        "download_format": "unarchived"
    }
    _client = _cdsapi.Client()
    _client.retrieve(_dataset, _request).download(_path+"/era5-land-"+_year+"-"+_month+".nc")

def era5(_year, _month):
    """
    Downloads era5 data for a given year and month.
    """
    _dataset = "reanalysis-era5-single-levels"
    _request = {
        "product_type": ["reanalysis"],
        "variable": [
            "2m_temperature", "surface_solar_radiation_downwards", "surface_solar_radiation_downward_clear_sky",
            "10m_u_component_of_wind", "10m_v_component_of_wind"
        ],
        "year": _year,
        "month": _month,
        "day": [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
            "25", "26", "27", "28", "29", "30", "31"],
        "time": [
            "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
            "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
            "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"],
        "data_format": "netcdf",
        "download_format": "unarchived"
    }
    _client = _cdsapi.Client()
    _client.retrieve(_dataset, _request).download(_path+"/era5-"+_year+"-"+_month+".nc")

