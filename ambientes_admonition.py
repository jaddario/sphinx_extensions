from docutils import nodes
from docutils.nodes import Element
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

import sphinx
from sphinx.environment import NoUri
from sphinx.locale import _
from sphinx.util import logging
from sphinx.util.nodes import set_source_info
from sphinx.util.texescape import tex_escape_map

if False:
    from typing import Any, Dict, Iterable, List  
    from sphinx.application import Sphinx  
    from sphinx.environment import BuildEnvironment  

logger = logging.getLogger(__name__)


class todo_node(nodes.Admonition, nodes.Element):
    pass

class ParaProfessor(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(ParaProfessor, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Para o professor')))
        
        env = self.state.document.settings.env
    
        return [todo]

class Atividades(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(Atividades, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Atividades')))
        
        env = self.state.document.settings.env
    
        return [todo]

class Observacao(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(Observacao, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        env = self.state.document.settings.env
    
        return [todo]

class ParaRefletir(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(ParaRefletir, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Para Refletir')))
        
        env = self.state.document.settings.env
    
        return [todo]

class Exercicio(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(Exercicio, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Exercicio')))
        
        env = self.state.document.settings.env
        
        return [todo]

class Exemplo(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(Exemplo, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Exemplo')))
        
        env = self.state.document.settings.env
        
        return [todo]

class VoceSabia(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(VoceSabia, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Voce Sabia?')))
        
        env = self.state.document.settings.env
        
        return [todo]

class ParaPesquisar(BaseAdmonition):
    node_class = todo_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }
    
    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-todo']

        (todo,) = super(ParaPesquisar, self).run()
        if isinstance(todo, nodes.system_message):
            return [todo]

        todo.insert(0, nodes.title(text=_('Para Pesquisar')))
        
        env = self.state.document.settings.env
        
        return [todo]



def visit_todo_node(self, node):
    self.visit_admonition(node)
    

def depart_todo_node(self, node):
    self.depart_admonition(node)


def latex_visit_todo_node(self, node):
    
    title = node.pop(0).astext().translate(tex_escape_map)
    self.body.append(u'\n\\begin{professor}{')

    target = node.get('targetref')
    if target is not None:
        self.body.append(u'\\label{%s}' % target)
    self.body.append('%s:}' % title)


def latex_depart_todo_node(self, node):
    self.body.append('\\end{professor}\n')

def setup(app):

    app.add_event('todo-defined')
    app.add_config_value('todo_include_todos', False, 'html')
    app.add_config_value('todo_link_only', False, 'html')
    app.add_config_value('todo_emit_warnings', False, 'html')

    app.add_node(todo_node,
                 html=(visit_todo_node, depart_todo_node),
                 latex=(latex_visit_todo_node, latex_depart_todo_node),
                 text=(visit_todo_node, depart_todo_node),
                 man=(visit_todo_node, depart_todo_node),
                 texinfo=(visit_todo_node, depart_todo_node))

    app.add_directive('paraoprofessor', ParaProfessor)
    app.add_directive('atividades', Atividades)
    app.add_directive('observacao', Observacao)
    app.add_directive('pararefletir', ParaRefletir)
    app.add_directive('exercicio', Exercicio)
    app.add_directive('exemplo', Exemplo)
    app.add_directive('vocesabia', VoceSabia)
    app.add_directive('parapesquisar', ParaPesquisar)
    
    return {
        'version': sphinx.__display_version__,
        'env_version': 1,
        'parallel_read_safe': True
}