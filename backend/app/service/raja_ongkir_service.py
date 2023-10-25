from app.core.rajaongkir import RajaOngkirAPI
from app.domain.requests.rajaongkir.ongkos import OngkosRequest
import json
from app.service.abstract_class.raja_ongkir_abstract import RajaOngkirAbstractService


class RajaOngkirService(RajaOngkirAbstractService):
    @staticmethod
    def get_provinsi():
        try:
            connection, headers = RajaOngkirAPI.get_instance()
            endpoint = "/starter/province"
            connection.request("GET", endpoint, headers=headers)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return json.loads(data.decode("utf-8"))
            else:
                raise Exception(
                    f"Failed to fetch province data from RajaOngkir API. Status code: {response.status}"
                )
        except Exception as error:
            raise Exception(
                f"Failed to fetch province data from RajaOngkir API: {error}"
            )

    @staticmethod
    def get_city(id_prov: int):
        try:
            connection, headers = RajaOngkirAPI.get_instance()
            endpoint = f"/starter/city?province={id_prov}"
            connection.request("GET", endpoint, headers=headers)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return json.loads(data.decode("utf-8"))
            else:
                raise Exception(
                    f"Failed to fetch city data from RajaOngkir API. Status code: {response.status}"
                )
        except Exception as error:
            raise Exception(f"Failed to fetch city data from RajaOngkir API: {error}")

    @staticmethod
    def get_cost(ongkos_dto: OngkosRequest):
        try:
            connection, headers = RajaOngkirAPI.get_instance()
            endpoint = "/starter/cost"
            payload = {
                "origin": ongkos_dto.asal,
                "destination": ongkos_dto.tujuan,
                "weight": ongkos_dto.berat,
                "courier": ongkos_dto.kurir,
            }
            payload_str = "&".join([f"{key}={value}" for key, value in payload.items()])
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            connection.request("POST", endpoint, body=payload_str, headers=headers)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return json.loads(data.decode("utf-8"))
            else:
                raise Exception(
                    f"Failed to get shipping cost from RajaOngkir API. Status code: {response.status}"
                )
        except Exception as error:
            raise Exception(f"Failed to get shipping cost from RajaOngkir API: {error}")
