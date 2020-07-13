from abm_buyer_seller.model import WasteModel
import multiprocessing as mp
import numpy as np
from time import time
import matplotlib.pyplot as plt
from mesa.batchrunner import BatchRunner


# model = WasteModel(10, 1, 1)
# # model.schedule.print_lists()
# print(model)
# model.step()
# print(model)

# np.random.RandomState(100)
# arr = np.random.randint(0, 10, size=[200000, 5])
# data = arr.tolist()
# data[:5]

# seller_goods = [s[2].goods_left for s in model.schedule.sellers]
# plt.hist(seller_goods)
# buyer_money = [b[2].money_left for b in model.schedule.buyers]

def compute_recycling_rate(model) -> float:
    print('RUN')
    return model.total_waste_traded / model.total_waste_produced


fixed_params = {'width': 1, 'height': 1}
variable_params = {'num_per_agent': range(1, 2)}
batch_run = BatchRunner(WasteModel, variable_params, fixed_params,
                        iterations=1, max_steps=2, model_reporters={'Recycling_Rate': compute_recycling_rate})
batch_run.run_all()
run_data = batch_run.get_model_vars_dataframe()
run_data.head()
plt.scatter([1], run_data.Recycling_Rate)
plt.show()

# plt.hist(buyer_money)
# plt.show()



