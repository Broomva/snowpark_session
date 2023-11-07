#%%
from snowpark_session import SnowparkSession

# %%
spark = SnowparkSession().get_session()

# %%
sdf = spark.read.table("samples.nyctaxi.trips")
print(sdf.show())
# %%

from snowpark_session import AzureMLFlowSession

# %%
mlflow_session = AzureMLFlowSession().get_session()

# %%
print(mlflow_session.client.MlflowClient())
# %%
