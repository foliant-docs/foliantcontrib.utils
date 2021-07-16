python3 -m doctest docs/*.md &&\
    python3 -m unittest discover -v &&\
    mypy foliant/contrib/chapters.py foliant/contrib/combined_options.py foliant/contrib/header_anchors.py
