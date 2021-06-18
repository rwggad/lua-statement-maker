from lua_ctx_base import LuaCtxBase


class LuaIfBranch(LuaCtxBase):
    """ Lua If Branch Context """
    def __init__(self, directive, expr=''):
        self.__directive = directive
        self.__expression = expr
        self.__statements = []
        self.next = None

    def append(self, statement):
        self.__statements.append(statement)
        return self.__statements

    def extend(self, statements):
        self.__statements.extend(statements)
        return self.__statements

    def append_next_branch(self, branch):
        if not isinstance(branch, LuaIfBranch):
            raise InternalError(
                'Invalid instance type (need \'LuaIfBranch\' Type')

        curr = self
        while True:
            if not curr.next:
                break
            curr = curr.next
        curr.next = branch

    def make_stmt(self, indent_cnt=1):
        indent = ((' ' * self.BASE_INDENT) * indent_cnt)

        branches = []
        if self.__directive in ['if', 'elseif']:
            branches.append(
                '{indent}{directive} {expression} then'.format(
                    indent=indent,
                    directive=self.__directive,
                    expression=self.__expression))

        else:
            branches.append(
                '{indent}{directive}'.format(
                    indent=indent,
                    directive=self.__directive))

        for _stmt in self.__statements:
            if isinstance(_stmt, LuaCtxBase):
                branches.append(
                    _stmt.make_stmt(indent_cnt + 1))

            else:
                branches.append(
                    '{indent}{statement}'.format(
                        indent = ((' ' * self.BASE_INDENT) * (indent_cnt + 1)),
                        statement=_stmt))

        if self.next:
            branches.append(
                self.next.make_stmt(indent_cnt))

        return '\n'.join(branches)


class LuaIfCtx(LuaIfBranch):
    """ Lua If Context

        Usage.
          lua_if_ctx_1 = LuaIfCtx('expr_1')
          lua_if_ctx_1.append('stmt_1')
          lua_elseif_ctx_1 = lua_if_ctx_1.append_elseif('expr_2')
          lua_elseif_ctx_1.append('stmt_2')
          lua_else_ctx_1 = lua_if_ctx_1.append_else()
          lua_else_ctx_1.append('stmt_3')
          lua_if_ctx.make_stmt()

        Result.
          if expr_1 then
              stmt_1
          elseif expr_2 then
              stmt_2
          else
              stmt_3
          end
    """
    def __init__(self, expr):
        super(LuaIfCtx, self).__init__('if', expr)

    def append_elseif(self, expr):
        elseif_ctx = LuaIfBranch('elseif', expr)
        self.append_next_branch(elseif_ctx)
        return elseif_ctx

    def append_else(self):
        else_ctx = LuaIfBranch('else')
        self.append_next_branch(else_ctx)
        return else_ctx

    def make_stmt(self, indent_cnt=1):
        indent = ((' ' * self.BASE_INDENT) * indent_cnt)

        indentation_statements = []
        indentation_statements.append(
            super(LuaIfCtx, self).make_stmt(indent_cnt))

        indentation_statements.append(
            '{indent}end\n'.format(indent=indent))

        return '\n'.join(indentation_statements)
