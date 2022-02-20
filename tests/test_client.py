from requests_mock import Mocker


def test_geo_data_output(client, current_geo_data):
    with Mocker() as mock:
        mock.get(f"{client.get_api_endpoint}/?apikey=", json=current_geo_data)
        response = client.get_geo_location()
        assert response == current_geo_data


def test_geo_data_output_for_ip_address(client, geo_data_for_ip_address):
    with Mocker() as mock:
        mock.get(
            f"{client.get_api_endpoint}/8.8.8.8?apikey=", json=geo_data_for_ip_address
        )
        response = client.get_geo_location_for_ip_address("8.8.8.8")
        assert response == geo_data_for_ip_address
