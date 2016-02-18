##!/usr/bin/env python3

import time
from decimal import Decimal

from supplychainpy import model_inventory
from supplychainpy.model_inventory import analyse_orders_abcxyz_from_file, analyse_orders_from_file_row, analyse_orders, \
    analyse_orders_from_file_col, analyse_orders_np
from supplychainpy.demand import summarise_demand
from supplychainpy.demand import forecast_demand
from supplychainpy.enum_formats import PeriodFormats
import numpy as np
from supplychainpy.model_inventory import analyse_orders

__author__ = 'kevin'


def main():
    # end_time = time.time()
    # secs = end_time - start_time
    # print("model_orders took {:.5f} seconds to run".format(secs))
    # summary = analyse_orders_from_file_col('test.txt', 'RX9887-90', 4, 45, 400, 1.28)
    # print(summary)
    # start_time = time.time()
    # big_summary = analyse_orders_from_file_row('data.csv', 1.28, 400, file_type="csv")
    # print(big_summary)
    # end_time = time.time()
    # secs = end_time - start_time
    # print('model_orders took {:.5f} seconds to run'.format(secs))
    # start_time = time.time()
    # abc = analyse_orders_abcxyz_from_file('data.csv', 1.28, 5000, file_type="csv")
    # for sku in abc.orders:
    #     print(sku.orders_summary())
    # print(abc.abcxyz_summary)
    # end_time = time.time()
    # secs = end_time - start_time
    # print('model_orders took {:.5f} seconds to run'.format(secs))
    orders1 = [1, 3, 5, 67, 4, 65, 44, 50, 48, 24, 34, 20]
    orders2 = [1, 3, 5, 67, 4, 65, 44, 50, 48, 24, 34, 20]
    weights = [.5, .3, .2]
    forecast = forecast_demand.Forecast(orders1)
    print(orders1)
    forecast.weighted_moving_average_forecast(weights=weights, average_period=3, forecast_length=9,
                                              start_position=3)
    print(forecast.weighted_moving_average)

    # d.moving_average(forecast_length=3, base_forecast=True, start_position=3)
    # print(d.moving_average_forecast)

    k = forecast_demand.Forecast(orders2)
    k.moving_average_forecast(forecast_length=9, start_position=3, average_period=3)
    print(k.moving_average)
    result_array = k.mean_absolute_deviation(forecast.weighted_moving_average)
    result_array2 = forecast.mean_absolute_deviation(k.moving_average)
    print(result_array)
    print(result_array2)
    print(orders1)
    print(k.moving_average)
    print(forecast.weighted_moving_average)
    # s = np.array([200, 300, 343, 553, 356, 455, 264, 252, 264, 635, 677, 755, 887])
    # analyse_orders_np(unit_cost=300, period=PeriodFormats.months.name, z_value=1.28, orders=s, lead_time=9.00)


if __name__ == '__main__': main()
