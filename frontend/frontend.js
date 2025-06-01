function mostrarForm(){
    principal = document.getElementById("principal");
    tarefas = document.getElementById("telaLista");
    tarefas.style.visibility = "hidden";
    principal.style.visibility = "visible";
}

function limparForm(){
    document.getElementById("idTarefa").value = "";
    document.getElementById("name").value = "";
    document.getElementById("status").value = "";
}

function mostrarLista(data){
    principal = document.getElementById("principal");
    tarefas = document.getElementById("telaLista");
    tarefas.style.visibility = "visible";
    principal.style.visibility = "hidden";
    
    lista = document.getElementById("containerLista");
    data.forEach((tarefa) => {
        var div = document.createElement('div');
        feito = tarefa.done ? "Completa":"Incompleta"
        div.textContent = `ID:${tarefa.id.toString().padEnd(5)}|Titulo:${tarefa.title.toString().padEnd(20)}|Status:${feito}`;
        div.className = "tarefa";
        lista.appendChild(div);
    });
}

function mostrarCarregando(){
    carregando = document.getElementById("carregando");
    carregando.style.visibility = "visible";
}

function esconderCarregando(){
    carregando = document.getElementById("carregando");
    carregando.style.visibility = "hidden";
}
