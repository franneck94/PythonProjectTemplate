cd documentation
call sphinx-apidoc -o source/ ../fastvector/
call make html
cd ..