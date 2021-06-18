from lua_ctx_base import LuaCtxBase


class LuaCtx(LuaCtxBase):
    """ Lua Context

        Usage.
          lua_ctx = LuaCtx()
          lua_ctx.append('local var test1')
          lua_ctx.append('local var test2')
          lua_ctx.make_stmt()

        Result.
          local var test1
          local var test2
    """
    def __init__(self):
        self.__statements = []

    def append(self, statement):
        self.__statements.append(statement)
        return self.__statements

    def extend(self, statements):
        self.__statements.extend(statements)
        return self.__statements

    def make_stmt(self, indent_cnt=1):
        indent = ((' ' * self.BASE_INDENT) * indent_cnt)

        indentation_statements = []
        for _statement in self.__statements:
            indentation_statements.append(
                '{indent}{statement}'.format(indent=indent,
                                             statement=_statement))

        return '\n'.join(indentation_statements)
