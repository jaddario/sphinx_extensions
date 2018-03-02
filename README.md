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

# Modo de usar o ambientes_admonition
A extensão compreende os seguintes ambientes (em parentesis, as respectivas diretivas): 
* Para o professor(paraoprofessor), 
* Atividade(atividade),
* Observação(observacao),
* Para refletir(pararefletir),
* Exercício(exercicio),
* Exemplo(exemplo),
* Você sabia?(vocesabia),
* Para pesquisar(parapesquisar).

Para criar qualquer nota, utilizamos a diretiva como um admonition (atentando-se para a identação).
ex:
>.. paraoprofessor::
>   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
>   ut labore et dolore magna aliqua. Utenim ad minim veniam, quis nostrud exercitation ullamco 
>   laboris nisi ut aliquip ex.

Isso criará a saída no html abaixo:

	<p class="first admonition-title">Para o professor</p>
		<p class="last">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
				ut labore et dolore magna aliqua. Utenim ad minim veniam, quis nostrud exercitation ullamco 
				laboris nisi ut aliquip ex.</p>
	</div>
	   	
