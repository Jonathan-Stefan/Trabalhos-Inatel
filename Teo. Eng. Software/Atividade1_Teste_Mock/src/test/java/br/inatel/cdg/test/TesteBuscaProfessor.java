package br.inatel.cdg.test;

import br.inatel.cdg.BuscaProfessor;
import br.inatel.cdg.Professor;
import br.inatel.cdg.ProfessorService;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class TesteBuscaProfessor {

    ProfessorService service;
    BuscaProfessor buscaProfessor;

    @Before
    public void setup(){
        //Criando o contexo do meu teste com o Mock (serviço mock)
        service = new MockProfessorService();
        buscaProfessor = new BuscaProfessor(service);
    }

    @Test
    public void testeBuscaProfessorChris(){

        //Fiz a busca
        Professor chris = buscaProfessor.buscaProfessor("Chris");

        //Faz assertion
        assertEquals("Chris", chris.getNome());
        assertEquals("19:00 - 19:30", chris.getHorarioDeAtendimento());
        assertEquals("noturno", chris.getPeriodo());
        assertEquals("9", chris.getSala());
        assertTrue(chris.getPredio().contains("2"));
    }
    @Test
    public void testeBuscaProfessorSoned(){

        //Fiz a busca
        Professor Soned = buscaProfessor.buscaProfessor("Soned");

        //Faz assertion
        assertEquals("Soned", Soned.getNome());
        assertEquals("10:00 - 11:00", Soned.getHorarioDeAtendimento());
        assertEquals("integral", Soned.getPeriodo());
        assertEquals("4", Soned.getSala());
        assertTrue(Soned.getPredio().contains("1"));
    }
    @Test
    public void testeBuscaProfessorYvo(){

        //Fiz a busca
        Professor Yvo = buscaProfessor.buscaProfessor("Yvo");

        //Faz assertion
        assertEquals("Yvo", Yvo.getNome());
        assertEquals("18:00 - 19:00", Yvo.getHorarioDeAtendimento());
        assertEquals("noturno", Yvo.getPeriodo());
        assertEquals("18", Yvo.getSala());
        assertTrue(Yvo.getPredio().contains("4"));
    }
    @Test
    public void testeBuscaProfessorMarcelo(){

        //Fiz a busca
        Professor Marcelo = buscaProfessor.buscaProfessor("Marcelo");

        //Faz assertion
        assertEquals("Marcelo", Marcelo.getNome());
        assertEquals("17:30 - 19:00", Marcelo.getHorarioDeAtendimento());
        assertEquals("noturno", Marcelo.getPeriodo());
        assertEquals("21", Marcelo.getSala());
        assertTrue(Marcelo.getPredio().contains("5"));
    }
    @Test
    public void testeBuscaProfessorGuilherme(){

        //Fiz a busca
        Professor Guilherme = buscaProfessor.buscaProfessor("Guilherme");

        //Faz assertion
        assertEquals("Guilherme", Guilherme.getNome());
        assertEquals("21:00 - 21:30", Guilherme.getHorarioDeAtendimento());
        assertEquals("noturno", Guilherme.getPeriodo());
        assertEquals("11", Guilherme.getSala());
        assertTrue(Guilherme.getPredio().contains("3"));
    }
    @Test
    public void testeBuscaProfessorEstevan(){

        //Fiz a busca
        Professor Estevan = buscaProfessor.buscaProfessor("Estevan");

        //Faz assertion
        assertEquals("Estevan", Estevan.getNome());
        assertEquals("13:00 - 14:00", Estevan.getHorarioDeAtendimento());
        assertEquals("integral", Estevan.getPeriodo());
        assertEquals("26", Estevan.getSala());
        assertTrue(Estevan.getPredio().contains("6"));
    }
    @Test
    public void testeBuscaProfessorRodrigo(){

        //Fiz a busca
        Professor Rodrigo = buscaProfessor.buscaProfessor("Rodrigo");

        //Faz assertion
        assertEquals("Rodrigo", Rodrigo.getNome());
        assertEquals("08:00 - 09:00", Rodrigo.getHorarioDeAtendimento());
        assertEquals("integral", Rodrigo.getPeriodo());
        assertEquals("5", Rodrigo.getSala());
        assertTrue(Rodrigo.getPredio().contains("1"));
    }
    @Test
    public void testeBuscaProfessorRenan(){

        //Fiz a busca
        Professor Renan = buscaProfessor.buscaProfessor("Renan");

        //Faz assertion
        assertEquals("Renan", Renan.getNome());
        assertEquals("10:00 - 11:00", Renan.getHorarioDeAtendimento());
        assertEquals("integral", Renan.getPeriodo());
        assertEquals("7", Renan.getSala());
        assertTrue(Renan.getPredio().contains("2"));
    }
    @Test
    public void testeBuscaProfessorBruno(){

        //Fiz a busca
        Professor Bruno = buscaProfessor.buscaProfessor("Bruno");

        //Faz assertion
        assertEquals("Bruno", Bruno.getNome());
        assertEquals("13:00 - 14:00", Bruno.getHorarioDeAtendimento());
        assertEquals("integral", Bruno.getPeriodo());
        assertEquals("13", Bruno.getSala());
        assertTrue(Bruno.getPredio().contains("3"));
    }
    @Test
    public void testeBuscaProfessorInvalida(){

        //Fiz a busca
        Professor Invalida = buscaProfessor.buscaProfessor("Jose");

        //Faz assertion
        assertEquals("Entrada invalida", Invalida.getNome());
        assertEquals("-", Invalida.getHorarioDeAtendimento());
        assertEquals("-", Invalida.getPeriodo());
        assertEquals("-", Invalida.getSala());
        assertTrue(Invalida.getPredio().contains("-"));

    }

    // Teste para casos de falhas
    @Test
    public void testeBuscaProfessorFalhaChris(){

        //Fiz a busca
        Professor chris = buscaProfessor.buscaProfessor("Chris");

        //Faz assertion
        assertEquals("Chris", chris.getNome());
        assertEquals("19:00 - 19:30", chris.getHorarioDeAtendimento());
        assertEquals("noturno", chris.getPeriodo());
        assertEquals("9", chris.getSala());
        assertTrue(chris.getPredio().contains("4"));
    }
    @Test
    public void testeBuscaProfessorFalhaSoned(){

        //Fiz a busca
        Professor Soned = buscaProfessor.buscaProfessor("Soned");

        //Faz assertion
        assertEquals("Soned", Soned.getNome());
        assertEquals("15:00 - 16:00", Soned.getHorarioDeAtendimento());
        assertEquals("integral", Soned.getPeriodo());
        assertEquals("4", Soned.getSala());
        assertTrue(Soned.getPredio().contains("1"));
    }
    @Test
    public void testeBuscaProfessorFalhaYvo(){

        //Fiz a busca
        Professor Yvo = buscaProfessor.buscaProfessor("Yvo");

        //Faz assertion
        assertEquals("Yvo", Yvo.getNome());
        assertEquals("18:00 - 19:00", Yvo.getHorarioDeAtendimento());
        assertEquals("noturno", Yvo.getPeriodo());
        assertEquals("2", Yvo.getSala());
        assertTrue(Yvo.getPredio().contains("4"));
    }
    @Test
    public void testeBuscaProfessorFalhaMarcelo(){

        //Fiz a busca
        Professor Marcelo = buscaProfessor.buscaProfessor("Marcelo");

        //Faz assertion
        assertEquals("Vazio", Marcelo.getNome());
        assertEquals("17:30 - 19:00", Marcelo.getHorarioDeAtendimento());
        assertEquals("noturno", Marcelo.getPeriodo());
        assertEquals("21", Marcelo.getSala());
        assertTrue(Marcelo.getPredio().contains("5"));
    }
    @Test
    public void testeBuscaProfessorFalhaGuilherme(){

        //Fiz a busca
        Professor Guilherme = buscaProfessor.buscaProfessor("Guilherme");

        //Faz assertion
        assertEquals("Guilherme", Guilherme.getNome());
        assertEquals("21:00 - 21:30", Guilherme.getHorarioDeAtendimento());
        assertEquals("integral", Guilherme.getPeriodo());
        assertEquals("11", Guilherme.getSala());
        assertTrue(Guilherme.getPredio().contains("3"));
    }
    @Test
    public void testeBuscaProfessorFalhaEstevan(){

        //Fiz a busca
        Professor Estevan = buscaProfessor.buscaProfessor("Estevan");

        //Faz assertion
        assertEquals("Estevan", Estevan.getNome());
        assertEquals("13:00 - 14:00", Estevan.getHorarioDeAtendimento());
        assertEquals("noturno", Estevan.getPeriodo());
        assertEquals("26", Estevan.getSala());
        assertTrue(Estevan.getPredio().contains("6"));
    }
    @Test
    public void testeBuscaProfessorFalhaRodrigo(){

        //Fiz a busca
        Professor Rodrigo = buscaProfessor.buscaProfessor("Rodrigo");

        //Faz assertion
        assertEquals("Rodrigo", Rodrigo.getNome());
        assertEquals("08:00 - 09:00", Rodrigo.getHorarioDeAtendimento());
        assertEquals("integral", Rodrigo.getPeriodo());
        assertEquals("5", Rodrigo.getSala());
        assertTrue(Rodrigo.getPredio().contains("3"));
    }
    @Test
    public void testeBuscaProfessorFalhaRenan(){

        //Fiz a busca
        Professor Renan = buscaProfessor.buscaProfessor("Renan");

        //Faz assertion
        assertEquals("Renan", Renan.getNome());
        assertEquals("10:00 - 11:00", Renan.getHorarioDeAtendimento());
        assertEquals("integral", Renan.getPeriodo());
        assertEquals("7", Renan.getSala());
        assertTrue(Renan.getPredio().contains("6"));
    }
    @Test
    public void testeBuscaProfessorFalhaBruno(){

        //Fiz a busca
        Professor Bruno = buscaProfessor.buscaProfessor("Bruno");

        //Faz assertion
        assertEquals("Bruno", Bruno.getNome());
        assertEquals("15:00 - 16:00", Bruno.getHorarioDeAtendimento());
        assertEquals("integral", Bruno.getPeriodo());
        assertEquals("13", Bruno.getSala());
        assertTrue(Bruno.getPredio().contains("3"));
    }
    @Test
    public void testeBuscaProfessorFalhaInvalida(){

        //Fiz a busca
        Professor Invalida = buscaProfessor.buscaProfessor("Jose");

        //Faz assertion
        assertEquals("Marcelo", Invalida.getNome());
        assertEquals("-", Invalida.getHorarioDeAtendimento());
        assertEquals("-", Invalida.getPeriodo());
        assertEquals("-", Invalida.getSala());
        assertTrue(Invalida.getPredio().contains("-"));

    }
}