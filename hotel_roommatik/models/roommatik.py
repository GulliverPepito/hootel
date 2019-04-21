# Copyright 2019 Jose Luis Algara (Alda hotels) <osotranquilo@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import json
from datetime import datetime
from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class RoomMatik(models.Model):
    _name = 'roommatik.api'

    @api.model
    def rm_get_date(self):
        # RoomMatik API Gets the current business date/time. (MANDATORY)
        utc_s = '+01:00'
        # TODO Need know UTC in the machine/hotel
        json_response = {
            'dateTime': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f") + utc_s
            }
        json_response = json.dumps(json_response)
        return json_response

    @api.model
    def rm_get_reservation(self, reservation_code):
        # RoomMatik Gets a reservation ready for check-in
        # through the provided code. (MANDATORY)
        apidata = self.env['hotel.folio']
        return apidata.rm_get_reservation(reservation_code)

    @api.model
    def rm_add_customer(self, customer):
        # RoomMatik API Adds a new PMS customer through the provided parameters
        # Addition will be ok if the returned customer has ID. (MANDATORY)
        _logger.info('ROOMMATIK Customer Creation')
        apidata = self.env['res.partner']
        return apidata.rm_add_customer(customer)

    @api.model
    def rm_checkin_partner(self, stay):
        # RoomMatik API Check-in a stay.
        # Addition will be ok if the returned stay has ID. (MANDATORY)
        _logger.info('ROOMMATIK Check-IN')
        apidata = self.env['hotel.checkin.partner']
        return apidata.rm_checkin_partner(stay)

    @api.model
    def rm_get_stay(self, check_in_code):
        # RoomMatik API  Gets stay information through check-in code
        # (if code is related to a current stay)
        # (MANDATORY for check-out kiosk)
        apidata = self.env['hotel.checkin.partner']
        return apidata.rm_get_stay(check_in_code)

    @api.model
    def rm_get_all_room_type_rates(self):
        # Gets the current room rates and availability. (MANDATORY)
        # return ArrayOfRoomTypeRate
        _logger.info('ROOMMATIK Get Rooms and Rates')
        apidata = self.env['hotel.room.type']
        return apidata.rm_get_all_room_type_rates()

    @api.model
    def rm_get_prices(self, start_date, time_interval, number_intervals, room_type, guest_number):
        # Gets some prices related to different dates of the same stay.
        # return ArrayOfDecimal
        _logger.info('ROOMMATIK Get Prices')
        apidata = self.env['hotel.room.type']
        return apidata.rm_get_prices(start_date, time_interval, number_intervals, room_type, guest_number)

        # Debug Stop -------------------
        # import wdb; wdb.set_trace()
        # Debug Stop -------------------