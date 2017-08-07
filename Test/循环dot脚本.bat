for /L  %%i in (0,1,59) do dot -Tpdf %%i.dot -o %%i.pdf
	pause

