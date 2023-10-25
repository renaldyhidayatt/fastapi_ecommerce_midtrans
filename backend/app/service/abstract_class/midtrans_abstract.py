from abc import ABC, abstractmethod


class MidtransAbstractService(ABC):
    @abstractmethod
    def createTransaction(self, dto):
        """
        Metode abstrak untuk membuat transaksi pembayaran dengan Payment Gateway tertentu.

        Args:
            dto (PaymentRequest): Data permintaan transaksi yang berisi informasi seperti jumlah pembayaran, nama, email, dan nomor telepon pelanggan.

        Returns:
            dict: Hasil transaksi pembayaran dalam format JSON dari Payment Gateway.
        """
        pass
