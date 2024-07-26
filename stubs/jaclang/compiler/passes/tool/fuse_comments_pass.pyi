import jaclang.compiler.absyntree as ast
from _typeshed import Incomplete
from jaclang.compiler.passes import Pass as Pass

class FuseCommentsPass(Pass):
    all_tokens: Incomplete
    comments: Incomplete
    def before_pass(self) -> None: ...
    def exit_node(self, node: ast.AstNode) -> None: ...
    def after_pass(self) -> None: ...

def is_comment_next(cmt: ast.CommentToken, code: ast.Token) -> bool: ...
