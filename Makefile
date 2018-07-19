all: cube.pdf

cube.pdf: cube.tex planes.tex
	pdflatex cube.tex

PY_MODULES = geometry.py drawing.py color.py points.py

planes.tex: make_drawing_code.py $(PY_MODULES)
	python make_drawing_code.py

TEST_MODULES = test_drawing.py test_geometry.py

test: $(TEST_MODULES) $(PY_MODULES)
	python -m unittest discover
