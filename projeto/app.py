import os
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import datetime




app=Flask(__name__)


#db_path = os.path.join(os.getcwd(), 'site.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:YKGAvBXcEUoJCtjcuFUldKPidiTyGmzV@postgres.railway.internal:5432/railway'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = 'static/img'
app.secret_key="curso_flask"
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=900)

#tabelas
class Pessoas(db.Model):
   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   nome = db.Column(db.String(100), nullable = False)
   telefone = db.Column(db.String(11), unique = True, nullable = False)
  

class Ovos(db.Model):
    id_ovos = db.Column(db.Integer, primary_key = True,  autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)
    categoria = db.Column(db.String(100), nullable = False)
    preco = db.Column(db.Integer, nullable = False)
    peso = db.Column(db.Integer, nullable = False)

class CarrinhoTresSabores(db.Model):
    id_ovos = db.Column(db.Integer, primary_key = True,  autoincrement = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)
    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'), nullable=False)
    ovo_id = db.Column(db.Integer, db.ForeignKey('ovos.id_ovos'), nullable=False)
    nome = db.Column(db.String(100), nullable = False)
    peso = db.Column(db.Integer, nullable = False)
    quantidade = db.Column(db.Integer, nullable = False)
    categoria = db.Column(db.String(100), nullable = False)
    
   
   
 

   
    
class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)
    id_ovos = db.Column(db.Integer, db.ForeignKey('ovos.id_ovos'), nullable=False)

    # Relações
    usuario = db.relationship('Pessoas', backref=db.backref('carrinho', lazy=True))
    ovo = db.relationship('Ovos', backref=db.backref('carrinho', lazy = True)) 

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)
    total_pagar = db.Column(db.Integer, nullable = False)
    
    
    # Relações
    usuario = db.relationship('Pessoas', backref=db.backref('pedidos', lazy=True))
   

class PedidoFeitos(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    

    # Relações
    usuario = db.relationship('Pessoas', backref=db.backref('pedidosFeitos', lazy=True))
    pedidos = db.relationship('Pedido', backref=db.backref('pedidosFeitos', lazy = True))

class PedidoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    nome_ovo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    nome_usuario = db.Column(db.String(100), nullable=False)
    preco_ovo = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

class PedidoKit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    nome_ovo = db.Column(db.String(100), nullable=False)
    nome_usuario = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    
   


class PedidoPago(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)
    nome_usuario = db.Column(db.String(100), nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    total_pago = db.Column(db.Integer, nullable=False)
    

    # Relações
    usuario = db.relationship('Pessoas', backref=db.backref('pedidosPago', lazy=True))
    pedidos = db.relationship('Pedido', backref=db.backref('pedidosPago', lazy = True))



with app.app_context():  
    
    db.drop_all() #apaga todos os dados
    db.create_all()  

@app.route('/')
def principal():
    return render_template("principal.html")

@app.route('/itens')
def pag_itens():
   
    ovos = Ovos.query.all()
    return render_template("itens.html", ovos = ovos)

@app.route('/formulario')
def formulario():
    return render_template("login.html")

@app.route('/cadastrar', methods = ['POST'])
def cadastrar():
    nome = request.form.get('nome')
    telefone_original = request.form.get('telefone')
    nome_ajustado = nome.lower()
    telefone = telefone_original.replace(" ","")
    print(telefone)
    pessoa = Pessoas.query.filter_by(telefone = telefone).first()
    if pessoa:
        flash("Esse numero de telefone ja esta cadastrado")
        return redirect('/formulario')
    pessoa_nova = Pessoas(nome = nome_ajustado, telefone = telefone)
    db.session.add(pessoa_nova)
    db.session.commit()

    return redirect('/formulario')


@app.route('/login', methods = ['POST'])
def login():
    nome = request.form.get('nome-login')
    telefone_original = request.form.get('telefone-login')
    nome_ajustado = nome.lower()
    telefone = telefone_original.replace(" ","")
    print(telefone)

    usuario = Pessoas.query.filter_by(nome = nome_ajustado, telefone = telefone).first()

    if nome == 'hahahshdiknxwduicfoewdqwiudmnowqieudhw' and telefone == '16992992992':
        session['adm'] = True
        return redirect('/gerenciamento')
    if usuario:
        session['id'] = usuario.id
        session['nome'] = nome
        session['logado'] = True
        return redirect('/')

    else:
        flash("Dados incorretos")
        return redirect('/formulario')


@app.route('/gerenciamento')
def gerenciamento():
   if 'adm' not in session:
      return redirect('/formulario')
   bancoDados = Pessoas.query.all()
   cardapio = Ovos.query.all()
   carrinho = Carrinho.query.all()
   pedido = Pedido.query.all()
   pedidoItem = PedidoItem.query.all()
   pedidoPago = PedidoPago.query.all()
   carrinho_kits = CarrinhoTresSabores.query.all()
   total_pagar = sum(item.total_pagar for item in pedido)
   total_pago = sum(item.total_pago for item in pedidoPago)
   


   return render_template("gerenciamento.html", bancoDados =bancoDados ,
                           carrinho = carrinho, 
                           pedido = pedido, 
                           pedidoItem = pedidoItem, 
                           pedidoPago = pedidoPago,
                           cardapio = cardapio,
                           total_pagar = total_pagar,
                           total_pago = total_pago,
                           carrinho_kits = carrinho_kits)

@app.route('/remover_ovo/<int:id_ovos>', methods=['POST'])
def remover_ovo(id_ovos):
    print(id_ovos)
    ovo = Ovos.query.get(id_ovos)
    carrinho = Carrinho.query.filter_by(id_ovos = id_ovos).all()
    pedido = PedidoItem.query.filter_by(nome_ovo = ovo.nome).all()


    print("entrou")
    
    if carrinho:
         print("entrou aqui")
         for item in carrinho:
            db.session.delete(item)
         db.session.commit()
    if pedido:
         print("entrou aqui")
         for item in pedido:
            db.session.delete(item)
         db.session.commit()
    if ovo:
        print("entrou aqui")
        db.session.delete(ovo)
        db.session.commit()
    return redirect ('/gerenciamento')

@app.route('/ovo_trufado', methods = ['POST'])
def ovos_trufados():
    if 'adm' not in session:
      return redirect('/formulario')
    nome = request.form.get('nome_trufado')
    preco = request.form.get('preco_trufado')
    peso = request.form.get('peso_trufado')

   
    ovo = Ovos(nome = nome, preco = preco, categoria = 'trufado', peso = peso)

    
    db.session.add(ovo)

    db.session.commit()

    return redirect('/gerenciamento')
@app.route('/ovo_kit', methods = ['POST'])
def ovos_kit():
    if 'adm' not in session:
      return redirect('/formulario')
    nome = request.form.get('nome_kit')
    preco = request.form.get('preco_kit')
    peso = request.form.get('peso_kit')

   
    ovo = Ovos(nome = nome, preco = preco, categoria = nome, peso = peso)

    
    db.session.add(ovo)

    db.session.commit()

    return redirect('/gerenciamento')


@app.route('/ovo_recheado', methods = ['POST'])
def ovo_recheado():
    if 'adm' not in session:
      return redirect('/formulario')
    nome = request.form.get('nome_recheado')
    preco = request.form.get('preco_recheado')
    peso = request.form.get('peso_recheado')

   
    ovo = Ovos(nome = nome, preco = preco, categoria = 'recheado', peso = peso)

    
    db.session.add(ovo)

    db.session.commit()

    return redirect('/gerenciamento')
@app.route('/ovo_degustacao', methods = ['POST'])
def ovo_degustacao():
    if 'adm' not in session:
      return redirect('/formulario')
    nome = request.form.get('nome_degustacao')
    preco = request.form.get('preco_degustacao')
    peso = request.form.get('peso_degustacao')

    
    ovo = Ovos(nome = nome, preco = preco, categoria = 'degustacao', peso = peso)

   
    db.session.add(ovo)

    db.session.commit()

    return redirect('/gerenciamento')

@app.route('/carrinho')
def pag_carrinho():
    if 'logado' not in session:
      return redirect('/formulario')
    print(session['id'])
    carrinho_item = Carrinho.query.filter_by(id_usuario = session['id']).all()
    total = sum(item.ovo.preco for item in carrinho_item)
    return render_template("carrinho.html", carrinho = carrinho_item, total = total)

@app.route('/adiciona_carrinho/<int:id_ovos>')
def adiciona_carrinho(id_ovos):
   if 'logado' not in session:
      return redirect('/formulario')
   session['enviado'] = False
   ovo_carrinho = Ovos.query.filter_by(id_ovos = id_ovos).first()
   usuario_carrinho = Pessoas.query.filter_by(id = session['id']).first()
   carrinho_item = Carrinho(id_usuario = usuario_carrinho.id, id_ovos = ovo_carrinho.id_ovos)
   db.session.add(carrinho_item)
   db.session.commit()

   return redirect('/itens')
@app.route('/adicionar_ao_carrinho/<categoria>', methods=['POST'])
def adicionar_ao_carrinho(categoria):
    
    if 'logado' not in session:
      return redirect('/formulario')
    session['enviado'] = False
    quantidades = request.form.to_dict()  # Pega os dados como um dicionário
    print("Quantidades recebidas:", quantidades)

    usuario_carrinho = Pessoas.query.filter_by(id=session['id']).first()
    ovo_carrinho = Ovos.query.filter_by(categoria=categoria).first()
    carrinho = Carrinho(id_usuario = usuario_carrinho.id, id_ovos = ovo_carrinho.id_ovos)
    db.session.add(carrinho)

    for produto_id, quantidade in quantidades.items():
        ovo_id = produto_id.split('[')[1].split(']')[0]  # Extrai o ID do ovo
        quantidade_value = int(quantidade)  # Pega a quantidade

        print(f'Ovo ID: {ovo_id}, Quantidade: {quantidade_value}')

        produto = Ovos.query.get(ovo_id)  # Buscar o ovo com base no ID

        if produto and quantidade_value > 0:
            carrinho_item = CarrinhoTresSabores.query.filter_by(ovo_id=produto.id_ovos, id_carrinho = carrinho.id).first()

            if carrinho_item:
                carrinho_item.quantidade += quantidade_value  # Incrementa a quantidade se o produto já está no carrinho
            else:
                carrinho_item = CarrinhoTresSabores(ovo_id=produto.id_ovos, quantidade=quantidade_value, id_carrinho=carrinho.id, id_usuario = session['id'], nome = produto.nome, peso = produto.peso, categoria = categoria)
                db.session.add(carrinho_item)

    db.session.commit()
    return redirect('/itens')
@app.route('/remove_carrinho/<int:id>')
def remove_carrinho(id):
     if 'logado' not in session:
        return redirect('/formulario')
     
     carrinho = Carrinho.query.filter_by(id = id).first()
     print(carrinho)
     carrinho_kit = CarrinhoTresSabores.query.filter_by(id_carrinho = id).all()
     print(carrinho_kit)
     if carrinho_kit:
         for item in carrinho_kit: #for importante, pois carrinho kit retorna todos, ou seja, uma lista. Não é possivel deletar diretamente como: db.session.delete(carrinho_item)
            db.session.delete(item)
     db.session.commit()
     if carrinho:
        db.session.delete(carrinho)
    
     db.session.commit()
     return redirect('/carrinho')

@app.route('/finalizar_pedido')
def finalizar_pedido():
    if 'logado' not in session:
      return redirect('/formulario')

    carrinho_itens = Carrinho.query.filter_by(id_usuario= session['id']).all()
    carrinho_kits = CarrinhoTresSabores.query.filter_by(id_usuario = session['id']).all()
    total_pagar = sum(item.ovo.preco for item in carrinho_itens)

       

    print(total_pagar)
   

   
    novo_pedido = Pedido(id_usuario=session['id'], total_pagar = total_pagar )
    usuario = Pessoas.query.filter_by(id=session['id']).first()
    db.session.add(novo_pedido)
    db.session.commit()  

    for item in carrinho_itens:
        ovo = Ovos.query.get(item.id_ovos)
        print(ovo.nome)
        pedido = PedidoItem.query.filter_by(id_pedido = novo_pedido.id, nome_ovo = ovo.nome).first()
        if pedido:
             pedido.quantidade +=1
             pedido.preco_ovo += ovo.preco
        elif ovo.nome == ovo.categoria:
            print('nada')
        
        else:
            quantidade_total = 1
            pedido_item = PedidoItem(id_pedido=novo_pedido.id, nome_ovo=ovo.nome, preco_ovo = ovo.preco, nome_usuario = usuario.nome, categoria = ovo.categoria, quantidade = quantidade_total)
            db.session.add(pedido_item)
    for item in carrinho_kits:
        ovo = Ovos.query.get(item.id_ovos)
        ovo_categoria = Ovos.query.filter_by(categoria = item.categoria).first()
        pedido_item = PedidoItem(id_pedido=novo_pedido.id, nome_ovo=item.nome, preco_ovo = ovo_categoria.preco, nome_usuario = usuario.nome, categoria = item.categoria, quantidade = item.quantidade)
        db.session.add(pedido_item)

    db.session.commit()  

    CarrinhoTresSabores.query.filter_by(id_usuario=session['id']).delete()
    Carrinho.query.filter_by(id_usuario=session['id']).delete()
   
    db.session.commit()
    session['enviado'] = True
    return redirect('/carrinho')


@app.route('/pedido_pago/<int:id_pedido>', methods=['POST'])
def pedido_pago(id_pedido):
    
    if 'adm' not in session:
      return redirect('/formulario')
    pedido = Pedido.query.filter_by(id = id_pedido).first()
    usuario = Pessoas.query.filter_by(id = pedido.id_usuario).first()
    pedidoPago = PedidoPago(id_usuario = pedido.id_usuario, nome_usuario = usuario.nome, id_pedido = pedido.id, total_pago = pedido.total_pagar)
    
    db.session.add(pedidoPago)
    db.session.commit()

    Pedido.query.filter_by(id = id_pedido).delete()
    db.session.commit()

    return redirect('/gerenciamento')

@app.route('/logout')
def logout():
    if 'logado' not in session:
      return redirect('/formulario')
    session.pop('nome', default=None)
    session.pop('logado', default=None)
    session.pop('enviado', default=None)
    session.pop('id', default=None)
    session.pop('adm', default=None)
    return redirect('/formulario')
@app.route('/logoutADM')
def logoutADM():
    if 'adm' not in session:
      return redirect('/formulario')
    session.pop('adm', default=None)
    return redirect('/formulario')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)