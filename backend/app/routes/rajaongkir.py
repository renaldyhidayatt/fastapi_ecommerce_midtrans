from fastapi import APIRouter
from app.domain.requests.rajaongkir.ongkos import OngkosRequest
from app.service.raja_ongkir_service import RajaOngkirService

rajaongkir_router = APIRouter(prefix="/rajaongkir", tags=["Rajaongkir"])


@rajaongkir_router.get("/")
def get_provinsi():
    raja_ongkir = RajaOngkirService()

    return raja_ongkir.get_provinsi()


@rajaongkir_router.get("/get-city/{provId}")
def get_city(provId: int):
    raja_ongkir = RajaOngkirService()

    return raja_ongkir.get_city(id_prov=provId)


@rajaongkir_router.post("/get-shipping-cost")
def getOngkos(ongkos: OngkosRequest):
    raja_ongkir = RajaOngkirService()

    return raja_ongkir.get_cost(ongkos_dto=ongkos)
