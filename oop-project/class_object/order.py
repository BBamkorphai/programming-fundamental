from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from address import Address
from datetime import datetime

class Order:
    def __init__(self, orders:list, payment_id:str, payment_date:datetime, total_price:float, shipping_price:float, discount_price:float, final_price:float, 
                 address:Address, shipment:str='EMS', status:str='In the product management process.', delivery_time:datetime=None) -> None:
        self._orders = orders
        self._payment_id = payment_id
        self._payment_date = payment_date
        self._total_price = total_price
        self._shipping_price = shipping_price
        self._discount_price = discount_price
        self._final_price = final_price
        self._address = address
        self._shipment = shipment
        self._status = status
        self._delivery_time = delivery_time        

    @property
    def orders(self) -> list:
        return self._orders
    
    @property
    def payment_id(self) -> str:
        return self._payment_id
    
    @property
    def payment_date(self) -> datetime:
        return self._payment_date
    
    @property
    def total_price(self) -> float:
        return self._total_price
    
    @property
    def shipping_price(self) -> float:
        return self._shipping_price
    
    @property
    def discount_price(self) -> float:
        return self._discount_price
    
    @property
    def final_price(self) -> float:
        return self._final_price
    
    @property
    def address(self) -> Address:
        return self._address
    
    @property
    def shipment(self) -> str:
        return self._shipment
    
    @property
    def status(self) -> str:
        return self._status
    
    @property
    def delivery_time(self) -> datetime:
        return self._delivery_time

    def update_order(self, status:str='In the delivery process', delivery_time:datetime=datetime.now()) -> None:
        self._status = status
        self._delivery_time = delivery_time

    def __repr__(self) -> str:
        return f"{str(self._orders)}, {self._payment_id}, {self._payment_date.strftime('%m/%d/%Y')}, {self._final_price:.2f}, {self._status}"