# %%

from jwst.datamodels import ImageModel, CubeModel

# %%
from glob import glob
# %%
test = glob('./volumes/jwst_data/*/*/*.fits')[0]
# %%
print(test)
# %%
from jwst import datamodels
with datamodels.open(test) as im:
    im.info()
    assert isinstance(im, datamodels.CubeModel)
# %%
from jdaviz import Cubeviz

viz = Cubeviz()

# %%
viz.load_data(im)