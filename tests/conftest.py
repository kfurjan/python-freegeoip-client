import pytest
from freegeoip_client import FreeGeoIpClient


@pytest.fixture()
def client():
    yield FreeGeoIpClient(api_key="")


@pytest.fixture()
def current_geo_data():
    yield {
        "city": "Zagreb",
        "country_code": "HR",
        "country_name": "Croatia",
        "ip": "",
        "latitude": 0,
        "longitude": 0,
        "metro_code": 0,
        "region_code": "21",
        "region_name": "City of Zagreb",
        "time_zone": "Europe/Zagreb",
        "zip_code": "10000",
    }


@pytest.fixture()
def geo_data_for_ip_address():
    yield {
        "city": "",
        "country_code": "US",
        "country_name": "United States",
        "ip": "8.8.8.8",
        "latitude": 37.751,
        "longitude": -97.822,
        "metro_code": 0,
        "region_code": "",
        "region_name": "",
        "time_zone": "America/Chicago",
        "zip_code": "",
    }
