package br.inatel.cdg.test;
import java.util.ArrayList;

import br.inatel.cdg.ProfessorService;
import br.inatel.cdg.test.ProfessorConst;

@SuppressWarnings("unused")
public class MockProfessorService implements ProfessorService{

     @Override
    public String busca(String nome) {

        if (nome == "Soned"){
            return ProfessorConst.Soned;
        }else if (nome == "Chris"){
            return ProfessorConst.Chris;
        }else if(nome == "Yvo"){
            return ProfessorConst.Yvo;
        }else if(nome == "Marcelo"){
            return ProfessorConst.Marcelo;
        }else if(nome == "Guilherme"){
            return ProfessorConst.Guilherme;
        }else if ( nome == "Estevan") {
            return ProfessorConst.Estevan;
        }else if ( nome == "Rodrigo") {
            return ProfessorConst.Rodrigo;
        }else if ( nome == "Renan") {
            return ProfessorConst.Renan;
        }else if ( nome == "Bruno") {
            return ProfessorConst.Bruno;
        }else return ProfessorConst.Invalida;
    }


}