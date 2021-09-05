html_report:
	pytest --cov-report html:tests/reports/cov_html \
		--cov-report xml:tests/reports/cov.xml \
		--cov-report annotate:tests/annotations/cov_annotate \
		--cov-config=.coveragerc \
		--cov=.

terminal_report:
	pytest --cov-report term \
		--cov-config=.coveragerc \
		--cov=.

doctests:
	pytest --doctest-modules

type_check:
	mypy . --ignore-missing-imports

static_code_analysis:
	flake8

lint:
	black