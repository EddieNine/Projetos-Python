from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])

# usuario = Usuario.create(nome="Programador", email="teste@gmail.com", senha="123456")

# print("Novo usuario:", usuario.id, usuario.nome, usuario.email)

# Usuario.create(nome="Guilherme", email="gui@gmail.com", senha="123456")
# Usuario.create(nome="João", email="joao@gmail.com", senha="123456")
# Usuario.create(nome="Maria", email="maria@gmail.com", senha="123456")

# lista_usuarios = Usuario.select()
# print("Listando usuarios:")

# for u in lista_usuarios:
#    print('-', u.id, u.nome, u.email)

# usuario1 = Usuario.get(Usuario.id == 1)
# print("usuario pelo id:", usuario1.id, usuario1.nome)
