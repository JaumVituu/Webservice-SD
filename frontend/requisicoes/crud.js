function encontrar(){
    id = document.getElementById("idTarefa").value;
	titulo = document.getElementById("name");
	feito = document.getElementById("status");
	if (id == ""){
		alert("Preencha o ID para efetuar essa operação");
		return;
	}
	mostrarCarregando();
    const requestOptions = {
      	method: "GET",
      	redirect: "follow"
    };

    fetch(`http://localhost:8000/tasks/${id}`, requestOptions)
      	.then(response => {
			esconderCarregando();
			if (!response.ok) {
				return response.text().then(errorText => {
					return Promise.reject({ status: response.status, message: errorText });
				});
			}
			return response.json();
		})
      	.then(data => {
			console.log(data.result);
			titulo.value = data.title;
			feito.value = data.done;
			alert("Dados apresentados no formulário.");
		})
      	.catch(error => {
			if(error.status == 404){
				alert("Tarefa não encontrada.");
			}
			else{
				alert(error.status)
			}
		});
}

function cadastrar(){
	titulo = document.getElementById("name").value;
	
	if(titulo == ""){
		alert("Preencha o titulo para efetuar essa operação.");
		return;
	}

	mostrarCarregando();
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
		"title": titulo,
    });

    const requestOptions = {
      	method: "POST",
      	headers: myHeaders,
      	body: raw,
      	redirect: "follow"
    };

    fetch("http://localhost:8000/tasks", requestOptions)
      	.then((response) => {
			response.text();
			if(response.status == 201)
				alert("Cadastro efetuado com sucesso");
			else{
				alert("Erro ao cadastar");
			}
			esconderCarregando();
		})
      	.then((result) => console.log(result))
      	.catch((error) => console.error(error));
}

function atualizar(){
	id = document.getElementById("idTarefa").value;
	titulo = document.getElementById("name").value;
	feito = document.getElementById("status").value;
	
	if(id == ""){
		alert("Preencha o ID para efetuar essa operação.");
		return;
	}
	if(titulo == "" && feito == ""){
		alert("Modifique algum dado para realizar essa operação");
		return;
	}

	mostrarCarregando();
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
	var raw; 
	if (titulo == ""){
		raw = JSON.stringify({
			  "id": id,
			"done": feito
		});
	}
	else if(feito == ""){
		raw = JSON.stringify({
			  "id": id,
			"title": titulo
		});
	}
	else{
		raw = JSON.stringify({
			  "id": id,
			"title": titulo,
			"done": feito
		});
	}

    const requestOptions = {
      	method: "PATCH",
      	headers: myHeaders,
      	body: raw,
      	redirect: "follow"
    };

    fetch(`http://localhost:8000/tasks/${id}`, requestOptions)
      	.then((response) => {
			response.text();
			if(response.ok)
				alert("Tarefa atualizada com sucesso");
			else if(response.status == 404){
				alert("ID não cadastrado");
			}
			else{
				alert("Erro ao atualizar");
			}
			esconderCarregando();
		})
      	.then((result) => console.log(result))
      	.catch((error) => console.error(error));
}

function excluir(){
	id = document.getElementById("idTarefa").value;

	if(id == ""){
		alert("Preencha o ID para efetuar essa operação.");
		return;
	}
	const requestOptions = {
		method: "DELETE",
		redirect: "follow"
	};
	mostrarCarregando();
	fetch(`http://localhost:8000/tasks/${id}`, requestOptions)
	.then((response) => {
		response.text();
		if(response.ok){
			limparForm();
			alert("Tarefa excluída com sucesso.");
		}
		else{
			alert("Ocorreu um erro ao excluir a tarefa.");
		}
		esconderCarregando();
	})
	.then((result) => console.log(result))
	.catch((error) => console.error(error));
}

function listar(){
	const requestOptions = {
		method: "GET",
		redirect: "follow"
	};
	mostrarCarregando();
	fetch("http://localhost:8000/tasks", requestOptions)
	.then((response) => {
		esconderCarregando();
		if (!response.ok) {
			return response.text().then(errorText => {
				return Promise.reject({ status: response.status, message: errorText });
			});
		}
		return response.json();
	})
	.then((data) => mostrarLista(data))
	.catch((error) => {
		alert("Não foi possível efetuar essa operação");
	});
}