from flask import Flask, jsonify, request

app = Flask(__name__)

coisas = [
    {"id": 1, " nome": "arroz 5kg", "quantidade": 2, "categoria": "aimentos", "prioridade": "alta", "comprado": False},
    {"id": 2, " nome": "feijao 1kg", "quantidade": 10, "categoria": "aimentos", "prioridade": "alta", "comprado": False}

]

@app.route("/compras",methods=["GET"])
def get_compras():
    return jsonify({"mensagem": "lista de compras", "itens":coisas, "total": len (coisas)})

@app.route("/compras/<int:id>", methods=["GET"])
def get_compra_by_id(id):
    for  coisa in coisas:
        if coisas ["id"] == id:
            return jsonify({"mensagem": "item encontrado", "item": coisas(id)})
    return jsonify({"mensagem": "itemnao encontrado"}), 404

@app.route("/compras", methods= ["POST"])
def add_item():
    novo_item = request.json

    novo_item["id"] = len(coisas) + 1
    coisas.append(novo_item)
    return jsonify ({"mensagem": "item cadastrado!", "item": novo_item})

@app.route("/compras/<int:id>", methods=["PUT"])
def update_item(id):
    dados = request.json

    for coisa in coisas:
        if coisa["id"] == id:
            coisa.update(dados)
            return jsonify({"mensagem": "item atualizado!"})
       
    return jsonify({"mensagem": "item nao encontrado!"}),404
       
@app.route("/compras/<int:id>", methods=["DELETE"])
def delete_musica(id):
    for coisa in coisas:
        if coisa["id"] == id:
          coisas.remove(coisa)
          
        return jsonify ( {"mensagem": "item deletado"})



if __name__ == '__main__':
    app.run(debug=True)

