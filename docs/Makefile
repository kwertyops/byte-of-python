.PHONY: setup build pdf epub serve publish
setup:
	npm install honkit --save-dev

build:
	npx honkit build . docs --log=debug

pdf:
	npx honkit pdf . byte-of-python.pdf

epub:
	npx honkit epub . byte-of-python.epub

serve:
	npx honkit serve

publish:
	scp -r docs intropython@linux.cs.du.edu:~/public_html/byte-of-python