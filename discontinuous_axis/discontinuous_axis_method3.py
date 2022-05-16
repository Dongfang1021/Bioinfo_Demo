from matplotlib import pyplot as plt
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
import numpy as np

def CustomScaleFactory(l, u):
    class CustomScale(mscale.ScaleBase):
        name = 'custom'

        def __init__(self, axis, **kwargs):
            mscale.ScaleBase.__init__(self)
            self.thresh = None #thresh

        def get_transform(self):
            return self.CustomTransform(self.thresh)

        def set_default_locators_and_formatters(self, axis):
            pass

        class CustomTransform(mtransforms.Transform):
            input_dims = 1
            output_dims = 1
            is_separable = True
            lower = l
            upper = u
            def __init__(self, thresh):
                mtransforms.Transform.__init__(self)
                self.thresh = thresh

            def transform(self, a):
                aa = a.copy()
                aa[a>self.lower] = a[a>self.lower]-(self.upper-self.lower)
                aa[(a>self.lower)&(a<self.upper)] = self.lower
                return aa

            def inverted(self):
                return CustomScale.InvertedCustomTransform(self.thresh)

        class InvertedCustomTransform(mtransforms.Transform):
            input_dims = 1
            output_dims = 1
            is_separable = True
            lower = l
            upper = u

            def __init__(self, thresh):
                mtransforms.Transform.__init__(self)
                self.thresh = thresh

            def transform(self, a):
                aa = a.copy()
                aa[a>self.lower] = a[a>self.lower]+(self.upper-self.lower)
                return aa

            def inverted(self):
                return CustomScale.CustomTransform(self.thresh)

    return CustomScale

mscale.register_scale(CustomScaleFactory(1.12, 8.88))

x = np.concatenate((np.linspace(0,1,10), np.linspace(9,10,10)))
xticks = np.concatenate((np.linspace(0,1,6), np.linspace(9,10,6)))
y = np.sin(x)
plt.plot(x, y, '.')
ax = plt.gca()
#ax.set_xscale('custom')
ax.set_xticks(xticks)
plt.savefig("discontinuous_axis_method3.png")