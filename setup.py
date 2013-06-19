from setuptools import setup


setup(
    name='combine-stats',
    version='0.0.1',
    description='Combine multiple pstats files',
    py_modules=['combine_stats'],
    install_requires=['distribute'],
    entry_points=dict(
        console_scripts=[
            'combine-stats = combine_stats:main',
        ],
    ),
)
