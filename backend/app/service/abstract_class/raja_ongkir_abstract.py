from abc import ABC, abstractmethod
from app.domain.requests.rajaongkir.ongkos import OngkosRequest


class RajaOngkirAbstractService(ABC):
    @abstractmethod
    def get_provinsi(self):
        """
        Mendapatkan daftar provinsi dari RajaOngkir API.

        Returns:
            dict: Data provinsi dari RajaOngkir API dalam format JSON.
        Raises:
            Exception: Jika terjadi kesalahan dalam mengambil data provinsi dari API.
        """
        pass

    @abstractmethod
    def get_city(self, id_prov):
        """
        Mendapatkan daftar kota/kabupaten berdasarkan ID provinsi dari RajaOngkir API.

        Args:
            id_prov (int): ID provinsi yang digunakan sebagai filter untuk mendapatkan data kota/kabupaten.

        Returns:
            dict: Data kota/kabupaten dari RajaOngkir API dalam format JSON.
        Raises:
            Exception: Jika terjadi kesalahan dalam mengambil data kota/kabupaten dari API.
        """
        pass

    @abstractmethod
    def get_cost(self, ongkos_dto: OngkosRequest):
        """
        Mendapatkan informasi biaya pengiriman (ongkos kirim) berdasarkan permintaan pengiriman dari RajaOngkir API.

        Args:
            ongkos_dto (OngkosRequest): Data permintaan pengiriman yang berisi asal, tujuan, berat, dan kurir.

        Returns:
            dict: Data biaya pengiriman dari RajaOngkir API dalam format JSON.
        Raises:
            Exception: Jika terjadi kesalahan dalam mengambil data biaya pengiriman dari API.
        """
        pass
