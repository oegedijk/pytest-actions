from setuptools import setup, find_packages

setup(
    name='pytest-actions',
    version='0.1',
    license='MIT',
    packages=find_packages(),
    install_requires=['dash', 'dash-bootstrap-components', 'jupyter_dash', 'dash-auth',
                    'dtreeviz>=1.0', 'numpy', 'pandas', 'PDPbox', 'scikit-learn', 
                    'shap>=0.36', 'shortuuid', 'joblib', 'oyaml', 'click'],
    author='Oege Dijk',
    author_email='oegedijk@gmail.com',
)
