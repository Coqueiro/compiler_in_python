import analisador_sintatico as syntax

syntax.lexic.program = open('programa').read()

# for i in range(244):
#     t = syntax.lexic.nextToken()
#     print(syntax.lexic.enums[t])
# print(syntax.lexic.secondaryTokenMap)

syntax.parse()
