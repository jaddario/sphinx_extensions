# sphinx_extensions
Repositório de extensões em sphinx para o projeto Livro Aberto

Como utlizar as extensões?
* baixar o arquivo .py correspondente à extensão. 
* no diretório source da aplicação, criar um diretório e transferir o arquivo .py para lá.
* no arquivo conf.py, utilizar o seguinte comando para importar a extensão:
	
	import sys, os

	sys.path.append(os.path.abspath('nome_do_diretorio_de_extensoes'))

	extensions = [
		...
		'nome_da_extensão',
		...
	]

