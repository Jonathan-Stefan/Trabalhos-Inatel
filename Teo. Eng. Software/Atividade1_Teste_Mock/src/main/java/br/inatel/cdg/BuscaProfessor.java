package br.inatel.cdg;

import java.util.ArrayList;
import java.util.List;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class BuscaProfessor {

    ProfessorService professorService;
    
    // construtor da classe (Injeção de dependencia)
    public BuscaProfessor(ProfessorService service){
        this.professorService = service;
    }

    public Professor buscaProfessor(String nome){
        // Chama o serviço para buscar o professor
        String professorJson = professorService.busca(nome);

        // Converte a string JSON em um objeto JSON
        JsonObject jsonObject = JsonParser.parseString(professorJson).getAsJsonObject();

        // Recupera os campos do objeto JSON
        String nomeDoProfessor = jsonObject.get("nome").getAsString();
        String sala = jsonObject.get("sala").getAsString();
        String horarioDeAtendimento = jsonObject.get("horarioDeAtendimento").getAsString();
        String periodo = jsonObject.get("periodo").getAsString();

        // Recupera a lista de prédios
        JsonArray predioArray = jsonObject.getAsJsonArray("predio");
        List<String> predioList = new ArrayList<>();
        for (JsonElement element : predioArray) {
            predioList.add(element.getAsString());
        }

        // Cria e retorna um novo objeto Professor
        return new Professor(nomeDoProfessor, sala, horarioDeAtendimento, periodo, predioList);
    }

}
