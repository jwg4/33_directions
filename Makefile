all: cube.pdf

cube.pdf: cube.tex planes.tex
	pdflatex cube.tex

planes.tex: make_drawing_code.py
	python make_drawing_code.py

test: test_drawing.py test_geometry.py geometry.py drawing.py
	python -m unittest discover
