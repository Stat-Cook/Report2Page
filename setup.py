import setuptools
setuptools.setup(
    name='Report2Page',
    version='0.2',
    author='Robert Cook',
    description='',
    packages=['report2page'],
    entry_points = '''
        [console_scripts]
        report_cli=report2page.cli:report_cli
    ''',
    install_requires=[
        'setuptools',
        'pandas >= 0.22.0',
        'numpy >= 1.16.0',
        "pyyaml",
        "dominate"
    ],
    python_requires='>=3.5'
)
