from setuptools import setup

def main():
    setup(
        name='prettycolors',
        version='1.0.0',
        packages=['prettycolors'],
        install_requires=['numpy'],
        test_suite='nose.collector',
        tests_require=['nose', 'matplotlib'],
    )

if __name__ == '__main__':
    main()
