from package.lua_ctx import *
from package.lua_if_ctx import *


def main():
    """ Result.

        local test1
        local test2
        if expr___1 then
            if expr__1 then
                stmt__1
                if expr_1 then
                    stmt_1
                    stmt_2
                elseif expr_2 then
                    stmt_3
                    stmt_4
                else
                    stmt_5
                end

                stmt__2
            elseif expr__2 then
                stmt__2
            end

        end
    """
    # nomal
    lua_ctx = LuaCtx()
    lua_ctx.append('local test1')
    lua_ctx.append('local test2')
    print lua_ctx.make_stmt()

    # if statement 1
    lua_if_ctx_1 = LuaIfCtx('expr_1')
    lua_if_ctx_1.append('stmt_1')
    lua_if_ctx_1.append('stmt_2')
    lua_elseif_ctx_1 = lua_if_ctx_1.append_elseif('expr_2')
    lua_elseif_ctx_1.append('stmt_3')
    lua_elseif_ctx_1.append('stmt_4')
    lua_else_ctx_1 = lua_if_ctx_1.append_else()
    lua_else_ctx_1.append('stmt_5')

    # if statement 2
    lua_if_ctx_2 = LuaIfCtx('expr__1')
    lua_if_ctx_2.append('stmt__1')
    lua_if_ctx_2.append(lua_if_ctx_1)
    lua_if_ctx_2.append('stmt__2')
    lua_elseif_ctx_2 = lua_if_ctx_2.append_elseif('expr__2')
    lua_elseif_ctx_2.append('stmt__2')

    # if statement 3
    lua_if_ctx_3 = LuaIfCtx('expr___1')
    lua_if_ctx_3.append(lua_if_ctx_2)
    print lua_if_ctx_3.make_stmt()


if __name__ == "__main__":
    main()
