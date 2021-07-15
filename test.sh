python3 -m doctest docs/*.md &&\
    python3 -m unittest discover -v &&\
    mypy foliant/contrib/chapters.py --ignore-missing-imports
